import mysql.connector
from models import Customer

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()

def LoginLLL():
    
    userID = input("User ID\n")
    Password = input("password\n")

    mycursor.execute("SELECT * FROM PMS_Staff WHERE StaffID = %s and password = %s",(userID,Password))
    
    pswdreturn = mycursor.fetchone()
    
    if pswdreturn == None:
        print("Login Error\n") 
        return False, False, False
    
    else:
        print("Login Success")
        return True, pswdreturn[1],pswdreturn[2]
        

def Login1(userID,Password):
   
    mycursor.execute("SELECT * FROM PMS_Staff WHERE StaffID = %s and password = %s",(userID,Password))
    
    pswdreturn = mycursor.fetchone()
    
    if pswdreturn == None:
        return False
    else:
        return True
    
