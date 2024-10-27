import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

def submit_form():
    messagebox.showinfo("Submitted", "Form has been submitted!")

# Main window
root = tk.Tk()
root.title("Bath Spa University Management System")

# Image load and resize
logo_image = Image.open("BSULOGO.png")  
logo_image = logo_image.resize((300, 100))
logo_photo = ImageTk.PhotoImage(logo_image)

# Label to hold the image
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(side="top", pady=5)

# Title
title_label = tk.Label(root, text="Student Management System", font=("Arial", 14))
title_label.pack(pady=5)

# Subtitle
subtitle_label = tk.Label(root, text="New Student Registration", font=("Arial", 10))
subtitle_label.pack(pady=5)

# Form Frame
form_frame = tk.Frame(root)
form_frame.pack(pady=5, padx=5)

# Input Fields
fields = ["Student Name", "Mobile Number", "Email Id", "Home Address"]
entries = {}
for field in fields:
    tk.Label(form_frame, text=field, font=("Arial", 8)).pack(anchor="w")
    entry = tk.Entry(form_frame, font=("Arial", 8))
    entry.pack(fill="x", pady=2)
    entries[field] = entry

# Dropdown Menu for Gender
tk.Label(form_frame, text="Gender", font=("Arial", 8)).pack(anchor="w")
gender = ttk.Combobox(form_frame, values=["Male", "Female", "Other"], font=("Arial", 8))
gender.pack(fill="x", pady=2)

# Radio Buttons for Course Enrolled
tk.Label(form_frame, text="Course Enrolled", font=("Arial", 8)).pack(anchor="w")
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
course_var = tk.StringVar()
for course in courses:
    tk.Radiobutton(form_frame, text=course, variable=course_var, value=course, font=("Arial", 8)).pack(anchor="w")

# Checkboxes for Languages Known
tk.Label(form_frame, text="Languages Known", font=("Arial", 8)).pack(anchor="w")
languages = ["English", "Tagalog", "Hindi/Urdu"]
language_vars = {}
for language in languages:
    var = tk.IntVar()
    tk.Checkbutton(form_frame, text=language, variable=var, font=("Arial", 8)).pack(anchor="w")
    language_vars[language] = var

# Slider to Rate English Communication Skills
tk.Label(form_frame, text="Rate English Communication Skills", font=("Arial", 8)).pack(anchor="w")
slider = tk.Scale(form_frame, from_=0, to=10, orient=tk.HORIZONTAL, font=("Arial", 8))
slider.pack(fill="x", pady=2)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)
submit_button = tk.Button(button_frame, text="Submit", command=submit_form, font=("Arial", 8))
submit_button.pack(side="left", padx=5)
clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 8))
clear_button.pack(side="right", padx=5)

# Run the application
root.mainloop()