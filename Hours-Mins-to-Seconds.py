# Importing modules
from tkinter import *

# Creating window
window = Tk()
window.title("Time Converter")
window.geometry("200x150")

# Variables to store user entered hours and minutes
hours = IntVar()
minutes = IntVar()

# This function is called when the butten is clicked
def calculate():
    s = (hours.get() * 3600) + (minutes.get() * 60)
    seconds = Label(window, text = str(s) + " Seconds")
    seconds.grid(row = 4, column = 1)

# To display the required widgets 
def display():
    hourLabel = Label(window, text = "Hours : ")
    hoursSpin = Spinbox(window, from_= 0, to = 24, textvariable = hours)

    minutesLabel = Label(window, text = "Minutes : ")
    minutesSpin = Spinbox(window, from_= 0, to = 60, textvariable = minutes)

    hourLabel.grid(row = 0, column = 0)
    hoursSpin.grid(row = 0, column = 1)

    minutesLabel.grid(row = 1, column = 0)
    minutesSpin.grid(row = 1, column = 1)

    claculateButton = Button(window, text = "Calculate", command = calculate)
    claculateButton.grid(row = 3, column = 1)

display()
window.mainloop()