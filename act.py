import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

def submit_form():
    messagebox.showinfo("Submitted", "Form has been submitted!")

# Main window
root = tk.Tk()
root.title("Bath Spa University Management System")
root.configure(bg="lightgrey")  # Set background color to grey

# Image load and resize
logo_image = Image.open("BSULOGO.png")  
logo_image = logo_image.resize((389, 114))
logo_photo = ImageTk.PhotoImage(logo_image)

# Label to hold the image
logo_label = tk.Label(root, image=logo_photo, bg="lightgrey")
logo_label.pack(side="top")

# Title
title_label = tk.Label(root, text="Student Management System", font=("Arial", 14, "bold"), bg="lightgrey")
title_label.pack(pady=5)

# Subtitle
subtitle_label = tk.Label(root, text="New Student Registration", font=("Arial", 10, "bold"), bg="lightgrey")
subtitle_label.pack(pady=5)

# Form Frame
form_frame = tk.Frame(root, bg="lightgrey")
form_frame.pack(pady=5, padx=5)

# Input Fields with Grid Layout
fields = ["Student Name", "Mobile Number", "Email Id", "Home Address"]
entries = {}
for i, field in enumerate(fields):
    tk.Label(form_frame, text=field, font=("Arial", 8), bg="lightgrey").grid(row=i, column=0, sticky="w", padx=2, pady=2)
    entry = tk.Entry(form_frame, font=("Arial", 8, "bold"))
    entry.grid(row=i, column=1, padx=5, pady=2, sticky="ew")
    entries[field] = entry

# Dropdown Menu for Gender
tk.Label(form_frame, text="Gender", font=("Arial", 8), bg="lightgrey").grid(row=len(fields), column=0, sticky="w", padx=2, pady=2)
gender = ttk.Combobox(form_frame, values=["Male", "Female", "Other"], font=("Arial", 8))
gender.grid(row=len(fields), column=1, padx=5, pady=2, sticky="ew")

# Radio Buttons for Course Enrolled
tk.Label(form_frame, text="Course Enrolled", font=("Arial", 8), bg="lightgrey").grid(row=len(fields)+1, column=0, sticky="w", padx=2, pady=2)
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
course_var = tk.StringVar()
for i, course in enumerate(courses):
    tk.Radiobutton(form_frame, text=course, variable=course_var, value=course, font=("Arial", 8), bg="lightgrey").grid(row=len(fields)+1+i, column=1, sticky="w")

# Checkboxes for Languages Known
tk.Label(form_frame, text="Languages Known", font=("Arial", 8), bg="lightgrey").grid(row=len(fields)+len(courses)+1, column=0, sticky="w", padx=2, pady=2)
languages = ["English", "Tagalog", "Hindi/Urdu"]
language_vars = {}
for i, language in enumerate(languages):
    var = tk.IntVar()
    tk.Checkbutton(form_frame, text=language, variable=var, font=("Arial", 8), bg="lightgrey").grid(row=len(fields)+len(courses)+1+i, column=1, sticky="w")
    language_vars[language] = var

# Slider to Rate English Communication Skills
slider_frame = tk.Frame(form_frame, bg="lightgrey")
slider_frame.grid(row=len(fields)+len(courses)+len(languages)+1, column=0, columnspan=2, pady=10)  # Center by spanning across both columns

tk.Label(slider_frame, text="Rate English Communication Skills", font=("Arial", 8), bg="lightgrey").pack(anchor="center")
slider = tk.Scale(slider_frame, from_=0, to=10, orient=tk.HORIZONTAL, font=("Arial", 8), bg="lightgrey", troughcolor="blue", length=300)  # Set the slider width here
slider.pack(anchor="center", padx=10, pady=2)


# Buttons
button_frame = tk.Frame(root, bg="lightgrey")
button_frame.pack(pady=5)
submit_button = tk.Button(button_frame, text="Submit", command=submit_form, font=("Arial", 8))
submit_button.pack(side="left", padx=5)
clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 8))
clear_button.pack(side="right", padx=5)

# Run the application
root.mainloop()
