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


# For deleting entries
def deleteEntry(oid, top):
    conn = sqlite3.connect('address_book.db')
    # Creating cursor
    cur = conn.cursor()
    # Delete entry
    cur.execute(f"DELETE FROM addresses WHERE oid=={oid}")
    cur.execute("SELECT * FROM addresses")
    # Commit changes
    conn.commit()
    # Closing connection
    conn.close()
    # Distroy and recreate current window
    top.destroy()
    getEntries()

# For Updating entries
def getEntry(oid, top):
    # Creating UI
    update = Tk()
    update.title("Update Entry")
    update.geometry("500x500")
    # Creating labels for each entry
    f_name_label = Label(update, text="First Name : ")
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(update, text="Last Name : ")
    l_name_label.grid(row=1, column=0)
    address_label = Label(update, text="Address : ")
    address_label.grid(row=2, column=0)
    city_label = Label(update, text="City : ")
    city_label.grid(row=3, column=0)
    state_label = Label(update, text="State : ")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(update, text="ZipCode : ")
    zipcode_label.grid(row=5, column=0)

    # Creating Entry for each field
    f_name = Entry(update, width=50)
    f_name.grid(row=0, column=1, padx=10, pady=10)
    l_name = Entry(update, width=50)
    l_name.grid(row=1, column=1, padx=10, pady=10)
    address = Entry(update, width=50)
    address.grid(row=2, column=1, padx=10, pady=10)
    city = Entry(update, width=50)
    city.grid(row=3, column=1, padx=10, pady=10)
    state = Entry(update, width=50)
    state.grid(row=4, column=1, padx=10, pady=10)
    zipcode = Entry(update, width=50)
    zipcode.grid(row=5, column=1, padx=10, pady=10)
    # Getting older entries and set it into respective entries
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM addresses WHERE oid="+str(oid))
    record = cur.fetchall()
    conn.close()

    data = [f_name, l_name, address, city, state, zipcode]
    i = 0
    for item in record:
        for field in item:
            data[i].insert(0, field)
            i += 1

    Button(update, text="Update Entry", command=lambda: updateEntry(oid, data, top, update)).grid(row=6, column=0, columnspan=2)


def updateEntry(oid, data, top, update):
    
    # Making connection to database
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()

    # Updating databases
    cur.execute("""UPDATE addresses SET 
                 first_name = :f_name,
                 last_name = :l_name,
                 address = :add,
                 city = :city,
                 state = :state,
                 zipcode = :zip
                 
                 WHERE oid=:oid""",
                 {
                     'f_name': data[0].get(),
                     'l_name': data[1].get(),
                     'add': data[2].get(),
                     'city': data[3].get(),
                     'state': data[4].get(),
                     'zip': data[5].get(),
                     'oid': oid
                 })

    # Closing connection
    conn.commit()
    conn.close()

    # Destroing both top and update windows
    update.destroy()
    top.destroy()
    # Creating viewdata window
    getEntries()


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

# For showing entries in another window
def showEntries(records):
    top = Tk()
    top.title("Database")
    i = 0
    j = 0
    col_text = ["ID no.", "First Name", "Last Name", "Address", "City", "State", "ZipCode"]
    # Creating labels for indexes
    for i in range(len(col_text)):
        Label(top, text=col_text[i]).grid(row=0, column=i, padx=10, pady=10)
    # Creating labels for Operations
    Label(top, text="Operations").grid(row=0, column=len(col_text), padx=10, columnspan=2)
    # Showing entries
    for record in records:
        i += 1
        j = 0
        Label(top, text=record[6]).grid(row=i, column=j, padx=10)
        Button(top, text="Edit", command=lambda: getEntry(record[6], top)).grid(row=i, column=len(col_text)+1, padx=10)
        Button(top, text="Delete", command=lambda: deleteEntry(record[6], top)).grid(row=i, column=len(col_text)+2, padx=10)
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
# Submit Button
s_btn = Button(root, text="Insert Into Database", command=submit)
s_btn.grid(row=6, column=0, columnspan=2)
# Show entries button
g_btn = Button(root, text="Show Entries", command=getEntries)
g_btn.grid(row=7, column=0, columnspan=2)


# Closing connection
conn.close()

mainloop()
