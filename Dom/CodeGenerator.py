#!/usr/bin/python3
import mysql.connector
import random, sys, os
import twilio
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
            self.phone_number = self.target_user[3]

        except mysql.connector.InterfaceError:
            print("Could not connect to database.", file=sys.stderr)
            
    def send_message(self):
        account_sid = os.environ.get('TWILIO_ACC_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        messaging_sid = os.environ.get('MESSAGING_SERVICE_SID')
        try:            
            client = Client(account_sid, auth_token)
            client.messages.create(
                to = os.environ.get('MY_PHONE_NUMBER'), #self.phone_number,
                from_ = messaging_sid,
                body = "Authorization Code: " + str(self.get_auth_code())
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
    # CD.send_message()
   
    account_sid = os.environ.get('TWILIO_ACC_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    messaging_sid = os.environ.get('MESSAGING_SERVICE_SID')
    print(account_sid, auth_token, messaging_sid) 
   
    cursor = CD.db_connect.cursor(buffered=True)
    cursor.execute("SELECT * FROM auth_codes;")
    upd_auth_codes = cursor.fetchall()
    print(upd_auth_codes)
    #for user in CD.auth_codes:
     #   print(__name__ + "\n" + str(user) + "\n" + str(user[0]) + ", " + str(user[2]))