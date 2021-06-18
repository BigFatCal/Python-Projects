from turtle import Turtle, Screen, forward, pencolor
from random import randint

me_as_turtle = Turtle()
me_as_turtle.shape("turtle")

screen = Screen()
screen.colormode(255)

left = 90
right = 270
back = 180
straight = 0

# setting a random colour for every shape
def set_random_colour():

    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
     
    return (r,g,b)


def spirograph(num_circles):

    turn = 360/num_circles
    for x in range(num_circles):
        me_as_turtle.pencolor(set_random_colour())
        me_as_turtle.circle(100)
        me_as_turtle.right(turn)


me_as_turtle.speed(0)
screen.title("Oooooo wavey circles")
spirograph(20)

# keep at the bottom of the code
screen.exitonclick()