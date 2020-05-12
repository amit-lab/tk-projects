from tkinter import *
root = Tk()
root.title('Scientific Calculator')

menu = Menu(root)

def getNum():
    global first_num
    first_num = int(myInput.get())
    myInput.delete(0, END)

def onClick(num):
    current = myInput.get()
    myInput.delete(0, END)
    myInput.insert(0, current + str(num))

def add():
    getNum()
    global math
    math = '+'

def sub():
    getNum()
    global math
    math = '-'

def mul():
    getNum()
    global math
    math = '*'

def div():
    getNum()
    global math
    math = '/'

def equalTo():
    sec_num = int(myInput.get())
    myInput.delete(0, END)
    if math == '+':
        myInput.insert(0, first_num + sec_num)
    elif math == '-':
        myInput.insert(0, first_num - sec_num)
    elif math == '*':
        myInput.insert(0, first_num * sec_num)
    elif math == '/':
        myInput.insert(0, first_num / sec_num)

def clearInput():
    myInput.delete(0, END)


# Creating button widget
# Input Box
myInput = Entry(root, width=40, borderwidth=5)
myInput.grid(row=0, column=0, columnspan=3, pady=10)

# buttons
buttons_0 = Button(root, text=0, padx=40, pady=40, command=lambda: onClick(0))
buttons_1 = Button(root, text=1, padx=40, pady=40, command=lambda: onClick(1))
buttons_2 = Button(root, text=2, padx=40, pady=40, command=lambda: onClick(2))
buttons_3 = Button(root, text=3, padx=40, pady=40, command=lambda: onClick(3))
buttons_4 = Button(root, text=4, padx=40, pady=40, command=lambda: onClick(4))
buttons_5 = Button(root, text=5, padx=40, pady=40, command=lambda: onClick(5))
buttons_6 = Button(root, text=6, padx=40, pady=40, command=lambda: onClick(6))
buttons_7 = Button(root, text=7, padx=40, pady=40, command=lambda: onClick(7))
buttons_8 = Button(root, text=8, padx=40, pady=40, command=lambda: onClick(8))
buttons_9 = Button(root, text=9, padx=40, pady=40, command=lambda: onClick(9))
# Operator buttons
plusButton = Button(root, text='+', padx=40, pady=40, command=add)
minusButton = Button(root, text='-', padx=40, pady=40, command=sub)
mulButton = Button(root, text='*', padx=40, pady=40, command=mul)
divButton = Button(root, text='/', padx=40, pady=40, command=div)
clearButton = Button(root, text='Clear', padx=140, pady=40, command=clearInput)
equalButton = Button(root, text='=', padx=40, pady=40, command=equalTo)

# Setting grid for each button
clearButton.grid(row=6, column=0, columnspan=3)

mulButton.grid(row=5, column=0)
minusButton.grid(row=5, column=1)
divButton.grid(row=5, column=2)


buttons_0.grid(row=4, column=0)
plusButton.grid(row=4, column=1)
equalButton.grid(row=4, column=2)

buttons_1.grid(row=3, column=0)
buttons_2.grid(row=3, column=1)
buttons_3.grid(row=3, column=2)

buttons_4.grid(row=2, column=0)
buttons_5.grid(row=2, column=1)
buttons_6.grid(row=2, column=2)

buttons_7.grid(row=1, column=0)
buttons_8.grid(row=1, column=1)
buttons_9.grid(row=1, column=2)


mainloop()