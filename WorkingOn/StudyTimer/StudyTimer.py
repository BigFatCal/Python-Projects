# I am studying everyday and often burn out! 
# My usual attention span is around 40 minutes.
# I will do 3x40mins of work with 5minute breaks inbetween 
# After these blocks I will either set it to choose to 'end studying' or to take a 20min break and start again
from tkinter import *
import timer

window = Tk()
# Please ignore how crude this white space is - i'm just trying to get the title to sit in the middle
window.title("STUDY OR NEVER REACH YOUR FULL POTENTIAL")
window.minsize(600, 400)
# window.config(padx=600, pady=200)

canvas = Canvas(width=600, height=400, bg="#DDFFBC")
canvas.create_text(300,200,text="00:00", font=("Courier", 30, "bold"))
canvas.pack()

STUDY_LEN = 40
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15


# This should always be at the end of the program!
# Listens to what the user is doing with the screen
window.mainloop()