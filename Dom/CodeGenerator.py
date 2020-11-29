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
            #self.target_user = [user for user in self.auth_codes if user[0] == ID]
            self.target_user = self.auth_codes[ID-1]
            print(self.target_user)
           # for (codeid, userid, code, used) in self.auth_codes:
           #     print(codeid, code)
            for (codeid, userid, code, used) in self.target_user:
                print(codeid, code)

        except mysql.connector.InterfaceError:
            print("Could not connect to database.", file=sys.stderr)

    def get_auth_codes_table(self):
        return self.auth_codes


    def used_code(self, code):
        if code in self.target_user[2]:
            return True

    def generate_code(self):
        code = ""
        for i in range(5):
            rand_num = random.randint(0, 9)
            code += str(rand_num)
        return code
    
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
        ID = self.target_user
        to_execute = '''
                UPDATE hacknotss.auth_codes
                SET code = %s
                WHERE id = %s
                location = "UPDATE auth_codes SET code = " + str(self.target_user)
                '''
        val = (code, ID)
        try: 
            cursor = self.db_connect.cursor(buffered=True)
            cursor.execute(to_execute, val)
            self.db_connect.commit
        except:
            print("Syntax Wrong")
            
            
            
            
if __name__ == "__main__":
    CD = CodeGenerator(1)
    #CD.update_auth_code()
    for user in CD.auth_codes:
        print(str(user) + "\n" + str(user[0]) + ", " + str(user[3]))
        

# create table auth_codes (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, user_id INT NOT NULL, code VARCHAR(6) NOT NULL, used TINYINT(1) DEFAULT 0 NOT NULL);


# cursor.execute("SELECT * FROM users")

# users = cursor.fetchall()

# for u in users:
#     print(u)


# for c in CD.auth_codes:
#     print(c)


# check auth_codes for the id
# generate a code for the id
# check if the code is already use
# if not, insert the code into the auth_codes[2] (which is code)
