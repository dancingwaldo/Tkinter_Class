from tkinter import *

# Create the Root Widget
root = Tk()

def myClick():
    myLabel = Label(root, text = "Something something")
    myLabel.pack()

# Create a Button Widget
# Add text and padding
myButton = Button(root, text = "Click Me!", padx = 30, pady = 10, command = myClick)
myButton.pack()

# Create an event loop
root.mainloop()
