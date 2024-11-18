# Import Module
from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title('Student Management System')
main.geometry('350x600')
main.resizable(0, 0)
main.iconbitmap('logo1.ico') # To change Tkinter logo on top right

#insert image
img = ImageTk.PhotoImage(Image.open("BSULOGO.png"))
imgLabel = Label(main, image=img)
imgLabel.place(x=0,y=0)

label_frame = Frame(main, bg='white')
label_frame.place(x=0, y=115, height=125, width=350)
#Create a label

# Placing the components in the label frame
Name = Label(label_frame, text=" Student \n Management\n System", font=('Roboto',25), 
             bg= '#FFFFFF', fg='#22263d')
Name.place(relx=0.5, rely=0.5, anchor=CENTER)

# Placing the components in the iamge frame

#inserting image
image_frame = Frame(main, bg='red')
image_frame.place(x=0, y=240, height=400, width=350)

pic1 = Image.open("image2.png") # open image
pic2 = pic1.resize((350,500)) # Resize the iamge as per required size
img2 = ImageTk.PhotoImage(pic2) # Create image label
imgLabel2 = Label(image_frame, image=img2)
imgLabel2.place(x=0, y=0)

#inserting button on image
button = Button(image_frame,
    text="Click Here",
    width=25, # Set the width value to 25
    height=2, # Set the height value to 3
    bg="#22263d",  # Set the background color to cyan
    fg="#FFFFFF",  # Set the text color to white
    font=('Roboto',12)
).place(x=60, y=280,)

main.mainloop()