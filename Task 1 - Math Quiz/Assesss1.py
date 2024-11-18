import tkinter as tk              # Import tkinter for GUI creation
from tkinter import font as tkFont # Import font module from tkinter
import random                     # Import random module for generating random numbers
from PIL import Image, ImageTk    # Import Pillow modules for image handling

# Initialize the main application window
root = tk.Tk()
root.title("Quiz Game - Exercise 1")  # Set window title
root.geometry("1280x720")             # Set window size
root.resizable(False, False)          # Disable window resizing
root.configure(bg='#2E0854')          # Set background color (Dark Violet)

# Define fonts, using available system fonts
available_fonts = tkFont.families()
montserrat_font = "Montserrat" if "Montserrat" in available_fonts else "Helvetica" # Primary font
poppins_font = "Poppins" if "Poppins" in available_fonts else "Helvetica"         # Secondary font

# Load and set the background image
bg_image = Image.open("Task 1 - Math Quiz\maxresdefault.jpg") # Load image
bg_image = bg_image.resize((1280, 720), Image.Resampling.LANCZOS) # Resize image to window size
bg_photo = ImageTk.PhotoImage(bg_image) # Convert image for Tkinter

# Define color scheme for the application
COLOR_BG = '#2E0854'          # Background color (Dark Violet)
COLOR_PRIMARY = '#FFFFFF'     # Primary text color (White)
COLOR_ACCENT = '#FF8C00'      # Accent color (Dark Orange)
COLOR_SUCCESS = '#28a745'     # Success message color (Green)
COLOR_ERROR = '#dc3545'       # Error message color (Red)
COLOR_BUTTON_BG = '#1E90FF'   # Button background color (Dodger Blue)
COLOR_BUTTON_FG = '#FFFFFF'   # Button text color (White)
COLOR_TITLE = '#23663a'       # Title background color (Dark Green)

# Global variables for game state
score = 0
question_count = 0
difficulty = 1
first_attempt = True
num1, num2, operation, correct_answer = None, None, None, None

# Function to display the difficulty selection menu
def displayDiff():
    title_frame.pack_forget()      # Hides the title frame
    menu_frame.pack(pady=50)       # Shows the menu frame

# Function to return to the title screen
def backToTitle():
    menu_frame.pack_forget()       # Hides the menu frame
    title_frame.pack(fill=tk.BOTH, expand=True)  # Shows the title frame

# Function to set the selected difficulty level and start the quiz
def displayMenu():
    global difficulty
    menu_frame.pack_forget()           # Hides the menu frame
    difficulty = difficulty_var.get()  # Gets the selected difficulty
    startQuiz()                        # Starts the quiz

# Function to generate a random integer based on difficulty level
def randomInt():
    if difficulty == 1:
        return random.randint(1, 9)       # Easy difficulty: 1-digit numbers
    elif difficulty == 2:
        return random.randint(10, 99)     # Moderate difficulty: 2-digit numbers
    else:
        return random.randint(1000, 9999) # Advanced difficulty: 4-digit numbers

# Function to randomly select a math operation
def decideOperation():
    return random.choice(['+', '-'])  # Randomly chooses between addition and subtraction

# Function to generate a new math problem
def generateProblem():
    global num1, num2, operation, correct_answer
    num1, num2 = randomInt(), randomInt()   # Generates two random numbers
    operation = decideOperation()           # Decides on the operation
    # Calculates the correct answer
    correct_answer = num1 + num2 if operation == '+' else num1 - num2
    displayProblem()                        # Displays the problem

# Function to display the current problem in the quiz frame
def displayProblem():
    # Update the question label with the current problem
    question_label.config(text=f"Question {question_count + 1}: \n\n {num1} {operation} {num2} = ")
    answer_entry.delete(0, tk.END)  # Clears the answer entry field
    if question_count == 0:
        back_button.pack(pady=10)   # Shows the back button on the first question
    else:
        back_button.pack_forget()   # Hides the back button after the first question

# Function to check the user's answer
def checkAnswer(event=None):
    global score, first_attempt, question_count
    try:
        user_answer = int(answer_entry.get())  # Gets the user's input

        if user_answer == correct_answer:
            points = 10 if first_attempt else 5  # Assigns points based on attempt
            score += points                       # Updates the score
            score_display.config(text=f"Score: {score}")
            result_label.config(text="Correct!", fg=COLOR_PRIMARY, bg=COLOR_SUCCESS)
            question_count += 1
            first_attempt = True
            if question_count < 10:
                generateProblem()  # Generate the next problem
            else:
                displayResults()   # Display the final results
        else:
            if first_attempt:
                result_label.config(text="Incorrect. Try again.", bg=COLOR_ERROR, fg=COLOR_PRIMARY)
                first_attempt = False  # Allows a second attempt
            else:
                result_label.config(text="Incorrect. Moving to next question.", bg=COLOR_ERROR, fg=COLOR_PRIMARY)
                score = max(score - 5, 0)  # Deducts points for incorrect answer
                score_display.config(text=f"Score: {score}")
                question_count += 1
                first_attempt = True
                if question_count < 10:
                    generateProblem()
                else:
                    displayResults()
    except ValueError:
        # Handle non-integer inputs
        result_label.config(text="Please enter a valid number.", bg=COLOR_ERROR, fg=COLOR_PRIMARY)

# Function to display final results and grading
def displayResults():
    quiz_frame.pack_forget()  # Hide the quiz frame
    score_label.config(text=f"Final Score: {score}/100")
    # Determine grade based on the score
    if score > 90:
        grade_label.config(text="Grade: A+", fg='gold')
    elif score > 80:
        grade_label.config(text="Grade: A", fg='gold')
    elif score > 70:
        grade_label.config(text="Grade: B", fg='silver')
    elif score > 60:
        grade_label.config(text="Grade: C", fg='#CD7F32') 
    else:
        grade_label.config(text="Grade: F", fg=COLOR_ERROR)
    result_frame.pack(pady=50)  # Shows the result frame

# Function to return to the difficulty selection menu
def backToMenu():
    quiz_frame.pack_forget()  # Hides the quiz frame
    menu_frame.pack(pady=50)  # Shows the menu frame

# Function to reset the quiz and return to the title screen
def resetQuiz():
    global score, question_count, first_attempt
    score = 0
    question_count = 0
    first_attempt = True
    score_display.config(text="Score: 0")
    result_label.config(text="", bg=COLOR_BG)
    result_frame.pack_forget()                  # Hides the result frame
    title_frame.pack(fill=tk.BOTH, expand=True) # Shows the title frame

# Function to start the quiz
def startQuiz():
    generateProblem()          # Generates the first problem
    quiz_frame.pack(pady=20)   # Shows the quiz frame

# Create main frames for different screens
title_frame = tk.Frame(root, bg=COLOR_BG, highlightthickness=0)
menu_frame = tk.Frame(root, bg=COLOR_BG, highlightthickness=0)
quiz_frame = tk.Frame(root, bg=COLOR_BG, highlightthickness=0)
result_frame = tk.Frame(root, bg=COLOR_BG, highlightthickness=0)

# Create a label for the background image in the title frame
bg_label = tk.Label(title_frame, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

# Title label in the title frame
title_label = tk.Label(
    title_frame, 
    text="Welcome to Raf's Math Quiz!", 
    font=(montserrat_font, 48, 'bold'), 
    bg=COLOR_TITLE,
    fg=COLOR_PRIMARY,
    wraplength=750,
    anchor=tk.CENTER
)
title_label.pack(pady=(100))

# Instruction label in the title frame
start_label = tk.Label(
    title_frame, 
    text="Click 'START' to Begin!", 
    font=(montserrat_font, 32), 
    bg=COLOR_TITLE,
    fg=COLOR_PRIMARY,
    wraplength=750,
)
start_label.pack(pady=(0, 50))

# Start button in the title frame
start_button = tk.Button(
    title_frame, 
    text="START", 
    command=displayDiff, 
    height=2, 
    width=25, 
    font=(montserrat_font, 24, 'bold'), 
    bg=COLOR_ACCENT, 
    fg=COLOR_PRIMARY, 
    activebackground='#FFA500', 
    cursor="hand2",
    bd=0,
    relief='raised'
)
start_button.pack(pady=50)

# Pack the title frame to make it visible
title_frame.pack(fill=tk.BOTH, expand=True)

# Variable to store the selected difficulty
difficulty_var = tk.IntVar(value=1)

# Menu title label
menu_title = tk.Label(
    menu_frame, 
    text="Choose Difficulty Level", 
    font=(montserrat_font, 28, 'bold'), 
    bg=COLOR_BG, 
    fg=COLOR_PRIMARY
)
menu_title.pack(pady=(5, 10))

# Menu description label
menu_description = tk.Label(
    menu_frame, 
    text=(
        "This Quiz has 10 questions to solve. Each question is worth 10 points. "
        "You can choose between 3 difficulties: Easy (1-digit questions), "
        "Moderate (2-digit questions), and Advanced (4-digit questions). "
        "Once you get an answer wrong, you get another attempt, but it will only cost 5 points."
    ),
    font=(montserrat_font, 16),
    bg=COLOR_BG, 
    fg=COLOR_PRIMARY, 
    wraplength=1000, 
    justify=tk.LEFT
)
menu_description.pack(pady=5, padx=50)

# Difficulty options for the radiobuttons
difficulty_options = [
    ("Easy (1-digit)", 1),
    ("Moderate (2-digit)", 2),
    ("Advanced (4-digit)", 3)
]

# Create radiobuttons for difficulty selection
for text, value in difficulty_options:
    rb = tk.Radiobutton(
        menu_frame, 
        text=text, 
        variable=difficulty_var, 
        value=value, 
        font=(poppins_font, 18), 
        bg=COLOR_BG, 
        fg=COLOR_PRIMARY, 
        selectcolor=COLOR_BG,
        activebackground=COLOR_BG,
        activeforeground=COLOR_PRIMARY,
        cursor="hand2"
    )
    rb.pack(anchor="w", padx=100)

# Button to start the quiz
start_quiz_button = tk.Button(
    menu_frame, 
    text="START QUIZ", 
    command=displayMenu, 
    height=1, 
    width=20, 
    font=(poppins_font, 24, 'bold'), 
    bg='#28a745',     # Green background
    fg=COLOR_PRIMARY, 
    activebackground='#218838', 
    cursor="hand2",
    bd=0,
    relief='raised'
)
start_quiz_button.pack(pady=5)

# Button to return to the title screen
back_to_title_button = tk.Button(
    menu_frame, 
    text="Back to MENU", 
    command=backToTitle, 
    height=1, 
    width=20, 
    font=(poppins_font, 24, 'bold'), 
    bg=COLOR_BUTTON_BG, 
    fg=COLOR_PRIMARY, 
    activebackground='#218838', 
    cursor="hand2",
    bd=0,
    relief='raised'
)
back_to_title_button.pack(pady=5)

# Button to return to difficulty selection (in quiz frame)
back_button = tk.Button(
    quiz_frame, 
    text="Back", 
    command=backToMenu, 
    height=1,          
    width=15,     
    font=(poppins_font, 14, 'bold'), 
    bg=COLOR_BUTTON_BG, 
    fg=COLOR_BUTTON_FG,
    activebackground='#1C86EE',
    cursor="hand2",
    bd=0,
    relief='raised'
)

# Score display label in the quiz frame
score_display = tk.Label(
    quiz_frame, 
    text="Score: 0", 
    font=(montserrat_font, 24, 'bold'), 
    bg=COLOR_BG, 
    fg=COLOR_PRIMARY
)
score_display.pack(pady=5)

# Question label to display the problem
question_label = tk.Label(
    quiz_frame, 
    text="", 
    font=(montserrat_font, 32, 'bold'), 
    bg=COLOR_BG, 
    fg=COLOR_PRIMARY
)
question_label.pack(pady=5)

# Entry widget for user's answer
answer_entry = tk.Entry(
    quiz_frame, 
    font=(montserrat_font, 32), 
    bg="#FFFFFF", 
    fg="#000000",
    justify='center',
    bd=2,
    relief='groove'
)
answer_entry.pack(pady=20, ipady=5, ipadx=20)
answer_entry.bind('<Return>', checkAnswer)  # Binds Enter key to submit answer

# Submit button in the quiz frame
submit_button = tk.Button(
    quiz_frame, 
    text="Submit", 
    command=checkAnswer, 
    height=2, 
    width=15, 
    font=(montserrat_font, 24, 'bold'), 
    bg=COLOR_ERROR, 
    fg=COLOR_PRIMARY, 
    activebackground='#c82333', 
    cursor="hand2",
    bd=0,
    relief='raised'
)
submit_button.pack()

# Label to display result messages
result_label = tk.Label(
    quiz_frame, 
    text="", 
    font=(montserrat_font, 28, 'bold'), 
    bg=COLOR_BG, 
    fg=COLOR_PRIMARY
)
result_label.pack(pady=20)

# Label to display the final score in result frame
score_label = tk.Label(
    result_frame, 
    text="", 
    font=(montserrat_font, 32, 'bold'), 
    bg=COLOR_BG, 
    fg=COLOR_PRIMARY
)
score_label.pack(pady=(50, 20))

# Label to display the grade in result frame
grade_label = tk.Label(
    result_frame, 
    text="", 
    font=(montserrat_font, 48, 'bold'), 
    bg=COLOR_BG, 
    fg=COLOR_PRIMARY
)
grade_label.pack(pady=10)

# Button to play again (reset the quiz)
retry_button = tk.Button(
    result_frame, 
    text="Play Again", 
    command=resetQuiz, 
    height=2, 
    width=20, 
    font=(montserrat_font, 24, 'bold'), 
    bg='#dc3545',   
    fg=COLOR_PRIMARY, 
    activebackground='#bd2130', 
    cursor="hand2",
    bd=0,
    relief='raised'
)
retry_button.pack(pady=20)

# Run the application
root.mainloop()