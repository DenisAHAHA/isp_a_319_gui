from tkinter import *
from turtle import left
root = Tk()

def change():
    if var.get() == 0:
        label['text'] = '+79111111111'
    elif var.get() == 1:
        label['text'] = '+79222222222'
    elif var.get() == 2:
        label['text'] = '+79333333333'

var=IntVar()
var.set(0)
r1 = Radiobutton(text = 'Петя', variable=var,command=change, value=0, indicatoron=0, height=2, width=5)
r2 = Radiobutton(text = 'Вася', variable=var,command=change, value=1, indicatoron=0, width=5, height=2)
r3 = Radiobutton(text = 'Артем', variable=var, value=2,command=change, indicatoron=0, width=5, height=2)
label = Label(width=20, height=10)

label.pack(side=RIGHT)
r1.pack()
r2.pack()
r3.pack()


root.mainloop()