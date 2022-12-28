from tkinter import *

# Must import the Pillow library to use modern image files
# NEED TO INSTALL VIA PIP
# pip install Pillow
from PIL import ImageTk, Image
import os


# Create the Root Widget
root = Tk()

# Change the Title of the Application
root.title('Image Viewer')

# Change the icon at the top of the window
root.iconbitmap('/Users/tk24535/Desktop/capture-one-22-icon.ico')

# Create image variables for each image
my_img1 = ImageTk.PhotoImage(Image.open("/Users/nicholasfoerster/Dropbox/Git/Tkinter_Class/Images/gameboy_kirby.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("/Users/nicholasfoerster/Dropbox/Git/Tkinter_Class/Images/vinylrecord1.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("/Users/nicholasfoerster/Dropbox/Git/Tkinter_Class/Images/Tenable_Network_Security.png"))
my_img4 = ImageTk.PhotoImage(Image.open("/Users/nicholasfoerster/Dropbox/Git/Tkinter_Class/Images/lotta-icon.png"))

image_list = [my_img1, my_img2, my_img3, my_img4]

# Add the image(s) to the grid
my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

# Define functions for buttons
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    # Need to remove the previous image when button is clicked
    my_label.grid_forget()
    # Defining the new displayed image which is the image number + 1
    my_label = Label(image = image_list[image_number + 1])
    # Add to the grid
    my_label.grid(row = 0, column = 0, columnspan = 3)

def back():
    global my_label
    global button_forward
    global button_back
    return

# Create button variables
button_back = Button(root, text="<<", command = back)
button_exit = Button(root, text="Exit", command = root.quit)
button_forward = Button(root, text=">>", command = lambda: forward(0))

# Add buttons to the grid
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)



root.mainloop()
