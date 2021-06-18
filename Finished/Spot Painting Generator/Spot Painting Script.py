# This program takes an image as an imput, recognises all of the prominant colours within that 
# image, then returns a spot painting using these colours!
# Just change the directory path for your image to change the output
# Hopefully can develop this into a web app where you can just upload an image and it'll happen

from turtle import Turtle, Screen, color, forward, pencolor
from random import randint
import colorgram    

# extracting 10 colours from the image
colours = colorgram.extract(r'C:\Users\calmc\OneDrive\Desktop\Portfolio Projects\Python Projects\Finished\Spot Painting Generator\hirst.jpeg',10)
# putting their RBG values in a list
rgb_values = []
for i in range(len(colours)):
    rgb_values.append(colours[i].rgb)
    
me_as_turtle = Turtle()
screen = Screen()
screen.colormode(255)

def set_start():

    screen.screensize(250,250)
    me_as_turtle.hideturtle()
    me_as_turtle.pu()
    me_as_turtle.setx(-250)
    me_as_turtle.sety(210)
    
# painting a row with random colours
def paint():

    count = 0
    while count < 6:
            random_num = randint(0,9)
            me_as_turtle.dot(50, rgb_values[random_num])
            me_as_turtle.forward(100)
            count += 1

# dropping a level so painting doesn't carry on off the window
def drop_level():

    me_as_turtle.setx(-250)
    me_as_turtle.sety(me_as_turtle.ycor() - 100)

# let it commence!
screen.title("Here is some mega valuable art")
set_start()
for x in range(5):
    paint()
    drop_level()


# keep at the bottom of the code
screen.exitonclick()