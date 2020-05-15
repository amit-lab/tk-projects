from tkinter import *
import sqlite3

root = Tk()
root.title('Database App')
icon = PhotoImage(file='cactus.png')
root.iconphoto(False, icon)
root.geometry("500x500")

# Setting connection
conn = sqlite3.connect('address_book.db')

# Creating cursor
cor = conn.cursor()

# Creating Table
'''
cur.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )
""")
'''

# Creating necessary functions
# For Inserting into databases
def submit():
    # Connecting to database again
    # Setting connection
    conn = sqlite3.connect('address_book.db')
    # Creating cursor
    cor = conn.cursor()
    # Inserting into databases
    cor.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",{
        'first_name': f_name.get(),
        'last_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
    })
    # Committing changes
    conn.commit()
    # Closing Database connection
    conn.close()
    # Clearing fields
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Getting entries from databases
def getEntries():
    # Connecting to Database
    conn = sqlite3.connect('address_book.db')
    # Creating cursor
    cur = conn.cursor()
    # Getting data
    cur.execute("SELECT *, oid FROM addresses")
    records = cur.fetchall()
    showEntries(records)
    # Closing Connection
    conn.close()

def showEntries(records):
    top = Toplevel()
    top.title("Database")
    etries = []
    i = 0
    j = 0
    # Creating labels for indexes
    iL1 = Label(top, text="sr. no.")
    iL1.grid(row=0, column=0, padx=10)
    iL2 = Label(top, text="First Name")
    iL2.grid(row=0, column=1)
    iL3 = Label(top, text="Last Name")
    iL3.grid(row=0, column=2)
    iL4 = Label(top, text="Address")
    iL4.grid(row=0, column=3)
    iL5 = Label(top, text="City")
    iL5.grid(row=0, column=4)
    iL6 = Label(top, text="state")
    iL6.grid(row=0, column=5)
    iL7 = Label(top, text="ZipCode")
    iL7.grid(row=0, column=6)

    for record in records:
        i += 1
        j = 0
        Label(top, text=record[6]).grid(row=i, column=j, padx=10)
        for field in range(len(record)-1):
            j += 1
            Label(top, text=record[field]).grid(row=i, column=j, padx=10)

# Creating labels for each entry
f_name_label = Label(root, text="First Name : ")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name : ")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address : ")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City : ")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State : ")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="ZipCode : ")
zipcode_label.grid(row=5, column=0)

# Creating Entry for each field
f_name = Entry(root, width=50)
f_name.grid(row=0, column=1, padx=10, pady=10)
l_name = Entry(root, width=50)
l_name.grid(row=1, column=1, padx=10, pady=10)
address = Entry(root, width=50)
address.grid(row=2, column=1, padx=10, pady=10)
city = Entry(root, width=50)
city.grid(row=3, column=1, padx=10, pady=10)
state = Entry(root, width=50)
state.grid(row=4, column=1, padx=10, pady=10)
zipcode = Entry(root, width=50)
zipcode.grid(row=5, column=1, padx=10, pady=10)

# Creating Buttons
s_btn = Button(root, text="Insert Into Database", command=submit)
s_btn.grid(row=6, column=0, columnspan=2)
g_btn = Button(root, text="Show Entries", command=getEntries)
g_btn.grid(row=7, column=0, columnspan=2)



# Closing connection
conn.close()

mainloop()