from tkinter import *
from tkinter import filedialog

# Create the main window
main = Tk()
main.title("Reading Text File in GUI window")
main.geometry("600x700")
main['bg'] = 'lightblue'

# Define the global variable for the string
global num_string

# Function to open and read the file
def openFile():
    with open("num.txt") as file_handler:
        lines = file_handler.readlines()
        num_string = ''
        for each_line in lines:
            num_string += each_line.rstrip() + ' '
            # adds each line of digits to num_string and removes the newline character from each line
            # adds space after each number
    print(num_string) #prints num_string
    txtarea.insert(END, num_string)
    print(len(num_string)) #prints length of string
    txtarea.insert(END, f"\nThe length of the string is {len(num_string)}")

# Create a heading label and center it
heading = Label(main, text="To Read from the file into the textarea below,\nclick the button:", 
                font=('Roboto', 16), fg="black", bg="lightblue")
heading.pack(pady=20)

# Create text area to display the file contents
txtarea = Text(main)
txtarea.pack(pady=20, padx=20)

# Create a button to open the file and center it
Button(
    main, 
    text="Open File", 
    command=openFile
).pack(pady=20)

# Run the main event loop
main.mainloop()
