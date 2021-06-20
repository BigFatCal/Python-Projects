# this is my version of the classic Etch-A-Sketch game
# this is also my first attempt at taking direct user input and returning a function

from random import randint
from turtle import Turtle, Screen, clearscreen
import turtle

cursor = Turtle()
cursor.shape("turtle")
cursor.speed(8)
screen = Screen()
screen.colormode(255)

# this allows our GUI window to 'listen' to any input we give it on the keyboard
def forwards():
    cursor.forward(10)

def backwards():
    cursor.backward(10)

def turn_right():
    cursor.right(10)

def turn_left():
    cursor.left(10)

def clear_screen():
    cursor.clear()
    cursor.reset()

def undo():
    cursor.undo()

def change_colour():

    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)

    cursor.pencolor((r,g,b))

screen.title("Etch-A-Sketch!")
screen.listen()
turtle.onkeypress(forwards, "Up")
turtle.onkeypress(backwards, "Down")
turtle.onkeypress(turn_right, "Right")
turtle.onkeypress(turn_left, "Left")
turtle.onkeypress(clear_screen, "r")
turtle.onkeypress(undo, "d")
turtle.onkeypress(change_colour, "c")



# keep at the bottom of the code
screen.exitonclick()


### UPDATE TO SAVE GAME