from tkinter import *
from PIL import Image, ImageTk, ImageFont

# Initialize root window
root = Tk()
root.title("Tkinter App with Background")
root.geometry("600x400")  # Set your desired window size

# Function to raise frames
def switch_frame(frame):
    frame.tkraise()

# Create frames for home and task screens
home_frame = Frame(root)
home_frame.place(relwidth=1, relheight=1)

# Load the background image for home_frame
bg_image_home = Image.open("TestActs/Homepage.png")  # Replace with your image file
bg_image_home = bg_image_home.resize((600, 400))  # Resize image to window size
bg_photo_home = ImageTk.PhotoImage(bg_image_home)

# Create a Label widget to hold the image in the home_frame
bg_label_home = Label(home_frame, image=bg_photo_home)
bg_label_home.place(relwidth=1, relheight=1)

# Continue button in home_frame
Continue_button = Button(
    home_frame,
    text="Continue",
    compound="center",
    bg="white",
    font=("Hobo Regular", 15),
    fg="#022c5e",
    borderwidth=0,
    activebackground="white",
    activeforeground="#022c5e",
    command=lambda: switch_frame(task_frame))
Continue_button.place(x=470, y=340)

task_frame = Frame(root)
task_frame.place(relwidth=1, relheight=1)

# Load the background image for task_frame
bg_image_task = Image.open("TestActs\TaskPage.png")  # Replace with your image file
bg_image_task = bg_image_task.resize((600, 400))  # Resize image to window size
bg_photo_task = ImageTk.PhotoImage(bg_image_task)

# Create a Label widget to hold the image in the task_frame
bg_label_task = Label(task_frame, image=bg_photo_task)
bg_label_task.place(relwidth=1, relheight=1)

# Back Button in task_frame
back_button = Button(
    task_frame,
    text="Go To Home",
    bg="white",
    font=("Hobo Regular", 15),
    fg="#022c5e",
    borderwidth=0,
    activebackground="white",
    activeforeground="#022c5e",
    command=lambda: switch_frame(home_frame))
back_button.place(x=270, y=350)

# Raise the home_frame first
switch_frame(home_frame)

root.mainloop()