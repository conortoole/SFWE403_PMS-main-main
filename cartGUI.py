from tkinter import Frame
import customtkinter as tk
from models.Medicine import Medicine
from models.Staff import Cashier
import checkoutGui as cg

# Selecting GUI theme - dark, light , system (for system default) 
tk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
tk.set_default_color_theme("blue") 

cashier = Cashier()
medicine = Medicine()

window = tk.CTk()
table = Frame(window)
window.geometry("500x500") 
window.title("Add to Cart") 

window.columnconfigure(0, weight = 0)
window.columnconfigure(1, weight = 0)
window.columnconfigure(2, weight = 0)
window.columnconfigure(3, weight = 0)
window.rowconfigure(0, weight = 0)
window.rowconfigure(1, weight = 0)
window.rowconfigure(2, weight = 0)
window.rowconfigure(3, weight = 0)
window.rowconfigure(4, weight = 0)
window.rowconfigure(5, weight = 0)

# frame = tk.CTkFrame(master=window) 
# frame.pack(pady=20,padx=40,fill='both',expand=True) 

button = tk.CTkButton(
    master=window,
    text="Add to Cart",
    width=150,
    height=50,
    # bg="blue",
    # fg="yellow",
)

back = tk.CTkButton(
    master=window,
    text="Go Back",
    width=150,
    height=50,
    # bg="blue",
    # fg="yellow",
)

checkOutB = tk.CTkButton(
    master=window,
    text="Check Out",
    width=150,
    height=50,
    # bg="blue",
    # fg="yellow",
)

# labels are text
label = tk.CTkLabel(master=window,text="Shopping Cart", font=("Fira Code", 25)) 
label1 = tk.CTkLabel(master=window,text="Name") 
label2 = tk.CTkLabel(master=window,text="Quantity") 
# the cart headers
nameL = tk.CTkLabel(master=window,text="name") 
quantityL = tk.CTkLabel(master=window,text="quantity") 
strengthL = tk.CTkLabel(master=window,text="strength") 
priceL = tk.CTkLabel(master=window,text="price") 

success = tk.CTkLabel(master=window,text="Successfully Added!")  
failure = tk.CTkLabel(master=window,text="Failed to Add!") 
#These are the input fields
nameIn = tk.CTkEntry(master=window, width=300)
quantityIn = tk.CTkEntry(master=window, width=300)


#this adds inputs to window
label.grid(columnspan=4, row=0, padx=1, pady=1)
label1.grid(column=0, row=4, padx=5, pady=5)
nameIn.grid(column=1, columnspan=3, row=4, padx=5, pady=5) 
label2.grid(column=0, row=5, padx=5, pady=5)
quantityIn.grid(column=1, columnspan=3, row=5, padx=5, pady=5) 

button.grid(column = 1, columnspan=2, row=7, padx=5, pady=5)
back.grid(column = 0, row=7, padx=5, pady=5)
checkOutB.grid(column = 3, columnspan=2, row=7, padx=5, pady=5)

def handle_click(event): 
    # this gets info from input and puts into class
    medicine.name = nameIn.get()
    medicine.quantity = quantityIn.get()
    try:
        item = cashier.fetchItem(medicine.name)
        newMed = loadMedicine(item, medicine)
    
        cashier.addCart(newMed) 
        items = cashier.fetchCart()

        nameL.grid(column=0, row=1, padx=3, pady=5)
        quantityL.grid(column=1, row=1, padx=3, pady=5) 
        strengthL.grid(column=2, row=1, padx=3, pady=5)
        priceL.grid(column=3, row=1, padx=3, pady=5) 
        failure.grid_remove()
        clear_text(nameIn)
        clear_text(quantityIn)
        buildTable(items)
    except:
        clear_text(nameIn)
        clear_text(quantityIn)
        failure.grid(row = 8, columnspan = 4, pady = 4)

def clear_text(text):
   text.delete(0, tk.END)

def buildTable(items):
    count = 0
    for row in items:
        #row is of type medicine
        temp = tk.CTkLabel(master=window, text="{}".format(row.name))
        temp.grid(row = 2 + count, column = 0)

        temp1 = tk.CTkEntry(master=window, width=100)
        temp1.insert(0, row.quantity)
        temp1.grid(row = 2 + count, column = 1)

        temp2 = tk.CTkLabel(master=window, text="{}".format(row.strength))
        #temp2.insert(0, row.strength)
        temp2.grid(row = 2 + count, column = 2)

        temp3 = tk.CTkLabel(master=window, text="${}".format(row.price))
        #temp3.insert(0, row.price)
        temp3.grid(row = 2 + count, column = 3)
        count = count + 1

def loadMedicine(item, medicine):
    newMedicine = Medicine()
    newMedicine.name = medicine.name
    newMedicine.quantity = medicine.quantity
    newMedicine.expDate = item[5]
    newMedicine.strength = item[3] 
    newMedicine.batch = item[4] 
    newMedicine.price = item[6] 
    return newMedicine

def checkOut(event):
    total = cashier.calculateTotal()
    cg.open_checkoutView(window, total)
    window.withdraw()
    


button.bind("<Button-1>", handle_click) #connects function handle_click to button 
checkOutB.bind("<Button-1>", checkOut)

window.mainloop() #constant loop for gui 