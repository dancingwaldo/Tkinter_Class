from tkinter import *

# Create the Root Widget
root = Tk()

# Create Label Widgets, with text
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Batman")

# Add to the Root Widget using the grid() method
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)

# Create an event loop
root.mainloop()
