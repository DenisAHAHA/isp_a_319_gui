from distutils.util import change_root
from tkinter import * 
root = Tk()

lbox = Listbox(width=15, height=8)
lbox.pack(side=LEFT)
lbox2 = Listbox(width=15, height=8)
lbox2.pack(side=RIGHT)

for i in('apple', 'bananas', 'carrot', 'bread'):
    lbox.insert(0,i)







b1 = Button(text= ">>", width= 9, height=2)
b2 = Button(text= "<<", width=9, height=2)

b1.pack()
b2.pack()

root.mainloop()