
from tkinter import * 
from tkinter import messagebox

def Calculate(input):
    num1 = float(e1.get())
    num2 = float(e2.get())
    if input ==1:
        result = num1 + num2
        s = f'The sum of two numbers is: {result}'
    elif input ==2:
        result = num1 - num2
        s = f'The sub of two numbers is: {result}'
    elif input ==3:
        result = num1 * num2
        s = f'The product of two numbers is: {result}'
    elif input ==4:
        result = num1 / num2
        s = f'The quotient of two numbers is: {result}'    
    l2.configure(text=s)
    messagebox.showinfo("Result",s)

root = Tk()
root.title('Tkinter_Program')
root.geometry('400x400')
root.config(bg='#234567')

l1 = Label(root, text = "Enter Values",
bg='#234567',fg="white",font=("tahoma",12))
l1.place(x=10, y=20)

e1 = Entry(root,font=("tahoma",12))
e1.place(x=10, y=60)
e2 = Entry(root,font=("tahoma",12))
e2.place(x=200, y=60)

l2 = Label(root, text = "",
bg='#234567',fg="white",font=("tahoma",12))
l2.place(x=10, y=200)

b1 = Button(root, text = "Sum", fg="yellow", bg="#001111"
,font=("tahoma",12), command=lambda:Calculate(1))
b1.place(x=60,y=100)

b2 = Button(root, text = "Sub", fg="yellow", bg="#001111"
,font=("tahoma",12), command=lambda:Calculate(2))
b2.place(x=200,y=100)

b3 = Button(root, text = "Multiply", fg="yellow", bg="#001111"
,font=("tahoma",12), command=lambda:Calculate(3))
b3.place(x=60,y=150)

b4 = Button(root, text = "Divide", fg="yellow", bg="#001111"
,font=("tahoma",12), command=lambda:Calculate(4))
b4.place(x=200,y=150)
root.mainloop()

     
