#!/usr/bin/python3
import mysql.connector
import random, sys
from twilio.rest import Client

class CodeGenerator:

    def __init__(self, ID):
        self.ID = ID
        try:
            #Setting Up the 'auth_codes' access
            self.db_connect = mysql.connector.connect(user="root", password="alexandre", host="127.0.0.1", database="hacknotts")
            cursor = self.db_connect.cursor(buffered=True)
            cursor.execute("SELECT * FROM auth_codes;")
            self.auth_codes = cursor.fetchall()
            self.target_user_ac = self.auth_codes[ID-1]
            
            #Setting Up the 'users' access
            cursor = self.db_connect.cursor(buffered=True)
            cursor.execute(f"SELECT * FROM users;")
            self.users = cursor.fetchall()
            self.target_user = self.users[ID-1]
            self.phone_number = str(self.target_user[3])
            print(self.phone_number)

        except mysql.connector.InterfaceError:
            print("Could not connect to database.", file=sys.stderr)
            
    def send_message(self):
        account_sid = 'AC981838466c123165f5a99c5913488181'
        auth_token = 'f33080514f1b3e9cd3b7c6e6dc92748b'
        messaging_sid = '+447723412253' #'PN77be9d18bceff01b2e184040f98c516e'
        the_body = str(self.get_auth_code())
        try:            
            client = Client(account_sid, auth_token)
            client.messages.create(
                to = '+447579065474', #self.phone_number,
                from_ = messaging_sid,
                body = (f"Authorization Code: {the_body}")
                )
            
        except client.TwilioRestException as err:
            print(err)
            
    #Gets the latest authorization code assoisiated with this instance
    def get_auth_code(self):
        cursor = self.db_connect.cursor(buffered=True)
        cursor.execute("SELECT * FROM auth_codes;")
        code_in_db = cursor.fetchall()[self.ID - 1][2]
        return code_in_db    
    
    def get_auth_codes_table(self):
        return self.auth_codes


    def used_code(self, code):
        if code in self.target_user_ac[2]:
            return True


    def generate_code(self):
        code = ""
        for i in range(6):
            rand_num = random.randint(0, 9)            
            print(rand_num)
            code += str(rand_num)
            
        return code.zfill(6)
    
    
    def set_auth_code(self):
        code = self.generate_code()
        already_used = self.used_code(code)
        if not already_used:
            return code
        else:
            while already_used:
                code = self.generate_code()
            return code


    def update_auth_code(self):
        code = self.set_auth_code()
        ID = ID = self.ID
        
        try: 
            cursor = self.db_connect.cursor(buffered=True)
            cursor.execute(f"UPDATE hacknotts.auth_codes SET code = {code} WHERE id = {ID}")
            self.db_connect.commit
            
        except mysql.connector.Error as err:
            print(f"An error: {err}")
            
    
if __name__ == "__main__":
    CD = CodeGenerator(1)
    print(CD.get_auth_code())
    CD.update_auth_code()
    print("\n" + str(CD.get_auth_code()))
    CD.send_message()
   
    cursor = CD.db_connect.cursor(buffered=True)
    cursor.execute("SELECT * FROM auth_codes;")
    upd_auth_codes = cursor.fetchall()
    print(upd_auth_codes)
