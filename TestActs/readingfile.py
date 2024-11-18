from tkinter import *

# Initialize the main window
root = Tk()
root.geometry("300x450")
root.config(bg="beige")

# Define the openFile function
def openFile():
    # Ensure that the Text area is empty
    txtarea.delete("1.0", "end")

    # Open the file readexample.txt and display its contents
    try:
        with open('rak.txt') as file_handler:
            for contents in file_handler:
                txtarea.insert(END, contents)
    except FileNotFoundError:
        txtarea.insert(END, "File not found.")

# Create a text area to read contents from the file
txtarea = Text(root)
txtarea.place(x=20, y=40, height=125, width=200)

# Create a button to open the file
Button(
    root,
    text="Open File",
    command=openFile
).place(x=20, y=200, height=25, width=200)

# Add a Scrollbar(vertical)
scrollV=Scrollbar( orient='vertical') 
scrollV.place(x=220,y=40,height=125)

scrollV.config(command=txtarea.yview)
txtarea.config(yscrollcommand=scrollV.set)

root.mainloop()