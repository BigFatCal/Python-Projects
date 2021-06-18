# This is my first project working with a GUI, so forgive it being pretty basic!


from turtle import Turtle, Screen
from random import randint

me_as_turtle = Turtle()
me_as_turtle.shape("turtle")

screen = Screen()
screen.colormode(255)


# setting a random colour for every shape
def set_random_colour():

    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    
    return (r,g,b)

# function to draw each shape
def draw_shape(num_of_sides):

    angle = 360/num_of_sides
    for x in range(num_of_sides):
        me_as_turtle.forward(100) 
        me_as_turtle.left(angle)

# function to get the shape in the range that we want
def get_shapes():

    for x in range(3,11):
        me_as_turtle.pencolor(set_random_colour())
        draw_shape(x) 

# setting the start in a reasonable place
def set_start():

    me_as_turtle.pu()
    me_as_turtle.setx(-50)
    me_as_turtle.sety(-150)
    me_as_turtle.pd()

# running it!
screen.title("Yeeeeeeeeeeehaw!")
set_start()
get_shapes()

#keep this at the bottom
screen.exitonclick()