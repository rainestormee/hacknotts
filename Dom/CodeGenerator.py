import os, random, requests, mysql.connector
#from twilio.rest import Client

class CodeGenerator:
        
    def __init__(self, id):
        self.id = id
    

   # def create_code(self.id):
    #    code = ""
     #   for i in range(5):
      #      random = random
        
        
            
    dbconnect = mysql.connector.connect(user = "root", password = "alexandre", host = "127.0.0.1", database = "hacknotts")    
    #response = requests.get(dbconnect)

gen = CodeGenerator(1)

print(gen.response)