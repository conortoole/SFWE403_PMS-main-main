import customtkinter as tk
import models.Customer as Customer
from models.Staff import PharmacyManager

def open_addCustomerView(cashierHome):
    #Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
        
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    manager = PharmacyManager("test")
    customer = Customer.Customer()

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Add Customer") 

    window.columnconfigure(0, weight = 0)
    window.columnconfigure(1, weight = 2)
    window.rowconfigure(0, weight = 2)
    window.rowconfigure(1, weight = 0)
    window.rowconfigure(2, weight = 0)
    window.rowconfigure(3, weight = 0)
    window.rowconfigure(4, weight = 0)
    window.rowconfigure(5, weight = 0)
    window.rowconfigure(6, weight = 0)
    window.rowconfigure(7, weight = 0)
    window.rowconfigure(8, weight = 0)
    window.rowconfigure(9, weight = 0)

    # frame = tk.CTkFrame(master=window) 
    # frame.pack(pady=20,padx=40,fill='both',expand=True) 

    button = tk.CTkButton(
        master=window,
        text="Add Customer",
        width=200,
        height=50,
        # bg="blue",
        # fg="yellow",
    )
    
    back = tk.CTkButton(
        master=window,
        text="Go Back",
        width=200,
        height=50,
        # bg="blue",
        # fg="yellow",
    )

    # labels are text
    label = tk.CTkLabel(master=window,text="Add Customer", font=("Fira Code", 25)) 
    label1 = tk.CTkLabel(master=window,text="First Name") 
    label2 = tk.CTkLabel(master=window,text="Last Name") 
    label3 = tk.CTkLabel(master=window,text="DOB in yyyy-mm-dd") 
    label4 = tk.CTkLabel(master=window,text="Address") 
    label5 = tk.CTkLabel(master=window,text="Phone") 
    label6 = tk.CTkLabel(master=window,text="Email") 
    label7 = tk.CTkLabel(master=window,text="Insurance") 

    success = tk.CTkLabel(master=window,text="Successfully Added!")  
    failure = tk.CTkLabel(master=window,text="Failed to Add!") 
    #These are the input fields
    firstNameIn = tk.CTkEntry(master=window, width=300)
    lastNameIn = tk.CTkEntry(master=window, width=300)
    bDayIn = tk.CTkEntry(master=window, width=300)
    adressIn = tk.CTkEntry(master=window, width=300)
    phoneIn = tk.CTkEntry(master=window, width=300)
    emailIn = tk.CTkEntry(master=window, width=300)
    insuranceIn = tk.CTkEntry(master=window, width=300)
    #this adds inputs to window
    label.grid(columnspan=2, row=0, padx=5, pady=5)
    label1.grid(column=0, row=1, padx=5, pady=5)
    firstNameIn.grid(column=1, row=1, padx=5, pady=5) 
    label2.grid(column=0, row=2, padx=5, pady=5)
    lastNameIn.grid(column=1, row=2, padx=5, pady=5) 
    label3.grid(column=0, row=3, padx=5, pady=5)
    bDayIn.grid(column=1, row=3, padx=5, pady=5)
    label4.grid(column=0, row=4, padx=5, pady=5) 
    adressIn.grid(column=1, row=4, padx=5, pady=5) 
    label5.grid(column=0, row=5, padx=5, pady=5)
    phoneIn.grid(column=1, row=5, padx=5, pady=5)
    label6.grid(column=0, row=6, padx=5, pady=5) 
    emailIn.grid(column=1, row=6, padx=5, pady=5)
    label7.grid(column=0, row=7, padx=5, pady=5) 
    insuranceIn.grid(column=1, row=7, padx=5, pady=5) 
    button.grid(column = 1, row=8, padx=5, pady=5)
    back.grid(column = 0, row=8, padx=5, pady=5)

    def handle_click(event): 
        # this gets info from input and puts into class
        customer.first_name = firstNameIn.get()
        customer.last_name = lastNameIn.get()
        customer.date_of_birth = bDayIn.get()
        customer.address = adressIn.get()
        customer.phone = phoneIn.get()
        customer.email = emailIn.get()
        customer.insurance = insuranceIn.get()
        #this adds the customer to database and checks if it worked
        test = manager.createPatient(customer)
        if test:
            failure.grid_remove() #removes from screen
            success.grid(columnspan=2, row=9, padx=5, pady=5) #adds to screen 
            #clears input fields
            clear_text(firstNameIn)
            clear_text(lastNameIn)
            clear_text(bDayIn)
            clear_text(adressIn)
            clear_text(phoneIn)
            clear_text(emailIn)
            clear_text(insuranceIn)
        else:
            success.grid_remove()
            failure.grid(columnspan=2, row=9, padx=5, pady=5) 

    def closeWindow(self):
        cashierHome.deiconify()
        window.destroy()

    def clear_text(text):
        text.delete(0, tk.END)

    button.bind("<Button-1>", handle_click) #connects function handle_click to button 
    back.bind("<Button-1>", closeWindow)
    #lets priors window know that this one will close itself

#window.mainloop() #constant loop for gui 
