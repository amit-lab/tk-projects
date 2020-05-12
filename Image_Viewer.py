from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()
# Getting Image Names
PATH = "/home/amit/Pictures/"
my_imgs = []
labels = []
for imgs in os.listdir(PATH):
    current_img = os.path.join(PATH, imgs)
    img_array = Image.open(current_img)
    img_array = img_array.resize((300, 300))
    photo = ImageTk.PhotoImage(img_array)
    my_imgs.append(photo)

img_label = Label(image=my_imgs[0])
img_label.grid(row=0, column=0, columnspan=3)
def back(img_number):
    global img_label_previous
    img_label_next.grid_forget()
    createButtons(img_number)
    img_label_previous = Label(image=my_imgs[img_number])
    img_label_previous.grid(row=0, column=0, columnspan=3)


def forword(img_number):
    global img_label_next
    img_label.grid_forget()
    try:
        img_label_previous.grid_forget()
    except:
        pass
    createButtons(img_number)
    img_label_next = Label(image=my_imgs[img_number])
    img_label_next.grid(row=0, column=0, columnspan=3)

def createButtons(img_number=0):
    back_btn = Button(root, text='<<', command=lambda: back(img_number-1))
    exit_btn = Button(root, text='Exit Program', command=root.quit)
    forword_btn = Button(root, text='>>', command=lambda: forword(img_number+1))
    if img_number == len(my_imgs)-1:
        forword_btn = Button(root, text='>>', state=DISABLED)
    if img_number == 0:
        back_btn = Button(root, text='<<', state=DISABLED)
    back_btn.grid(row=1, column=0)
    exit_btn.grid(row=1, column=1)
    forword_btn.grid(row=1, column=2)


createButtons()
mainloop()