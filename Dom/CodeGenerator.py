#!/usr/bin/python3
import mysql.connector
import random, sys
# from twilio.rest import Client

class CodeGenerator:

    def __init__(self, ID):
        self.ID = ID
        try:
            db_connect = mysql.connector.connect(user="root", password="alexandre", host="127.0.0.1", database="hacknotts")
            cursor = db_connect.cursor()
            cursor.execute("SELECT * FROM auth_codes")
            auth_codes = cursor.fetchall()
            self.target_user = auth_codes.index(ID)
        except mysql.connector.InterfaceError:
            print("Could not connect to database.", file=sys.stderr)
        #    self.generated_code = create_code()

    def generate_code(self):
        r = random()
        code = ""
        for i in range(5):
            rand_num = r.randint(0, 9)
            code += str(rand_num)
        return code

    def check_code(self, code):
        if code in self.target_user[2]:
            return False

    def get_auth_codes_table(self):
        return self.auth_codes


if __name__ == "__main__":
    CD = CodeGenerator(1)
    print(CD.generate_code())
    for users in CD.get_auth_codes_table():
        print(users)


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
