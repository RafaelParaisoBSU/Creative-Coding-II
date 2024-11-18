from tkinter import *
root = Tk()

# Set the size of the main window to match the flag proportions
root.geometry("300x180")

# Top stripe (white)
topframe = Frame(root, bg='white', width=300, height=60)
topframe.pack(fill=X)

# Middle stripe (blue)
middleframe = Frame(root, bg='blue', width=300, height=60)
middleframe.pack(fill=X)

# Bottom stripe (red)
bottomframe = Frame(root, bg='red', width=300, height=60)
bottomframe.pack(fill=X)

root.mainloop()
