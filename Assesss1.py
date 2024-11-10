from tkinter import *
import random

# Initialize the main application window
root = Tk()
root.title("Quiz Game - Exercise 1")
root.geometry("1280x720")
root.resizable(False, False)

# Global variables
score = 0
question_count = 0
difficulty = 1
first_attempt = True
num1, num2, operation, correct_answer = None, None, None, None



# Functions

def displayDiff():
    title_frame.pack_forget()
    menu_frame.pack()

def displayMenu():
    global difficulty
    menu_frame.pack_forget()
    difficulty = int(difficulty_var.get())
    startQuiz()

def randomInt():
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(['+', '-'])

def generateProblem():
    global num1, num2, operation, correct_answer
    num1, num2 = randomInt(), randomInt()
    operation = decideOperation()
    correct_answer = num1 + num2 if operation == '+' else num1 - num2
    displayProblem()

def displayProblem():
    question_label.config(text=f"{num1} {operation} {num2} = ")
    answer_entry.delete(0, END)

def checkAnswer():
    global score, first_attempt, question_count
    user_answer = int(answer_entry.get())
    
    if user_answer == correct_answer:
        score += 10 if first_attempt else 5
        result_label.config(text="Correct!", fg="green")
        question_count += 1
        first_attempt = True
        if question_count < 10:
            generateProblem()
        else:
            displayResults()
    else:
        result_label.config(text="Incorrect. Try again." if first_attempt else "Incorrect. Moving to next question.", fg="red")
        first_attempt = not first_attempt
        if not first_attempt:
            question_count += 1
            if question_count < 10:
                generateProblem()
            else:
                displayResults()

def displayResults():
    quiz_frame.pack_forget()
    score_label.config(text=f"Final Score: {score}/100")
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
    result_frame.pack()

def resetQuiz():
    global score, question_count, first_attempt
    score = 0
    question_count = 0
    first_attempt = True
    result_frame.pack_forget()
    menu_frame.pack()

def startQuiz():
    menu_frame.pack_forget()
    generateProblem()
    quiz_frame.pack()

# Frames
title_frame = Frame(root)
menu_frame = Frame(root)
quiz_frame = Frame(root)
result_frame = Frame(root)

Label(title_frame, text="Welcome to Raf's Math Quiz!", font=("Arial", 48)).pack(pady=100, anchor=CENTER)
Label(title_frame, text="Click 'START' to Begin!", font=("Arial", 32)).pack(pady=50, anchor=CENTER)
Button(title_frame, text="START", command=displayDiff, height=50, width=25, font=("Arial", 24), bg="red").pack(pady=100, anchor=CENTER)
title_frame.pack()

# Menu frame
difficulty_var = IntVar(value=1)
Label(menu_frame, text="Choose Difficulty Level", font=("Arial", 24)).pack(pady=50)
Radiobutton(menu_frame, text="Easy (1-digit)", variable=difficulty_var, value=1, font=("Arial", 18)).pack(anchor="w", pady=20)
Radiobutton(menu_frame, text="Moderate (2-digit)", variable=difficulty_var, value=2, font=("Arial", 18)).pack(anchor="w", pady=20)
Radiobutton(menu_frame, text="Advanced (4-digit)", variable=difficulty_var, value=3, font=("Arial", 18)).pack(anchor="w", pady=20)
Button(menu_frame, text="START QUIZ", command=displayMenu, height=2, width=25, font=("Arial", 24), bg="red").pack(pady=100, anchor=CENTER)
title_frame.pack()

# Quiz frame
question_label = Label(quiz_frame, text="", font=("Arial", 32))
question_label.pack(pady=50)
answer_entry = Entry(quiz_frame, font=("Arial", 32), bg="grey")
answer_entry.pack(pady=50)
submit_button = Button(quiz_frame, text="Submit", command=lambda: checkAnswer(), height=2, width=25, font=("Arial", 24), bg="red")
submit_button.pack(pady=50)
result_label = Label(quiz_frame, text="", font=("Arial", 32))
result_label.pack()

# Result frame
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
