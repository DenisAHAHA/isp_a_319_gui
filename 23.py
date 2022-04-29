from tkinter import *

root = Tk()
e1 = Entry(width=50)

b1 = Button(text="Красный", width=9, height=3)
b2 = Button(text="Оранжевый", width=9, height=3)
b3 = Button(text="Желтый", width=9, height=3)
b4 = Button(text="Зеленый", width=9, height=3)
b5 = Button(text="Голубой", width=9, height=3)
l1 = Label(text="", width=10, height=0, font="Arial 12")

def change():
    b1 ['text'] = ""
    b1 ['bg'] = '#ff0000'
    b1 ['activebackground'] = '#ff0000'
    b1 ['fg'] = '#000000'
    b1 ['activeforeground'] = '#000000'
    e1.delete(0, END)
    e1.insert(0, "#ffaaaa")
    l1['text'] = "Красный"

def change1():
    b2 ['text'] = ""
    b2 ['bg'] = '#ff7d00'
    b2 ['activebackground'] = '#ff7d00'
    b2 ['fg'] = '#000000'
    b2 ['activeforeground'] = '#000000'
    e1.delete(0, END)
    e1.insert(0, "#ff7d00")
    l1['text'] = "Оранжевый"

def change2():
    b3 ['text'] = ""
    b3 ['bg'] = '#ffff00'
    b3 ['activebackground'] = '#ffff00'
    b3 ['fg'] = '#000000'
    b3 ['activeforeground'] = '#000000'
    e1.delete(0, END)
    e1.insert(0, "#ffff00")
    l1['text'] = "Желтый"

def change3():
    b4 ['text'] = ""
    b4 ['bg'] = '#00ff00'
    b4 ['activebackground'] = '#00ff00'
    b4 ['fg'] = '#000000'
    b4 ['activeforeground'] = '#000000'
    e1.delete(0, END)
    e1.insert(0, "#00ff00")
    l1['text'] = "Зеленый"

def change4():
    b5 ['text'] = ""
    b5 ['bg'] = '#007dff'
    b5 ['activebackground'] = '#007dff'
    b5 ['fg'] = '#000000'
    b5 ['activeforeground'] = '#000000'
    e1.delete(0, END)
    e1.insert(0, "#007dff")
    l1['text'] = "Голубой"


b1.config(command=change)
b2.config(command=change1)
b3.config(command=change2)
b4.config(command=change3)
b5.config(command=change4)
l1.config(bd=10)

l1.pack(side=TOP)
e1.pack(side=TOP)
b1.pack(side=LEFT, padx=6, pady=4)
b2.pack(side=LEFT, padx=6, pady=4)
b3.pack(side=LEFT, padx=6, pady=4)
b4.pack(side=LEFT, padx=6, pady=4)
b5.pack(side=LEFT, padx=6, pady=4)
root.mainloop()