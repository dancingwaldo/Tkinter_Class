from tkinter import *

# Must import the Pillow library to use modern image files
# NEED TO INSTALL VIA PIP
# pip install Pillow
from PIL import ImageTk, Image


# Create the Root Widget
root = Tk()

# Change the Title of the Application
root.title('Images')

# Change the icon at the top of the window
root.iconbitmap('/Users/tk24535/Desktop/capture-one-22-icon.ico')

# Display an Image file using the Pillow module
my_img = ImageTk.PhotoImage(Image.open("/Users/tk24535/Desktop/utc-icon.png"))
my_label = Label(image = my_img)
my_label.pack()

# Create an exit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()







root.mainloop()
