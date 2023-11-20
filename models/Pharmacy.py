class Pharmacy:
    
    def __init__(self, name, address, phone_number, work_hours, website, owner):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.work_hours = work_hours
        self.website = website
        self.owner = owner
    
    def __str__(self):
        return "Pharmacy Name: {}\nAddress: {}\nPhone Number: {}\nWork Hours: {}\nWebsite: {}\nOwner: {}".format(self.name, self.address, self.phone_number, self.work_hours, self.website, self.owner)
    
    def __repr__(self):
        return "Pharmacy('{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.address, self.phone_number, self.work_hours, self.website, self.owner)
    
    def __eq__(self, other):
        return self.name == other.name and self.address == other.address and self.phone_number == other.phone_number and self.work_hours == other.work_hours and self.website == other.website and self.owner == other.owner
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.name, self.address, self.phone_number, self.work_hours, self.website, self.owner))
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number
    
    def get_work_hours(self):
        return self.work_hours
    
    def get_website(self):
        return self.website
    
    def get_owner(self):
        return self.owner
    
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_work_hours(self, work_hours):
        self.work_hours = work_hours

    def set_website(self, website):
        self.website = website

    def set_owner(self, owner):
        self.owner = owner

# Path: models/Prescription.py
