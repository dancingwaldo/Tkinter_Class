from tkinter import *

# Create the Root Widget
root = Tk()

# Create an Entry Widget
e = Entry(root, width = 30, bg = "black", fg = "white")
e.pack()

# get() will retrieve the string that was stored in the Entry Widget
e.get()

# Inserts default text into the text field
e.insert(0, "Enter your name: ")

def myClick():
    myLabel = Label(root, text = e.get())
    myLabel.pack()

# Create a Button Widget
# Add text and padding
myButton = Button(root, text = "Enter your name:", padx = 30, pady = 10, command = myClick)
myButton.pack()

# Create an event loop
root.mainloop()
