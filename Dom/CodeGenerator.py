import os, random, requests, mysql.connector
#from twilio.rest import Client

class CodeGenerator:
        
    def __init__(self, id):
        self.id = id
        
    dbconnect = mysql.connector.connect(user = "root", password = "alexandre", host = "127.0.0.1", database = "hacknotts")
    cursor = dbconnect.cursor()
    cursor.execute("CREATE TABLE auth_codes (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, user_id INT NOT NULL, code VARCHAR(6) NOT NULL, used TINYINT(1) DEFAULT 0 NOT NULL);")
    cursor.execute("SHOW TABLES")
    
    for c in cursor:
        print(c)
    
    
    #users = cursor.execute("QUERY", (auth_codes, c))





        
            

    

    



