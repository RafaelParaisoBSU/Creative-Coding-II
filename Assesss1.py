from tkinter import *
import random

# Initialize the main application window
root = Tk()
root.title("Quiz Game - Exercise 1")
root.geometry("1280x720")
root.resizable(False, False)

# Global variables for game state
score = 0                 # Player's score
question_count = 0        # Number of questions answered
difficulty = 1            # Game difficulty level
first_attempt = True      # Tracks if it's the player's first attempt at a question
num1, num2, operation, correct_answer = None, None, None, None  # Variables for the math problem

# Function to display difficulty selection menu
def displayDiff():
    title_frame.pack_forget()  # Hide the title screen
    menu_frame.pack()          # Show the difficulty selection menu

# Function to set the selected difficulty level and start the quiz
def displayMenu():
    global difficulty
    menu_frame.pack_forget()               # Hide the menu screen
    difficulty = int(difficulty_var.get())  # Update difficulty based on user selection
    startQuiz()                            # Start the quiz

# Function to generate random integer based on difficulty level
def randomInt():
    if difficulty == 1:
        return random.randint(1, 9)         # Easy: 1-digit numbers
    elif difficulty == 2:
        return random.randint(10, 99)       # Moderate: 2-digit numbers
    else:
        return random.randint(1000, 9999)   # Advanced: 4-digit numbers

# Function to randomly decide the math operation
def decideOperation():
    return random.choice(['+', '-'])  # Randomly choose between addition and subtraction

# Function to generate a new math problem based on the selected difficulty
def generateProblem():
    global num1, num2, operation, correct_answer
    num1, num2 = randomInt(), randomInt()         # Generate random numbers
    operation = decideOperation()                 # Determine operation
    correct_answer = num1 + num2 if operation == '+' else num1 - num2  # Calculate correct answer
    displayProblem()                              # Display the problem

# Function to display the current problem in the quiz frame
def displayProblem():
    question_label.config(text=f"{num1} {operation} {num2} = ")  # Update the question label
    answer_entry.delete(0, END)                                  # Clear the answer entry field

# Function to check the user's answer
def checkAnswer():
    global score, first_attempt, question_count
    user_answer = int(answer_entry.get())  # Get the answer entered by the user
    
    # Check if the answer is correct
    if user_answer == correct_answer:
        score += 10 if first_attempt else 5  # Full points on first attempt, half on second
        result_label.config(text="Correct!", fg="green")  # Display feedback for correct answer
        question_count += 1                             # Increment question count
        first_attempt = True                            # Reset first attempt flag
        if question_count < 10:
            generateProblem()                           # Generate a new question
        else:
            displayResults()                            # Show results if 10 questions answered
    else:
        # Display feedback for incorrect answer
        result_label.config(text="Incorrect. Try again." if first_attempt else "Incorrect. Moving to next question.", fg="red")
        first_attempt = not first_attempt  # Toggle first attempt flag
        if not first_attempt:
            question_count += 1
            if question_count < 10:
                generateProblem()          # Move to next question after second attempt
            else:
                displayResults()           # Show results if 10 questions answered

# Function to display final results and grading
def displayResults():
    quiz_frame.pack_forget()                   # Hide quiz frame
    score_label.config(text=f"Final Score: {score}/100")  # Display the final score
    # Determine the grade based on the score
    if score > 90:
        grade_label.config(text="Grade: A+")
    elif score > 80:
        grade_label.config(text="Grade: A")
    elif score > 70:
        grade_label.config(text="Grade: B")
    elif score > 60:
        grade_label.config(text="Grade: C")
    else:
        grade_label.config(text="Grade: F")
    result_frame.pack()                        # Show the result frame

# Function to reset the quiz
def resetQuiz():
    global score, question_count, first_attempt
    score = 0                # Reset score
    question_count = 0       # Reset question count
    first_attempt = True     # Reset first attempt flag
    result_frame.pack_forget()  # Hide the result frame
    title_frame.pack()           # Display the title to start again

# Function to start the quiz by displaying the first question
def startQuiz():
    menu_frame.pack_forget()  # Hide menu screen
    generateProblem()         # Generate the first question
    quiz_frame.pack()         # Show quiz frame

# Frames for different parts of the app
title_frame = Frame(root)     # Title screen frame
menu_frame = Frame(root)      # Difficulty selection frame
quiz_frame = Frame(root)      # Quiz frame where questions are displayed
result_frame = Frame(root)    # Result frame to display final score and grade

# Title frame widgets
Label(title_frame, text="Welcome to Raf's Math Quiz!", font=("Arial", 48)).pack(pady=100, anchor=CENTER)
Label(title_frame, text="Click 'START' to Begin!", font=("Arial", 32)).pack(pady=50, anchor=CENTER)
Button(title_frame, text="START", command=displayDiff, height=50, width=25, font=("Arial", 24), bg="red").pack(pady=100, anchor=CENTER)
title_frame.pack()

# Menu frame widgets for difficulty selection
difficulty_var = IntVar(value=1)
Label(menu_frame, text="Choose Difficulty Level", font=("Arial", 24)).pack(pady=50)
Radiobutton(menu_frame, text="Easy (1-digit)", variable=difficulty_var, value=1, font=("Arial", 18)).pack(anchor="w", pady=20)
Radiobutton(menu_frame, text="Moderate (2-digit)", variable=difficulty_var, value=2, font=("Arial", 18)).pack(anchor="w", pady=20)
Radiobutton(menu_frame, text="Advanced (4-digit)", variable=difficulty_var, value=3, font=("Arial", 18)).pack(anchor="w", pady=20)
Button(menu_frame, text="START QUIZ", command=displayMenu, height=2, width=25, font=("Arial", 24), bg="red").pack(pady=100, anchor=CENTER)
title_frame.pack()

# Quiz frame widgets for question display and answer entry
question_label = Label(quiz_frame, text="", font=("Arial", 32))
question_label.pack(pady=50)
answer_entry = Entry(quiz_frame, font=("Arial", 32), bg="grey")
answer_entry.pack(pady=50)
submit_button = Button(quiz_frame, text="Submit", command=lambda: checkAnswer(), height=2, width=25, font=("Arial", 24), bg="red")
submit_button.pack(pady=50)
result_label = Label(quiz_frame, text="", font=("Arial", 32))
result_label.pack()

# Result frame widgets for final score and grading
score_label = Label(result_frame, text="", font=("Arial", 32))
score_label.pack(pady=50)
grade_label = Label(result_frame, text="", font=("Arial", 18))
grade_label.pack(pady=25)
retry_button = Button(result_frame, text="Play Again", command=resetQuiz, height=2, width=25, font=("Arial", 24), bg="red")
retry_button.pack(pady=20)

# Display the menu frame initially
menu_frame.pack()

# Run the application
root.mainloop()
