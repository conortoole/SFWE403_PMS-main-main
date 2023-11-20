class LoginLib:

    def __init__(self,UserID=0,password=None):
        self.UserID = UserID
        self.password = password

    def getID(self):
        return self.UserID

    def getPassword(self):
        return self.password  

    def setID(self, idnum):
        self.UserID = idnum  

    def setPassword(self,password):
        self.password = password

    def __str__(self):
        return ('{}','{}'.format(self.UserID,self.password))