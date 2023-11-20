import tkinter as tk



window = tk.Tk()
window.geometry("750x500")
window.title("Pharmacist Homepage")


AddCustomerButton = tk.Button(
    text = "Add Customer",
    width = 20,
    height = 5,
    bg = "blue",
    fg = "yellow",
    font = 10,
    #command = open addcustomer view 
)

UpdateCustomerButton = tk.Button(
    text = "Update Customer",
    width = 20,
    height = 5,
    bg = "blue",
    fg = "yellow",
    font = 10,
    #command = open updatecustomer view 
)

DeleteCustomerButton = tk.Button(
    text = "Delete Customer",
    width = 20,
    height = 5,
    bg = "blue",
    fg = "yellow",
    font = 10,
    #command = open deletecustomer view 
)

FillPrescriptionButton = tk.Button(
    text = "Fill Prescription", 
    width = 20, 
    height = 5, 
    bg = "blue", 
    fg = "yellow", 
    font = 10,
    #command = open fillprescription view 
)

NewPrescriptionButton = tk.Button(
    text = "Enter New Prescription", 
    width = 20, 
    height = 5, 
    bg = "blue", 
    fg = "yellow", 
    font = 10,
    #command = open enter new prescription view 
)

CheckAvailabilityButton = tk.Button(
    text = "Check Med Availability", 
    width = 20, 
    height = 5, 
    bg = "blue", 
    fg = "yellow", 
    font = 10,
    #command = open checkavailability view 
)

CheckoutButton = tk.Button(
    text = "Checkout", 
    width = 20, 
    height = 5, 
    bg = "blue", 
    fg = "yellow", 
    font = 10,
    #command = open checkout view 
)

AddCustomerButton.grid(row = 0, column = 0, padx=10, pady=10)
UpdateCustomerButton.grid(row = 0, column = 20, padx=10, pady=10)
DeleteCustomerButton.grid(row = 0, column = 40, padx=10, pady=10)
FillPrescriptionButton.grid(row = 50, column = 0, padx=10, pady=10)
NewPrescriptionButton.grid(row = 50, column = 20, padx=10, pady=10)
CheckAvailabilityButton.grid(row = 50, column = 40, padx=10, pady=10)
CheckoutButton.grid(row = 100, column = 20,  padx=10, pady=10)


window.mainloop()