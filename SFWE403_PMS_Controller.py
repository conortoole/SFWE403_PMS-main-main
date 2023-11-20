import mysql.connector
from datetime import datetime
from SFWE403_PMS_Model import *
from controllers.PharmacistController import PharmacistController
from models.Staff import Pharmacist
from models.Staff import PharmacyManager
from controllers.PharmacyManagerController import PharmacyManagerController

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()
    
if __name__ == '__main__':
    loggedIn = False
    while loggedIn != True:
        loginResult=Login()
        if loginResult[0] == True:
            loggedIn=loginResult[0]
    
    while loggedIn == True:
        rolereturn = str(loginResult[2])
        if rolereturn == "manager":
            pharmacist_manager_name = rolereturn[1]
            pharManagerControllerInstance = PharmacyManagerController(pharmacist_manager_name)
            while 1:
                pharManagerControllerInstance.run()
                prompt = str(input("Are you sure you want to log out? (y/n) \n")).strip().lower()
                if prompt == 'y':
                    loggedIn = False
                    break
                else:
                    continue
                    
                
                
                
        elif rolereturn == "pharmacist":
            pharmacist_name = rolereturn[1]
            pharmacistControllerInstance = PharmacistController(pharmacist_name)
            while 1:
                pharmacistControllerInstance.run()
                prompt = str(input("Are you sure you want to log out? (y/n)\n")).strip().lower()
                if prompt == 'y':
                    loggedIn = False
                else:
                    continue


            
        
    
    
   
