import tkinter as tk
import random

# Initialize the main application window
root = tk.Tk()
root.title("Arithmetic Quiz Game")
root.geometry("400x300")

# Global variables
score = 0
question_count = 0
difficulty = 1
first_attempt = True
num1, num2, operation, correct_answer = None, None, None, None

# Functions
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
    answer_entry.delete(0, tk.END)

def checkAnswer():
    global score, first_attempt, question_count
    user_answer = int(answer_entry.get())
    
    if user_answer == correct_answer:
        if first_attempt:
            score += 10
        else:
            score += 5
        result_label.config(text="Correct!", fg="green")
        question_count += 1
        first_attempt = True
        if question_count < 10:
            generateProblem()
        else:
            displayResults()
    else:
        if first_attempt:
            result_label.config(text="Incorrect. Try again.", fg="red")
            first_attempt = False
        else:
            result_label.config(text="Incorrect. Moving to next question.", fg="red")
            first_attempt = True
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
menu_frame = tk.Frame(root)
quiz_frame = tk.Frame(root)
result_frame = tk.Frame(root)

# Menu frame
difficulty_var = tk.IntVar(value=1)
tk.Label(menu_frame, text="Choose Difficulty Level", font=("Arial", 14)).pack(pady=10)
tk.Radiobutton(menu_frame, text="Easy (1-digit)", variable=difficulty_var, value=1).pack(anchor="w")
tk.Radiobutton(menu_frame, text="Moderate (2-digit)", variable=difficulty_var, value=2).pack(anchor="w")
tk.Radiobutton(menu_frame, text="Advanced (4-digit)", variable=difficulty_var, value=3).pack(anchor="w")
tk.Button(menu_frame, text="Start Quiz", command=displayMenu).pack(pady=20)

# Quiz frame
question_label = tk.Label(quiz_frame, text="", font=("Arial", 14))
question_label.pack(pady=10)
answer_entry = tk.Entry(quiz_frame, font=("Arial", 14))
answer_entry.pack(pady=5)
submit_button = tk.Button(quiz_frame, text="Submit", command=checkAnswer)
submit_button.pack(pady=10)
result_label = tk.Label(quiz_frame, text="", font=("Arial", 12))
result_label.pack()

# Result frame
score_label = tk.Label(result_frame, text="", font=("Arial", 14))
score_label.pack(pady=10)
grade_label = tk.Label(result_frame, text="", font=("Arial", 14))
grade_label.pack(pady=5)
retry_button = tk.Button(result_frame, text="Play Again", command=resetQuiz)
retry_button.pack(pady=20)

# Display the menu frame initially
menu_frame.pack()

# Run the application
root.mainloop()
