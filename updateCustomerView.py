import customtkinter as tk
from models.Customer import Customer
from models.Staff import PharmacyManager


def open_updateCustomerView(cashierHome):
    # Selecting GUI theme - dark, light , system (for system default) 
    tk.set_appearance_mode("dark") 
    
    # Selecting color theme - blue, green, dark-blue 
    tk.set_default_color_theme("blue") 

    manager = PharmacyManager("test")
    customer = Customer()

    window = tk.CTkToplevel()
    window.geometry("500x500") 
    window.title("Update Customer") 

    window.columnconfigure(0, weight = 0)
    window.columnconfigure(1, weight = 2)
    window.rowconfigure(0, weight = 0)
    window.rowconfigure(1, weight = 0)
    window.rowconfigure(2, weight = 0)
    window.rowconfigure(3, weight = 0)
    window.rowconfigure(4, weight = 0)
    window.rowconfigure(5, weight = 0)
    window.rowconfigure(6, weight = 0)
    window.rowconfigure(7, weight = 0)
    window.rowconfigure(8, weight = 0)
    window.rowconfigure(9, weight = 0)
    window.rowconfigure(10, weight = 0)
    window.rowconfigure(11, weight = 0)
    window.rowconfigure(12, weight = 0)

    customerID2 = 0

    button = tk.CTkButton(
        master=window,
        text="Update Customer",
        font=("Fira Code", 15),
        width=200,
        height=50,
    )

    button2 = tk.CTkButton(
        master=window,
        text="Load Customer",
        font=("Fira Code", 15),
        width=200,
        height=50,
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
    label = tk.CTkLabel(master=window,text="What is the first and last name of the Customer?") 
    label1 = tk.CTkLabel(master=window,text="First Name") 
    label2 = tk.CTkLabel(master=window,text="Last Name") 
    label3 = tk.CTkLabel(master=window,text="DOB in yyyy-mm-dd") 

    success = tk.CTkLabel(master=window,text="Successfully Added!")  
    failure = tk.CTkLabel(master=window,text="Failed to Load Customer!") 
    #These are the input fields
    nameIn = tk.CTkEntry(master=window, width=300)
    firstNameIn = tk.CTkEntry(master=window, width=300)
    lastNameIn = tk.CTkEntry(master=window, width=300)
    bDayIn = tk.CTkEntry(master=window, width=300)
    adressIn = tk.CTkEntry(master=window, width=300)
    phoneIn = tk.CTkEntry(master=window, width=300)
    emailIn = tk.CTkEntry(master=window, width=300)
    insuranceIn = tk.CTkEntry(master=window, width=300)
    #this adds inputs to window
    label.grid(columnspan=2, row=0, padx=5, pady=5)
    nameIn.grid(columnspan=2, row=1, padx=5, pady=5)
    button2.grid(columnspan=2, row=2, padx=5, pady=5)
    back.grid(columnspan=2, row=11, padx=5, pady=5)


    def load(event):
        name = nameIn.get()
        nameSplit = name.split(" ")
        if (len(nameSplit) > 1):
            customer.first_name = nameSplit[0]
            customer.last_name = nameSplit[1]
        try:
            failure.grid_remove()

            customerID = manager.fetchID(customer)
            customerInfo = manager.fetchCustomer(customerID)
            
            firstNameIn.insert(0, customerInfo[0][2])
            lastNameIn.insert(0, customerInfo[0][1])
            bDayIn.insert(0, customerInfo[0][3]) 
            adressIn.insert(0, customerInfo[0][4])
            phoneIn.insert(0, customerInfo[0][5])
            emailIn.insert(0, customerInfo[0][6])
            insuranceIn.insert(0, customerInfo[0][7])

            firstNameIn.grid(columnspan=2, row=3, padx=5, pady=5) 
            lastNameIn.grid(columnspan=2, row=4, padx=5, pady=5) 
            bDayIn.grid(columnspan=2, row=5, padx=5, pady=5) 
            adressIn.grid(columnspan=2, row=6, padx=5, pady=5) 
            phoneIn.grid(columnspan=2, row=7, padx=5, pady=5) 
            emailIn.grid(columnspan=2, row=8, padx=5, pady=5) 
            insuranceIn.grid(columnspan=2, row=9, padx=5, pady=5)
            button.grid(columnspan=2, row=10, padx=5, pady=5)
        except Exception as e:
            failure.grid(columnspan=2, row=3, padx=5, pady=5) 
            print(e)

    def update(event): 
        # this gets info from input and puts into class
        customer.first_name = firstNameIn.get()
        customer.last_name = lastNameIn.get()
        customer.date_of_birth = bDayIn.get()
        customer.address = adressIn.get()
        customer.phone = phoneIn.get()
        customer.email = emailIn.get()
        customer.insurance = insuranceIn.get()
        #this adds the customer to database and checks if it worked
        try:
            customerID = manager.fetchID(customer)
            test = manager.UpdateCustomer(customer, customerID)
        except Exception as e:
            print(e)
        if test:
            failure.grid_remove() #removes from screen
            success.grid(columnspan=2, row=12, padx=5, pady=5)  #adds to screen 
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
            failure.grid(columnspan=2, row=12, padx=5, pady=5) 

    def clear_text(text):
        text.delete(0, tk.END)

    def closeWindow(self):
        cashierHome.deiconify()
        window.destroy()

    button.bind("<Button-1>", update) #connects function handle_click to button 
    button2.bind("<Button-1>", load)
    back.bind("<Button-1>", closeWindow)
    
    

#window.mainloop() #constant loop for gui 
