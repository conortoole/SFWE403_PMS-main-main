import Medicine
import NonPrescriptionItems

class Inventory:
    def __init__(self, medicine, nonPrescriptionItems, pharmacy):
        self.medicine = medicine
        self.nonPrescriptionItems = nonPrescriptionItems
        self.pharmacy = pharmacy

    def __str__(self):
        return self.medicine + " " + self.nonPrescriptionItems + " " + self.pharmacy
    
    def __hash__(self):
        return hash((self.medicine, self.nonPrescriptionItems, self.pharmacy))
    
    def get_medicine(self):
        return self.medicine
    
    def get_nonPrescriptionItems(self):
        return self.nonPrescriptionItems
    
    def get_pharmacy(self):
        return self.pharmacy
    
    def set_medicine(self, medicine):
        self.medicine = medicine

    def set_nonPrescriptionItems(self, nonPrescriptionItems):
        self.nonPrescriptionItems = nonPrescriptionItems

    def set_pharmacy(self, pharmacy):
        self.pharmacy = pharmacy

