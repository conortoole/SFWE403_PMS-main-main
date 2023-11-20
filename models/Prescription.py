from Staff import Pharmacist
import Patient
from datetime import datetime

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


class Prescription:
    def __init__(self, medicine, dosage, doseFrequency, duration, refillDate, pharmacist, patient, prescriptionID):
        self.medicine = medicine
        self.dosage = dosage
        self.doseFrequency = doseFrequency
        self.duration = duration
        self.refillDate = canonical_date(refillDate)
        self.pharmacist = pharmacist
        self.patient = patient
        self.prescriptionID = prescriptionID

    def __str__(self):
        return "Medicine: {}\nDosage: {}\nDosage Frequency: {}\nDuration: {}\nRefill Date: {}\nPharmacist: {}\nPatient: {}\nPrescription ID: {}".format(self.medicine, self.dosage, self.doseFrequency, self.duration, self.refillDate, self.pharmacist, self.patient, self.prescriptionID)
    
    def __hash__(self):
        return hash((self.medicine, self.dosage, self.doseFrequency, self.duration, self.refillDate, self.pharmacist, self.patient, self.prescriptionID))
    
    def get_medicine(self):
        return self.medicine
    
    def get_dosage(self):
        return self.dosage
    
    def get_doseFrequency(self):
        return self.doseFrequency
    
    def get_duration(self):
        return self.duration
    
    def get_refillDate(self):
        return self.refillDate
    
    def get_pharmacist(self):
        return self.pharmacist
    
    def get_patient(self):
        return self.patient
    
    def get_prescriptionID(self):
        return self.prescriptionID
    
    def set_medicine(self, medicine):
        self.medicine = medicine

    def set_dosage(self, dosage):
        self.dosage = dosage

    def set_doseFrequency(self, doseFrequency):
        self.doseFrequency = doseFrequency

    def set_duration(self, duration):
        self.duration = duration

    def set_refillDate(self, refillDate):
        self.refillDate = refillDate

    def set_pharmacist(self, pharmacist):
        self.pharmacist = pharmacist

    def set_patient(self, patient):
        self.patient = patient

    def set_prescriptionID(self, prescriptionID):
        self.prescriptionID = prescriptionID

    
        