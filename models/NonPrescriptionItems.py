
class NonPrescriptionItems:
    def __init__(self, name, brand, price, itemInfo, type, state): 
        self.name = name
        self.brand = brand
        self.type = type
        self.price = price
        self.state = state
        self.itemInfo = itemInfo

    def __str__(self):
        return self.name + " " + self.brand + " " + self.type + " " + self.price + " " + self.state + " " + self.itemInfo
    
    def __hash__(self):
        return hash((self.name, self.brand, self.type, self.price, self.state, self.itemInfo))
    
    def get_name(self):
        return self.name
    
    def get_brand(self):
        return self.brand
    
    def get_type(self):
        return self.type

    def get_price(self):
        return self.price
    
    def get_state(self):
        return self.state
    
    def get_itemInfo(self):
        return self.itemInfo
    
    def set_name(self, name):
        self.name = name

    def set_brand(self, brand):
        self.brand = brand

    def set_type(self, type):
        self.type = type

    def set_price(self, price):
        self.price = price

    def set_state(self, state):
        self.state = state

    def set_itemInfo(self, itemInfo):
        self.itemInfo = itemInfo
