# This is my first project working with a GUI, so forgive it being pretty basic!


from turtle import Turtle, Screen
from random import randint

me_as_turtle = Turtle()
me_as_turtle.shape("turtle")

def set_random_colour():

    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    
    return (r,g,b)

def draw_triangle():

    me_as_turtle.pencolor(set_random_colour())
    for x in range(0,3):
        me_as_turtle.forward(100)
        me_as_turtle.left(120)

def draw_square():

    me_as_turtle.pencolor(set_random_colour())
    for x in range(0,4):
        me_as_turtle.forward(100)
        me_as_turtle.left(90)

def draw_pentagon():

    me_as_turtle.pencolor(set_random_colour())
    for x in range(0,5):
        me_as_turtle.forward(100)
        me_as_turtle.left(72)

def draw_hexagon():

    me_as_turtle.pencolor(set_random_colour())
    for x in range(0,6):
        me_as_turtle.forward(100)
        me_as_turtle.left(60)

def draw_heptagon():

    me_as_turtle.pencolor(set_random_colour())
    for x in range(0,7):
        me_as_turtle.forward(100)
        me_as_turtle.left(51.43)

def draw_octagon():

    me_as_turtle.pencolor(set_random_colour())
    for x in range(0,8):
        me_as_turtle.forward(100)
        me_as_turtle.left(45)

def draw_nonagon():

    me_as_turtle.pencolor(set_random_colour())
    for x in range(0,9):
        me_as_turtle.forward(100)
        me_as_turtle.left(40)

def draw_decagon():

    me_as_turtle.pencolor(set_random_colour())
    for x in range(0,10):
        me_as_turtle.forward(100)
        me_as_turtle.left(36)

def dashed_line():

    for x in range(0,21):
        me_as_turtle.pd()
        me_as_turtle.forward(5)
        me_as_turtle.pu()
        me_as_turtle.forward(5)

def set_start():

    me_as_turtle.pu()
    me_as_turtle.setx(-50)
    me_as_turtle.sety(-150)
    me_as_turtle.pd()

screen = Screen()
screen.colormode(255)
screen.title("Yeeeeeeeeeeehaw!")
set_start()
draw_triangle()
draw_square()
draw_pentagon()
draw_hexagon()
draw_heptagon()
draw_octagon()
draw_nonagon()
draw_decagon()

#keep this at the bottom
screen.exitonclick()