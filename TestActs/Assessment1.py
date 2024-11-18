from tkinter import *
import random

def displayDiff():
    title_frame.pack_forget()
    difficultyselect.pack()

def displayMenu():
    global difficulty
    difficultyselect.pack_forget()
    difficulty = int(var_difficulty.get())
    
root = Tk()
root.title("Quiz Game - Exercise 1")
root.geometry("1280x720")
root.resizable(False, False)

title_frame = Frame(root)
difficultyselect = Frame(root)
quiz_frame = Frame(root)
resultscreen_frame = Frame(root)

Label(title_frame, text="Welcome to Raf's Math Quiz!", font=("Arial", 48)).pack(pady=100, anchor=CENTER)
Label(title_frame, text="Click 'START' to Begin!", font=("Arial", 32)).pack(pady=50, anchor=CENTER)
Button(title_frame, text="START", command=displayDiff, height=50, width=25, font=("Arial", 24), bg="red").pack(pady=100, anchor=CENTER)
title_frame.pack()

var_difficulty = IntVar(value=1)
Label(difficultyselect, text="Select a Difficulty!", font=("Arial", 32)).pack(pady=100)
Radiobutton(difficultyselect, text="Easy (1-digit)", variable=var_difficulty, value=1, font=("Arial", 18)).pack(anchor="w")
Radiobutton(difficultyselect, text="Normal (2-digit)", variable=var_difficulty, font=("Arial", 18)).pack(anchor="w")
Radiobutton(difficultyselect, text="Hard (4-digit)", variable=var_difficulty, font=("Arial", 18)).pack(anchor="w")
Button(difficultyselect, text="START QUIZ", command=displayDiff, height=10, width=20, font=("Arial", 24), bg="red").pack(pady=100, anchor=CENTER)

question_label = Label(quiz_frame, text="", font=("Arial", 18)).pack(pady=25)


root.mainloop()
