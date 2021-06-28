from tkinter import *
import math
import pandas as pd
from datetime import datetime

# Setting the constants!
BG_COLOUR = "#CEE5D0"
# I may change these in the future, or add the functionaility to change these (maybe when it's a web app)
STUDY_LEN = 40 * 60
SHORT_BREAK = 8 * 60
LONG_BREAK = 20 * 60

window = Tk()
# Please ignore how crude this white space is - i'm just trying to get the title to sit in the middle
window.title("STUDY OR NEVER REACH YOUR FULL POTENTIAL")
window.minsize(600, 400)
window.config(bg=BG_COLOUR)


# Timer
header = Label(text="Timer", font=("Courier", 30, 'bold'))
header.config(bg=BG_COLOUR, fg="#0A1931")
header.place(y=95, x=240)

# Paused
paused = Label(text="PAUSED", font=("Courier", 20, 'bold'))
paused.config(bg=BG_COLOUR, fg=BG_COLOUR)
paused.place(y=10, x=15)


# Clock
clock = Label(text="00:00", font=("Courier", 60, "bold"))
clock.config(bg=BG_COLOUR, fg="#0A1931")
clock.place(y=155, x=180)

# Ticker
tick = "✔"
ticker = Label(text=tick,font=("Courier", 12, "bold"))
ticker.config(bg=BG_COLOUR, fg="#0A1931")

# Submitted label

submitted = Label (text = "Submitted!", font=("Courier", 12, "bold"))
submitted.config(bg=BG_COLOUR, fg="#0A1931")

# Creating the countdown mechanisms!
# Using the reps variable as a global variable in functions
reps = 0 
# So I can stop the clock and reset it!
timer = None
current_count = 0 
total_count = 0

file_name = r"C:\Users\calmc\OneDrive\Desktop\DevelopmentProjects\PythonProjects\WorkingOn\StudyTimer\study_tracker.csv"

def study_countdown(count):

    global reps
    global tick 
    paused.config(fg=BG_COLOUR)

    # Updating titles and ticks based on what section we're in!
    if reps % 2 == 0:
        header.config(text="Study!", fg="#0A1931")
    elif reps == 1: 
        header.config(text="Break!", fg="#FFBD9B")
        ticker.place(x=290, y=300)
    elif reps == 3: 
        header.config(text="Break!", fg="#F5A962")
        ticker.config(text=f"{tick*2}")
        ticker.place(x=285, y=300)
    elif reps == 5: 
        header.config(text="Break!", fg="#C84B31")
        ticker.config(text=f"{tick*3}")
        ticker.place(x=280, y=300)


    global timer
    global current_count
    global total_count


    current_count = count
    # Getting minutes and seconds value 
    count_minutes = math.floor(count/60)
    count_seconds = count % 60
    clock.config(text="{}:{}".format(count_minutes, count_seconds))

    if count_minutes < 10 and count_seconds < 10: 
        clock.config(text="0{}:0{}".format(count_minutes, count_seconds))
    
    elif count_minutes < 10:
        clock.config(text="0{}:{}".format(count_minutes, count_seconds))

    elif count_seconds < 10:
        clock.config(text="{}:0{}".format(count_minutes, count_seconds))

    else:
        clock.config(text="{}:{}".format(count_minutes, count_seconds))

    if count > 0:
        timer = window.after(1000, study_countdown, count-1)
        # Incrementing total count so we can add it to the study tracker at the end
        total_count += 1
    else:
        reps += 1
        # So the window pops up if its in the background/been minimised
        window.attributes('-topmost', 1)
        window.deiconify()
        # loop back to start timer 
        start_timer()

# Creating this for the button event to call
def start_timer():
    global reps

    if reps % 2 == 0 :
        study_countdown(STUDY_LEN)
    elif reps == 1 or reps == 3: 
        study_countdown(SHORT_BREAK)
    elif reps == 5:
        study_countdown(LONG_BREAK)

    play_button.place(x=700,y=600)
    pause_button.place(x=150,y=300)
    submit_session.place(x=800,y=700)
    submitted.place(x=900,y=800)

# Struggled for a while just retrying to use the study_countdown function but it kept messing up the breaks!
def continue_timer():

    paused.config(fg=BG_COLOUR)
    pause_button.place(x=150,y=300)
    play_button.place(x=700,y=600)
    submit_session.place(x=800,y=700)
    submitted.place(x=900,y=800)

    global reps
    global timer
    global current_count
    global total_count

    # Repeating the same code as in the function before - This could definitely be rewritten
    count_minutes = math.floor(current_count/60)
    count_seconds = current_count % 60
    clock.config(text="{}:{}".format(count_minutes, count_seconds))

    if count_minutes < 10 and count_seconds < 10: 
        clock.config(text="0{}:0{}".format(count_minutes, count_seconds))
    
    elif count_minutes < 10:
        clock.config(text="0{}:{}".format(count_minutes, count_seconds))

    elif count_seconds < 10:
        clock.config(text="{}:0{}".format(count_minutes, count_seconds))

    else:
        clock.config(text="{}:{}".format(count_minutes, count_seconds))

    if current_count > 0:
        timer = window.after(1000, study_countdown, current_count-1)
        total_count += 1
    else:
        reps += 1
        window.lift()
        start_timer()


# Resetting everything back to what it was!
def reset_timer():
    global timer
    global reps
    global current_count

    paused.config(fg=BG_COLOUR)
    header.config(text="Timer", fg="#0A1931")
    clock.config(text="00:00")
    ticker.config(text="")
    window.after_cancel(timer)
    reps = 0 
    current_count = 0 
    start_button.place(x=150,y=300)
    play_button.place(x=800,y=700)
    pause_button.place(x=700,y=600)
    submit_session.place(x=800,y=700)
    submitted.place(x=900,y=800)


def pause_timer():
    global timer
    
    window.after_cancel(timer)
    paused.config(fg="#C84B31")
    pause_button.place(x=700,y=600)
    play_button.place(x=151,y=300)
    submit_session.place(y=50, x=20)

# Updating the study tracker! 
def update_study_tracker():

    global total_count
    current_datetime = datetime.now()
    timestamp = current_datetime.strftime("%d-%b-%Y (%H:%M:%S)")
    total_minutes = math.floor(total_count/60)
    study_tracker = pd.read_csv(file_name)
    study_tracker = study_tracker.append({"Timestamp":timestamp, "Seconds":total_count, "Minutes":total_minutes}, ignore_index=True)
    study_tracker.to_csv(file_name, index=False)
    submitted.place(y=52, x=120)
    total_count = 0


# Start button
start_button = Button(text="Start", command=start_timer)
start_button.place(x=150,y=300)

# Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.place(x=420,y=300)

# Pause button
pause_button = Button(text="Pause", command=pause_timer)

# Play button 
play_button = Button(text="Play", command=continue_timer)

# Submit session button
submit_session = Button(text="Submit Session", command=update_study_tracker)

# This should always be at the end of the program!
# Listens to what the user is doing with the screen
window.mainloop()