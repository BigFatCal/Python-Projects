# This scripts allows you to add players, add their colours then race!

import random
from turtle import Screen, Turtle, color, pencolor, penup
import turtle

screen = Screen()
screen.colormode(255)
screen.bgcolor("lightgrey")
screen.setup(1000, 350)
screen.title("Why U Go So Fast")


colours = []
names = []
num_players = int(screen.numinput("Player Count", "How many players?? (max 6)"))
y_coors = 125

all_turtles = []
for x in range(1,num_players+1):

    # creating player turtle
    player = screen.textinput("Name", "Who is player "+str(x)+"?")
    names.append(player)
    colour = screen.textinput("Colour", "What colour do you want to be, {}?".format(player))
    fresh_turtle = Turtle(shape="turtle")
    fresh_turtle.pu()
    fresh_turtle.fillcolor(colour.lower())
    fresh_turtle.pencolor(colour.lower())
    fresh_turtle.goto(-400, y_coors)
    all_turtles.append(fresh_turtle)
    # creating turtle to write players name
    writing_turtle = Turtle()
    writing_turtle.hideturtle()
    writing_turtle.pu()
    writing_turtle.goto(-475, y_coors-8)
    writing_turtle.pd()
    writing_turtle.write("{}".format(player), font=("Arial",12))
    
    y_coors -= 50

    


turtle_names = {k:v for k,v in zip(all_turtles, names)}

is_race_on = False

user_bet = screen.textinput("Yeet", "Are you ready?")

finish_line = Turtle()
finish_line.hideturtle()
finish_line.pu()
finish_line.goto(438, 145)
finish_line.pd()
finish_line.write("Finish!")
finish_line.pu()
finish_line.goto(450, 140)
finish_line.right(90)
finish_line.pd()
finish_line.forward(280)

if user_bet:
    is_race_on = True
    
winner = 0
while is_race_on:

        for turtle in all_turtles:

            if turtle.xcor() >= 450:
                is_race_on = False
                winner = turtle

            else:
                turtle.pd()
                turtle.forward(random.randint(0,10))



new_turtle = Turtle()
new_turtle.hideturtle()
new_turtle.pu()
new_turtle.goto(-75,-15)
new_turtle.pd()
new_turtle.write("{} won!".format(turtle_names[winner]), font=("Arial",20))




screen.exitonclick()

#### UPDATE TO FIX SPACING, SPEED & CREATE A GIF POP UP AT THE END
#### EXCEPTION AND ERROR HANDLING FOR COLOURS AND NUM OF PLAYERS