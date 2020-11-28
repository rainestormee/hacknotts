import os, random, requests, mysql.connector
#from twilio.rest import Client

class CodeGenerator:
        
    def __init__(self, id):
        self.id = id
        
    dbconnect = mysql.connector.connect(user = "root", password = "alexandre", host = "127.0.0.1", database = "hacknotts")
    cursor = dbconnect.cursor()
   
    cursor.execute("SELECT * FROM users WHERE")
    
    users = cursor.fetchall()
    
    for u in users:
        print(u[0])




   #cursor.execute("SELECT * FROM auth_codes")
    
   #auth_code_res = cursor.fetchall()
    
       #for a in auth_code_res:
           #print(a)       
            

    

    



