import customtkinter as tk
#import addCustomerView as acv


CashierHome = tk.CTk()
CashierHome.geometry("700x200")
CashierHome.title("Manager Homepage")

#should add instant check for low stock or expired notifications

AddUserButton = tk.CTkButton(
    master = CashierHome,
    text = "Add User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = acv.open_addCustomerView()
)

UpdateUserButton = tk.CTkButton(
    master = CashierHome,
    text = "Update User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open updatecustomer view 
)

DeleteUserButton = tk.CTkButton(
    master = CashierHome,
    text = "Delete User",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open deletecustomer view 
)

UpdateInventory = tk.CTkButton(
    master = CashierHome,
    text = "Update Inventory",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open checkout view 
)

DeleteInventory = tk.CTkButton(
    master = CashierHome,
    text = "Delete Inventory",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open checkout view 
)

RecoverUserAccount = tk.CTkButton(
    master = CashierHome,
    text = "Recover User Account",
    width = 200,
    height = 50,
    #bg = "blue",
    #fg = "yellow",
    #font = 10,
    #command = open checkout view 
)




AddUserButton.grid(row = 0, column = 0, padx=10, pady=10)
UpdateUserButton.grid(row = 0, column = 20, padx=10, pady=10)
DeleteUserButton.grid(row = 0, column = 40, padx=10, pady=10)
UpdateInventory.grid(row = 50, column = 0,  padx=10, pady=10)
DeleteInventory.grid(row = 50, column = 20,  padx=10, pady=10)
RecoverUserAccount.grid(row = 50, column = 40,  padx=10, pady=10)

    


CashierHome.mainloop()