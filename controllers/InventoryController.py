import mysql.connector

#The idea would be to call a instance of inventory controller in main pass in mydb or whatever the sql connector is
#and then whenever you want to add or remove either a medicine or a prescription you just call the functions in the controller

class inventoryController:

    def __init__(self):
        self.counter = 0
        
    def addPrescription(self, newPrescription): #currently needs to connect to the database in call  
        mydb = mysql.connector.connect(         #note: customer Id must match a real customer ID
            host = 'mysql-145311-0.cloudclusters.net',
            port = '18166',
            user = 'admin',
            passwd = 'FcCZds4d',
            db = 'PMS'
        )
        mycursor = mydb.cursor()
        
        sql = "INSERT INTO PMS_Prescription (prescription, customerID, startDate, endDate, medication, quantity, strength, refills, instructions, prescriber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (newPrescription.prescription, newPrescription.customerID, newPrescription.startDate, newPrescription.endDate, newPrescription.medication, newPrescription.quantity, newPrescription.strength, newPrescription.refills, newPrescription.instructions, newPrescription.prescriber)
        mycursor.execute(sql, val)
        mydb.commit()

    def removePrescription(self, newPrescription): 
        mydb = mysql.connector.connect(
            host = 'mysql-145311-0.cloudclusters.net',
            port = '18166',
            user = 'admin',
            passwd = 'FcCZds4d',
            db = 'PMS'
        )
        mycursor = mydb.cursor()

        sql = "DELETE FROM PMS_Prescription WHERE prescription = " +  newPrescription.prescription
        mycursor.execute(sql)
        mydb.commit()

    # def addMedicine(Medicine, connector):
        
    #     sql = "INSERT INTO PMS_MEDICINE (#class attributes) VALUES (%s, %s, %s, )"
    #     val = ("newPrescription.prescription", "newPrescription.customerID", "newPrescription.startDate", "newPrescription.endDate", "newPrescription.medication", "newPrescription.quantity")
    #     connector.execute(sql, val)

    # def removeMedicine(Medicine, connector):
        
    #     sql = "DELETE FROM PMS_MEDICINE WHERE medicineID = 'Medicine.medicineID'"
    #     connector.execute(sql)
