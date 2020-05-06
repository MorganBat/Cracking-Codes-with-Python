# import tkinter
# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()

from tkinter import *

root = Tk()

var = StringVar()
label = Message( root, textvariable = var, relief = RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()