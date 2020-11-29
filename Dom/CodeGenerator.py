#!/usr/bin/python3
import mysql.connector
import random, sys
# from twilio.rest import Client

class CodeGenerator:

    def __init__(self, ID):
        self.ID = ID
        try:
            self.db_connect = mysql.connector.connect(user="root", password="alexandre", host="127.0.0.1", database="hacknotts")
            cursor = self.db_connect.cursor(buffered=True)
            cursor.execute("SELECT * FROM auth_codes;")
            self.auth_codes = cursor.fetchall()
            self.target_user = self.auth_codes[ID-1]
            #for (codeid, userid, code, used) in self.auth_codes:
            #    print(codeid, code)

        except mysql.connector.InterfaceError:
            print("Could not connect to database.", file=sys.stderr)

    def get_auth_codes_table(self):
        return self.auth_codes


    def used_code(self, code):
        if code in self.target_user[2]:
            return True

    def generate_code(self):
        code = ""
        valid_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(6):
            rand_num = valid_digits[random.randint(0, 9)]
            print(rand_num)
            code += str(rand_num)
            
        return format(code, '010d')
    
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
        ID = self.target_user[0]
        
        try: 
            cursor = self.db_connect.cursor(buffered=True)
            cursor.execute(f"UPDATE hacknotts.auth_codes SET code = {code} WHERE id = {ID}")
            self.db_connect.commit
            
        except mysql.connector.Error as err:
            print(f"An error: {err}")
            
if __name__ == "__main__":
    CD = CodeGenerator(1)
    CD.update_auth_code()
    cursor = CD.db_connect.cursor(buffered=True)
    cursor.execute("SELECT * FROM auth_codes;")
    upd_auth_codes = cursor.fetchall()
    print(upd_auth_codes)
    #for user in CD.auth_codes:
     #   print(__name__ + "\n" + str(user) + "\n" + str(user[0]) + ", " + str(user[2]))