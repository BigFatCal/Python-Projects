# This script pops out a GUI with a Turtle that walks in random directions 50 times
# I may expand this into a drinking game i.e if the turtle ends in top right, drink x times


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


# takes in a number of steps and creates a random path for that many steps
# each step has a random colour
def random_walk(steps):

    for x in range(steps):
        random_num = randint(1,4)
        me_as_turtle.pencolor(set_random_colour())
        if random_num == 1: 
            me_as_turtle.left(straight)
            me_as_turtle.forward(20)
        
        elif random_num == 2: 
            me_as_turtle.left(right)
            me_as_turtle.forward(20)

        elif random_num == 3: 
            me_as_turtle.left(back)
            me_as_turtle.forward(20)

        elif random_num == 4: 
            me_as_turtle.left(left)
            me_as_turtle.forward(20)

screen.title("Disco Turtle")
random_walk(50)


# keep at the bottom of the code
screen.exitonclick()