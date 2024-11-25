import tkinter as tk
import customtkinter
from PIL import Image, ImageTk, ImageSequence
import random
import os

# Create the main application window
root = customtkinter.CTk()
root.title("Quiz Game - Exercise 1")
root.geometry("1440x900")
root.resizable(False, False)

# Initialize global variables
score = 0
question_count = 0
difficulty = 1
first_attempt = True
num1, num2, operation, correct_answer = None, None, None, None

# Variable for selected difficulty
difficulty_var = tk.IntVar(value=1)

def startQuiz():
    global difficulty, score, question_count, first_attempt
    # Reset quiz parameters and start the quiz
    score = 0
    question_count = 0
    first_attempt = True
    difficulty = difficulty_var.get()
    generateProblem()
    quiz_frame.pack(fill=tk.BOTH, expand=True)

def randomInt():
    # Generate a random integer based on the selected difficulty
    if difficulty == 1:
        return random.randint(1, 9)       # Easy: 1-digit numbers
    elif difficulty == 2:
        return random.randint(10, 99)     # Intermediate: 2-digit numbers
    else:
        return random.randint(1000, 9999) # Hard: 4-digit numbers

def decideOperation():
    # Randomly select an operation (addition or subtraction)
    return random.choice(['+', '-'])

def generateProblem():
    global num1, num2, operation, correct_answer, first_attempt, question_count
    # Generate a new math problem
    if question_count >= 10:
        showResults()
        return
    first_attempt = True
    num1, num2 = randomInt(), randomInt()
    operation = decideOperation()
    # Calculate the correct answer
    correct_answer = num1 + num2 if operation == '+' else num1 - num2
    question_count_label.configure(text=f"Question {question_count + 1} of 10")
    displayProblem()

def displayProblem():
    # Display the current problem to the user
    question_label.configure(text=f"{num1} {operation} {num2} = ")
    answer_entry.delete(0, tk.END)
    answer_entry.focus()
    if question_count == 0:
        quiz_back_button.pack()
    else:
        quiz_back_button.pack_forget()

def checkAnswer(event=None):
    global score, question_count, first_attempt
    # Check the user's answer
    user_answer = answer_entry.get().strip()
    answer_entry.delete(0, tk.END)
    if user_answer == str(correct_answer):
        # Correct answer
        score_increment = 10 if first_attempt else 5
        score += score_increment
        score_label.configure(text=f"Score: {score}")
        feedback_label.configure(text="Correct!", text_color="white", fg_color="green")
        feedback_label.pack(pady=(5, 0))
        # Proceed to next question after a short delay
        quiz_frame.after(1250, lambda: [feedback_label.pack_forget(), nextQuestion()])
    else:
        # Incorrect answer
        if first_attempt:
            first_attempt = False
            feedback_label.configure(text="Incorrect! Try again.", text_color="white", fg_color="red")
            feedback_label.pack(pady=(5, 0))
        else:
            feedback_label.configure(text=f"Incorrect! The correct answer was {correct_answer}.", text_color="red", fg_color="red")
            feedback_label.pack(pady=(5, 0))
            # Proceed to next question after a short delay
            quiz_frame.after(1250, lambda: [feedback_label.pack_forget(), nextQuestion()])

def nextQuestion():
    global question_count, first_attempt
    # Move to the next question
    question_count += 1
    first_attempt = True
    if question_count >= 10:
        showResults()
    else:
        generateProblem()
        feedback_label.pack_forget()

def showResults():
    # Display the final results screen
    quiz_frame.pack_forget()
    results_frame.pack(fill=tk.BOTH, expand=True)
    ranking = calculateRanking()
    results_label.configure(text=f"Your Score: {score}\nRanking: {ranking}")

def calculateRanking():
    # Calculate the ranking based on the final score
    if score >= 95:
        return "A+"
    elif score >= 85:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def resource_path(relative_path):
    # Get the absolute path to the resource file
    return os.path.join("Task 1 - Math Quiz", relative_path)

# Load images
image_path = resource_path("titlebg.gif")
background_image = Image.open(image_path)

menu_bg_image = customtkinter.CTkImage(
    Image.open(resource_path("descbg.png")),
    size=(1440, 900)
)

quiz_bg_img = customtkinter.CTkImage(
    Image.open(resource_path("descbg.png")),
    size=(1440, 900)
)

def update_frame():
    global frame_index
    # Update the frame for animation
    frame_index = (frame_index + 1) % frame_count
    titlebg.configure(image=frames[frame_index])
    root.after(14, update_frame)

# Prepare frames for animation
frames = []
for frame in ImageSequence.Iterator(background_image):
    frame = frame.convert("RGBA")
    frames.append(ImageTk.PhotoImage(frame))
frame_count = len(frames)

# Create frames for different screens
# Each screen is a frame that will contain the widgets for that part of the application
title_frame = customtkinter.CTkFrame(root)     # Title screen frame
menu_frame = customtkinter.CTkFrame(root)      # Menu screen frame
diff_frame = customtkinter.CTkFrame(root)      # Difficulty selection screen frame
quiz_frame = customtkinter.CTkFrame(root)      # Quiz screen frame
results_frame = customtkinter.CTkFrame(root)   # Results screen frame

frame_index = 0

# Set up the title screen
# This screen displays the animated background and a play button
titlebg = customtkinter.CTkLabel(
    title_frame,
    text="",
    image=frames[0],     # Start with the first frame of the animation
    width=1440,
    height=900
)
titlebg.place(x=0, y=0)

title_start = customtkinter.CTkButton(
    title_frame,
    text="PLAY",
    font=("League Gothic", 104),
    width=400,
    height=150,
    fg_color='green',
    hover_color='darkgreen',
    command=lambda: [title_frame.pack_forget(), menu_frame.pack(fill=tk.BOTH, expand=True)],
    cursor="hand2"
)
title_start.pack(side=tk.BOTTOM, pady=130)
title_frame.pack(fill=tk.BOTH, expand=True)

# Set up the menu screen
# This screen provides instructions on how to play the quiz
menubg = customtkinter.CTkLabel(
    menu_frame,
    text="",
    image=menu_bg_image,
    width=1440,
    height=900
)
menubg.place(x=0, y=0)

menu_header = customtkinter.CTkLabel(
    menu_frame,
    text="How to Play:",
    fg_color="#5a825d",
    font=("Montserrat", 72, 'bold')
)
menu_header.pack(side=tk.TOP, pady=(150,5))

menu_text = customtkinter.CTkLabel(
    menu_frame,
    text=(
        "This Quiz has 10 questions to solve. Each question is worth 10 points. "
        "If you get an answer wrong, you get another attempt worth 5 points."
        "You can choose between 3 difficulties:\n\n"
        "Easy (1-digit questions)\n\n"
        "Intermediate (2-digit questions)\n\n"
        "Hard (4-digit questions)"
    ),
    fg_color="#5a825d",
    font=('Poppins', 24),
    wraplength=1200,
)
menu_text.pack()

menu_back = customtkinter.CTkButton(
    menu_frame,
    text="BACK",
    font=('League Gothic', 48),
    width=400,
    height=100,
    fg_color='red',
    hover_color='maroon',
    cursor="hand2",
    command=lambda: [menu_frame.pack_forget(), title_frame.pack(fill=tk.BOTH, expand=True)]
)
menu_back.pack(side='left', padx=50, pady=(125,50))

menu_next = customtkinter.CTkButton(
    menu_frame,
    text="NEXT",
    font=('League Gothic', 48),
    width=400,
    height=100,
    cursor="hand2",
    command=lambda: [menu_frame.pack_forget(), diff_frame.pack(fill=tk.BOTH, expand=True)]
)
menu_next.pack(side='right', padx=50, pady=(125,50))

# Set up the difficulty selection screen
# This screen allows the user to select the difficulty level
diffbg = customtkinter.CTkLabel(
    diff_frame,
    text="",
    image=menu_bg_image,
    width=1440,
    height=900
)
diffbg.place(x=0, y=0)

diff_header = customtkinter.CTkLabel(
    diff_frame,
    text="Choose a Difficulty:",
    fg_color="#5a825d",
    font=("Montserrat", 72, 'bold')
)
diff_header.pack(side=tk.TOP, pady=(150,50))

# Difficulty options
difficulty_options = [
    ("Easy (1-digit)", 1),
    ("Intermediate (2-digit)", 2),
    ("Hard (4-digit)", 3)
]

# Create radiobuttons for difficulty selection
for text, value in difficulty_options:
    rb = customtkinter.CTkRadioButton(
        diff_frame,
        text=text,
        variable=difficulty_var,
        value=value,
        font=('Poppins', 32,'bold'),
        bg_color="#5a825d",
        cursor="hand2"
    )
    rb.pack(anchor=tk.CENTER, pady=(50,0))

diff_back = customtkinter.CTkButton(
    diff_frame,
    text="BACK",
    font=('League Gothic', 48),
    width=400,
    height=100,
    fg_color='red',
    hover_color='maroon',
    cursor="hand2",
    command=lambda: [diff_frame.pack_forget(), menu_frame.pack(fill=tk.BOTH, expand=True)]
)
diff_back.pack(side='left', padx=50, pady=(100,50))

diff_next = customtkinter.CTkButton(
    diff_frame,
    text="START QUIZ",
    font=('League Gothic', 48),
    width=400,
    height=100,
    fg_color='green',
    hover_color='darkgreen',
    cursor="hand2",
    command=lambda: [diff_frame.pack_forget(), startQuiz()]
)
diff_next.pack(side='right', padx=50, pady=(100,50))

# Set up the quiz screen
# This screen displays the quiz questions and handles user input
quizbg = customtkinter.CTkLabel(
    quiz_frame,
    text="",
    image=quiz_bg_img,
    width=1440,
    height=900
)
quizbg.place(x=0, y=0)

score_label = customtkinter.CTkLabel(
    quiz_frame,
    text="Score: 0",
    fg_color="#5a825d",
    font=('Montserrat', 64, 'bold')
)
score_label.pack(pady=(130,0))

question_count_label = customtkinter.CTkLabel(
    quiz_frame,
    text="Question 1 of 10",
    fg_color="#5a825d",
    font=('Poppins', 48, 'bold')
)
question_count_label.pack(pady=(5))

question_label = customtkinter.CTkLabel(
    quiz_frame,
    fg_color="#5a825d",
    font=('Poppins', 72, 'bold')
)
question_label.pack()

# Entry for user's answer
answer_entry = customtkinter.CTkEntry(
    quiz_frame,
    width=500,
    height=100,
    font=('Montserrat', 36)
)
answer_entry.pack(pady=(10, 0))
answer_entry.bind("<Return>", checkAnswer)

# Feedback label to display messages to the user
feedback_label = customtkinter.CTkLabel(
    quiz_frame,
    width=500,
    height=100,
    font=('Poppins', 48)
)
feedback_label.pack(pady=(5, 0))
feedback_label.pack_forget()

submit_button = customtkinter.CTkButton(
    quiz_frame,
    text="SUBMIT",
    fg_color='green',
    hover_color='darkgreen',
    font=('League Gothic', 48),
    width=400,
    height=100,
    cursor="hand2",
    command=checkAnswer
)
submit_button.pack(pady=10)

quiz_back_button = customtkinter.CTkButton(
    quiz_frame,
    text="BACK",
    fg_color='red',
    hover_color='maroon',
    font=('League Gothic', 48),
    width=400,
    height=100,
    cursor="hand2",
    command=lambda: [quiz_frame.pack_forget(), diff_frame.pack(fill=tk.BOTH, expand=True)]
)
quiz_back_button.pack(pady=(0, 10))

# Set up the results screen
# This screen displays the user's final score and ranking
resultsbg = customtkinter.CTkLabel(
    results_frame,
    text="",
    image=quiz_bg_img,
    width=1440,
    height=900
)
resultsbg.place(x=0, y=0)

results_label = customtkinter.CTkLabel(
    results_frame,
    text="Your Score: 0\nRanking: F",
    font=('Montserrat', 72, 'bold'),
    fg_color='green'
)
results_label.pack(pady=(150, 50))

play_again_button = customtkinter.CTkButton(
    results_frame,
    text="PLAY AGAIN?",
    font=('League Gothic', 64),
    width=500,
    height=150,
    fg_color='green',
    hover_color='darkgreen',
    cursor="hand2",
    command=lambda: [results_frame.pack_forget(), diff_frame.pack(fill=tk.BOTH, expand=True)]
)
play_again_button.pack(side='left', padx=50, pady=50)

exit_button = customtkinter.CTkButton(
    results_frame,
    text="EXIT",
    font=('League Gothic', 64),
    width=500,
    height=150,
    fg_color='red',
    hover_color='maroon',
    cursor="hand2",
    command=lambda: [results_frame.pack_forget(), menu_frame.pack(fill=tk.BOTH, expand=True)]
)
exit_button.pack(side='right', padx=50, pady=50)

# Start the animation for the title screen
# This function updates the frame of the GIF to create the animation effect
update_frame()

# Start the main application loop
root.mainloop()