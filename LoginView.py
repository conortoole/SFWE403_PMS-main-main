
import customtkinter as ctk 
from tkinter import messagebox

from models.Login import LoginLib
from controllers.LoginController import Login

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



class LoginGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x280")
        self.title("PMS Login")

        self.frame = ctk.CTkFrame(self) 
        self.frame.pack(pady=20,padx=40,fill='both',expand=True) 
        
        self.label = ctk.CTkLabel(self.frame,text='PMS Login System') 
        self.label.pack(pady=12,padx=10) 
        
        
        self.user_entry= ctk.CTkEntry(self.frame,placeholder_text="User ID") 
        self.user_entry.pack(pady=12,padx=10) 
        
        self.user_pass= ctk.CTkEntry(self.frame,placeholder_text="Password",show="*") 
        self.user_pass.pack(pady=12,padx=10) 

        def loginlogic():
            logindata = LoginLib( UserID = self.user_entry.get(), password = self.user_pass.get())
            result = Login(logindata)
            if result != None:
                messagebox.showinfo("Success","Login Successful")
            else:
               messagebox.showinfo("Failed","Login Failed, please check ID and Password") 
        

        self.button = ctk.CTkButton(self.frame,text='Login',command=loginlogic) 
        self.button.pack(pady=12,padx=10) 

if __name__=='__main__':
    app = LoginGUI()
    app.mainloop()
        