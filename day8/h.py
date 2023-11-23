import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="")
if mydb:
    print("Connected")
else:
    print("Connection error")