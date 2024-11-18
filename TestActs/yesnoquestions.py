#import tkinter module and messagebox
from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
# Set the output window
root = Tk()
root.title('Working with message box')
root.geometry('400x400')
root.config(bg='#234567')
   

def clickHere():
    # To display the message on information message box
    messagebox.showinfo("Successful", "You clicked button 1")

def Click():
    # To retrieve the value selected from message box
    answer = messagebox.askyesno("Question", "Continue?")
    if answer:
        l1.configure(text="You selected Yes")
    else:
        l1.configure(text="You selected No")
        
#Create a button1 
b1 = Button(root, text = "show Info", fg="yellow", bg="#001111"
,font=("tahoma",12),command = clickHere)
b1.place(x=30, y=20)

#Create a button2 
b2 = Button(root, text = "Yes or No", fg="yellow", bg="#001111"
,font=("tahoma",12),command = Click)
b2.place(x=30, y=70)

#Create a label to display result
l1 = Label(root, text = "  ",bg='#234567',fg="white",font=("tahoma",12))
l1.place(x=10, y=100)

root.mainloop()
