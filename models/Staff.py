from datetime import datetime
from abc import ABC, abstractmethod
import warnings
from models.Customer import Customer
import mysql.connector

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()

def canonical_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        try:
            date = datetime.strptime(date_str, '%m/%d/%Y')
        except ValueError:
            try:
                date = datetime.strptime(date_str, '%d-%b-%Y')
            except ValueError:
                return None
    return date.strftime('%Y-%m-%d')

class Staff(ABC):
    @abstractmethod
    def __init__(self, name, birth_date, address, phone_number, email, username, password):
        self.name = name
        self.birth_date = canonical_date(birth_date)
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    @abstractmethod
    def __str__(self):
        return "Staff Name: {}\nBirth Date: {}\nAddress: {}\nPhone Number: {}\nEmail: {}\nUsername: {}\nPassword: {}".format(self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password)

    @abstractmethod
    def __repr__(self):
        return "Staff('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password)
    
    @abstractmethod
    def __eq__(self, other):
        return self.name == other.name and self.birth_date == other.birth_date and self.address == other.address and self.phone_number == other.phone_number and self.email == other.email and self.username == other.username and self.password == other.password
    
    @abstractmethod
    def __ne__(self, other):
        return not self.__eq__(other)
    
    @abstractmethod
    def __hash__(self):
        return hash((self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password))
    

    def get_name(self):
        return self.name
    
    def get_birth_date(self):
        return self.birth_date 
    
    def get_address(self):
        return self.address
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def set_name(self, name):
        self.name = name

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def createPatient(self, customer):
        success = False
        #print(first_name, ' ', last_name, ' ', DOB.month, "/", DOB.day, "/", DOB.year, ' ',address, ' ',phone, ' ',email, ' ',insurance, sep= '')
        try:
            mycursor.execute("INSERT INTO Customer (lastName, firstName, DOB, Address, phoneNum, email, insurance) VALUES (%s, %s, %s, %s, %s, %s, %s)", (customer.last_name, customer.first_name, customer.date_of_birth, customer.address, customer.phone, customer.email, customer.insurance))
            mydb.commit()
            success = True
        except:
            success = False 
        return success

    def fetchCustomer(self, customerID):
        try:                 #SELECT * FROM PMS.Customer where Customer_ID = 3
            mycursor.execute("SELECT * FROM Customer where Customer_ID = %s", (customerID,))
            customerInfo =  mycursor.fetchall()
        except Exception as e:
            print("failed to get customer: ", e)
        return customerInfo
    
    def fetchID(self, customer):
        try:                 #SELECT Customer_ID FROM PMS.Customer where firstName = 'conor' and lastName = 'toole'
            mycursor.execute("SELECT Customer_ID FROM Customer where firstName = %s and lastName = %s", (customer.first_name, customer.last_name))
            customerInfo = mycursor.fetchone()
            return str(customerInfo[0])
        except Exception as e:
            print("failed to get id: ", e)

    def loadCustomer(self):
        customer1 = Customer()
        customer1.first_name = input("Enter first name:")
        customer1.last_name = input("Enter last name:")
        customer1.date_of_birth = input("Enter DOB as YYYY-MM-DD")
        #DOB = datetime.strptime(date_of_birth, '%Y/%m/%d')
        customer1.address = input("Enter address:")
        customer1.phone = input("Enter phone number:")
        customer1.email = input("Enter email address:")
        customer1.insurance = input("Enter insurance information:")
        return customer1

    def UpdateCustomer(self, customer, customerID):
        try:   
            mycursor.execute("UPDATE Customer set firstName = %s, lastName = %s, DOB = %s, Address = %s, phoneNum = %s, email = %s, insurance = %s where Customer_ID = %s",(customer.first_name, customer.last_name,customer.date_of_birth,customer.address,customer.phone,customer.email,customer.insurance, customerID))
            mydb.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def enterPrescription(self):
        prescriptionID = input("Enter the prescription ID: ")

        #Get name and split
        customerName = input("\nEnter the name of the customer (first last): ")
        x = customerName.split()
        firstName = x[0]
        lastName = x[1]
        
        mycursor.execute("SELECT Customer_ID FROM Customer WHERE lastName = %s and firstName = %s",(lastName,firstName))
        customerID = mycursor.fetchone()
        customerID = customerID[0]
        

        prescriptionStartDate = input("\nEnter the start date for the medication in the form YYYY/MM/DD: ")
        prescriptionEndDate = input("\nEnter the end date for the prescription in the form YYYY/MM/DD: ")

        prescriptionMedication = input("\n Enter the name of the medication on the prescription: ")

        prescriptionQuantity = input("\nEnter the amount of the medication per refill: ")
        prescriptionStrength = input("\nEnter the strength: ")
        prescriptionRefills = input("\nEnter the amount of refills: ")
        instructions = input("\nEnter the instructions:")
        pName = input("\nEnter the pharmacist name:")
        
        mycursor.execute("INSERT INTO PMS_Prescription (prescription, customerID, startDate, endDate, medication, quantity, strength, refills, instructions, prescriber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )", (prescriptionID, customerID, prescriptionStartDate, prescriptionEndDate, prescriptionMedication, prescriptionQuantity, prescriptionStrength, prescriptionRefills, instructions, pName))
        mydb.commit()

    def addPrescription(self, newPrescription):  
        sql = "INSERT INTO PMS_Prescription (prescription, customerID, startDate, endDate, medication, quantity, strength, refills, instructions, prescriber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (newPrescription.prescription, newPrescription.customerID, newPrescription.startDate, newPrescription.endDate, newPrescription.medication, newPrescription.quantity, newPrescription.strength, newPrescription.refills, newPrescription.instructions, newPrescription.prescriber)
        mycursor.execute(sql, val)
        mydb.commit()

    def removePrescription(self, newPrescription): 
        sql = "DELETE FROM PMS_Prescription WHERE prescription = " +  newPrescription.prescription
        mycursor.execute(sql)
        mydb.commit()

    def fetchItem(self, name):
        try:                 
            mycursor.execute("SELECT * FROM Inventory where medName = %s", (name,))
            itemInfo = mycursor.fetchall()
            for item in itemInfo: #goes through all the batches and compares exp date
                if item[5] > datetime.today().date(): #takes first one thats not expired
                    return item
                else:
                    item = None
            return item
        except Exception as e:
            print("failed to get item: ", e)

    def updateInventory(self, items):
        try:
            for item in items:   
                olditem = self.fetchItem(item.name)
                num = olditem[2] - item.quantity
                mycursor.execute("UPDATE Inventory set quantity = %s where medName = %s", (num, olditem[0]))
                mydb.commit()
            return True
        except:
            return False
        
    def addCart(self, item):
        self.cart.append(item)

    def calculateTotal(self):
        total = 0
        for item in self.cart:
            total = total + (float(item.price) * float(item.quantity))
        return total
    
    def fetchCart(self):
        return self.cart

class PharmacyManager(Staff):
    def __init__(self, name):
        pass

    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __hash__(self):
        pass

    def createPharmacyAccount(self):
        role = input("Enter role (Manager, Pharmacist, Pharmacist technician, Cashier):")
        name = input("Enter full name:")
        password = input("Create password:")

        mycursor.execute("INSERT INTO PMS_Staff (role, name, password) VALUES (%s, %s, %s)", (role, name, password))
        mydb.commit()

    def removePatient(self, customerID):
        #!!!!!!!!!!!!!if you want to delete customer you must first delete reference in prescription!!!!!!!!
        try:
            if customerID:
                try:
                    mycursor.execute("DELETE FROM PMS_Prescription WHERE CustomerID = %s", (customerID,))
                    mycursor.execute("DELETE FROM Customer WHERE Customer_ID = %s", (customerID,))
                    mydb.commit()
                    return True
                except:
                    return False
        except Exception as e:
            print("Failed to delete customer: ", e)
            return False

    def recoverStaffAccount(self):
        pass

    def orderMedication(self, Medicine):
        success = False
        try:
            mycursor.execute("INSERT INTO Inventory (medName, quantity, strength, batchNum, expDate, price) VALUES (%s, %s, %s, %s, %s, %s)", ( Medicine.name, Medicine.quantity, Medicine.strength, Medicine.batch, Medicine.expDate, Medicine.price))
            mydb.commit()
            success = True
        except:
            success = False 
        return success

    def fetchMedicineID(self, medicine):
        try:                 #SELECT Customer_ID FROM PMS.Customer where firstName = 'conor' and lastName = 'toole'
            mycursor.execute("SELECT item_id FROM Inventory where medName = %s and batchNum = %s", (medicine.name, medicine.batch))
            medicineInfo = mycursor.fetchone()
            return str(medicineInfo[0])
        except Exception as e:
            print("failed to get id: ", e)

    def removeItem(self, medicineID):
        success = False
        try:       
            mycursor.execute("DELETE FROM Inventory WHERE item_id = %s",(medicineID,))
            mydb.commit()
            success = True
        except Exception as e:
            print(e)
            success = False
        return success
            

    def generateFinancialReport(self):
        pass

    def generateInventoryReport(self):
        pass

    
    

class Pharmacist(Staff):
    def __init__(self, name):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __hash__(self):
        pass

    def removePatient(self):
        firstName =input("Patient first name\n")
        lastName =input("Patient last name\n")        
        mycursor.execute(("DELETE FROM Customer WHERE firstName = %s and lastName = %s"),(firstName,lastName))
        
    def checkAvailability(self):
        pass

    def fillPrescription(self):
        # log()
        pass

    def log(self, Prescription):
        f = open("log.txt", "a")
        f.write(("prescription name: %s\nfilled by: %s\npatients name: %s\ndate: %s\nmedicine: %s\nquantity: %s"), (Prescription.prescription,Prescription.prescriber,Prescription.customerID,Prescription.startDate,Prescription.medication,Prescription.quantity))
        f.write("\n")
        f.close()

    
    
        

class PharmacistTechnician(Staff):
    def __init__(self, name, birth_date, address, phone_number, email, username, password, pharmacy):
        pass    
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __hash__(self):
        pass
    
    

class Cashier(Staff):
    def __init__(self):
        self.cart = []
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __hash__(self):
        pass

    

    
    
    
    

    


    
