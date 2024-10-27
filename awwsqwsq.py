import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Student Management System")

# Set window size and background color
root.geometry("400x700")
root.configure(bg="#f0f0f0")  # Light grey background for the window

# Header frame for the university logo or text (you can replace this with an image if needed)
header_frame = tk.Frame(root, bg="#2c2c44")  # Dark navy background color for header
header_frame.pack(fill='x')

# University labels (replace these with image if desired)
tk.Label(header_frame, text="BATH SPA\nUNIVERSITY", font=("Arial", 10, "bold"), fg="white", bg="#2c2c44", padx=10).pack(side='left')
tk.Label(header_frame, text="RAK\nCAMPUS", font=("Arial", 10, "bold"), fg="white", bg="#2c2c44", padx=20).pack(side='right')

# Add a frame for the entire form
frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
frame.pack(pady=20)

# Title labels
tk.Label(frame, text="Student Management System", font=("Arial", 14, "bold"), bg="#f0f0f0").pack()
tk.Label(frame, text="New Student Registration", font=("Arial", 12), bg="#f0f0f0").pack(pady=(10, 20))

# Student Name field
tk.Label(frame, text="Student Name", bg="#f0f0f0").pack(anchor='w')
entry_name = tk.Entry(frame, width=30, bg="#e0e0e0")  # Grey background for entries
entry_name.pack(pady=5)

# Mobile Number field
tk.Label(frame, text="Mobile Number", bg="#f0f0f0").pack(anchor='w')
entry_mobile = tk.Entry(frame, width=30, bg="#e0e0e0")
entry_mobile.pack(pady=5)

# Email Id field
tk.Label(frame, text="Email Id", bg="#f0f0f0").pack(anchor='w')
entry_email = tk.Entry(frame, width=30, bg="#e0e0e0")
entry_email.pack(pady=5)

# Home Address field
tk.Label(frame, text="Home Address", bg="#f0f0f0").pack(anchor='w')
entry_address = tk.Entry(frame, width=30, bg="#e0e0e0")
entry_address.pack(pady=5)

# Gender dropdown menu
tk.Label(frame, text="Gender", bg="#f0f0f0").pack(anchor='w')
gender_combobox = ttk.Combobox(frame, values=["Male", "Female", "Other"])
gender_combobox.pack(pady=5)

# Course Enrolled radio buttons
tk.Label(frame, text="Course Enrolled", bg="#f0f0f0").pack(anchor='w')
course_var = tk.StringVar()
tk.Radiobutton(frame, text="BSc CC", variable=course_var, value="BSc CC", bg="#f0f0f0").pack(anchor='w')
tk.Radiobutton(frame, text="BSc CY", variable=course_var, value="BSc CY", bg="#f0f0f0").pack(anchor='w')
tk.Radiobutton(frame, text="BSc PSY", variable=course_var, value="BSc PSY", bg="#f0f0f0").pack(anchor='w')
tk.Radiobutton(frame, text="BA & BM", variable=course_var, value="BA & BM", bg="#f0f0f0").pack(anchor='w')

# Languages known checkboxes
tk.Label(frame, text="Languages known", bg="#f0f0f0").pack(anchor='w')
lang1 = tk.BooleanVar()
lang2 = tk.BooleanVar()
lang3 = tk.BooleanVar()
tk.Checkbutton(frame, text="English", variable=lang1, bg="#f0f0f0").pack(anchor='w')
tk.Checkbutton(frame, text="Tagalog", variable=lang2, bg="#f0f0f0").pack(anchor='w')
tk.Checkbutton(frame, text="Hindi/Urdu", variable=lang3, bg="#f0f0f0").pack(anchor='w')

# Rate your English communication skills slider
tk.Label(frame, text="Rate your English communication skills", bg="#f0f0f0").pack(anchor='w')
english_skill_var = tk.IntVar()  # Variable to store slider value
scale = tk.Scale(frame, from_=0, to=10, orient='horizontal', variable=english_skill_var, bg="#f0f0f0")
scale.pack(fill='x', pady=5)


# Submit and Clear buttons
button_frame = tk.Frame(frame, bg="#f0f0f0")
button_frame.pack(pady=10)

submit_button = tk.Button(button_frame, text="Submit", bg="#2c2c44", fg="white", width=15)
submit_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", bg="#2c2c44", fg="white", width=15)
clear_button.grid(row=0, column=1, padx=5)



# Run the main event loop
root.mainloop()
