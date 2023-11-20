from models.Staff import Pharmacist

class PharmacistController:
    def __init__(self, pharmacist):
        self._pharmacist = Pharmacist(pharmacist)

    def run(self):
        session = True
        while session != False:
            pharmacistAction = input("Add Prescription, Fill Prescription, Check Out")
            if (pharmacistAction == "Add Prescription"):
                self._pharmacist.enterPrescription()
                continue
            elif (pharmacistAction == "Fill Prescription"):
                #self._pharmacist.FillPrescription
                continue
            elif (pharmacistAction == "Log Out"):
                session = False
            else:
                print("error")