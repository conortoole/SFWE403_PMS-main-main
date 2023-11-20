class Customer:
    
    def __init__(self, first_name, last_name, date_of_birth, address, phone, email, insurance):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.insurance = insurance
        
    def __init__(self):
        self.first_name = "default"
        self.last_name = "default"
        self.date_of_birth = "0-00-00"
        self.address = "default"
        self.phone = "0000000000"
        self.email = "default@default.com"
        self.insurance = "default"