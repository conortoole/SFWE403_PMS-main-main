import customtkinter as tk
from models.Medicine import Medicine
from models.Staff import PharmacyManager

# Selecting GUI theme - dark, light , system (for system default) 
tk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
tk.set_default_color_theme("blue") 

manager = PharmacyManager("test")
medicine = Medicine()

window = tk.CTk()
window.geometry("500x500") 
window.title("Add to Inventory") 

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
    text="Add Item",
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
label = tk.CTkLabel(master=window,text="Add Item", font=("Fira Code", 25)) 
label1 = tk.CTkLabel(master=window,text="Name") 
label2 = tk.CTkLabel(master=window,text="Quantity") 
label3 = tk.CTkLabel(master=window,text="Strength") 
label4 = tk.CTkLabel(master=window,text="Batch Number") 
label5 = tk.CTkLabel(master=window,text="Expiration (yyyy-mm-dd)") 
label6 = tk.CTkLabel(master=window,text="Price") 

success = tk.CTkLabel(master=window,text="Successfully Added!")  
failure = tk.CTkLabel(master=window,text="Failed to Add!") 
#These are the input fields
nameIn = tk.CTkEntry(master=window, width=300)
quantityIn = tk.CTkEntry(master=window, width=300)
strengthIn = tk.CTkEntry(master=window, width=300)
batchIn = tk.CTkEntry(master=window, width=300)
expIn = tk.CTkEntry(master=window, width=300)
priceIn = tk.CTkEntry(master=window, width=300)

#this adds inputs to window
label.grid(columnspan=2, row=0, padx=5, pady=5)
label1.grid(column=0, row=1, padx=5, pady=5)
nameIn.grid(column=1, row=1, padx=5, pady=5) 
label2.grid(column=0, row=2, padx=5, pady=5)
quantityIn.grid(column=1, row=2, padx=5, pady=5) 
label3.grid(column=0, row=3, padx=5, pady=5)
strengthIn.grid(column=1, row=3, padx=5, pady=5)
label4.grid(column=0, row=4, padx=5, pady=5) 
batchIn.grid(column=1, row=4, padx=5, pady=5) 
label5.grid(column=0, row=5, padx=5, pady=5)
expIn.grid(column=1, row=5, padx=5, pady=5)
label6.grid(column=0, row=6, padx=5, pady=5)
priceIn.grid(column=1, row=6, padx=5, pady=5)

button.grid(column = 1, row=7, padx=5, pady=5)
back.grid(column = 0, row=7, padx=5, pady=5)

def handle_click(event): 
    # this gets info from input and puts into class
    medicine.name = nameIn.get()
    medicine.quantity = quantityIn.get()
    medicine.strength = strengthIn.get()
    medicine.batch = batchIn.get()
    medicine.expDate = expIn.get()
    medicine.price = priceIn.get()
    #this adds the customer to database and checks if it worked
    #test = manager.createPatient(customer)
    test = manager.orderMedication(medicine);
    if test:
        failure.grid_remove() #removes from screen
        success.grid(columnspan=2, row=9, padx=5, pady=5) #adds to screen 

        #clears input fields
        clear_text(nameIn)
        clear_text(quantityIn)
        clear_text(strengthIn)
        clear_text(batchIn)
        clear_text(expIn)
        clear_text(priceIn)
    else:
        success.grid_remove()
        failure.grid(columnspan=2, row=9, padx=5, pady=5) 

def clear_text(text):
   text.delete(0, tk.END)

button.bind("<Button-1>", handle_click) #connects function handle_click to button 

window.mainloop() #constant loop for gui 