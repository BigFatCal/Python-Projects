# This is a racing game made up with the names of me and my friend group
# each colour is the colour each of us use in among us

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
num_players = int(screen.numinput("Player Count", "How many players??"))

for x in range(num_players):
    player = screen.textinput("Name", "Who is player "+str(x)+"?")
    colour = screen.textinput("Colour", "What colour do you want to be, {}?".format(player))
    colours.append(colour.lower)


is_race_on = False

user_bet = screen.textinput("Betty Betty Bet Bet", "Who you backing?")
if user_bet not in names:
    user_bet = screen.textinput("Pick a valid name!", "Who you got?:")

y_coors = []
seperation = (250/num_players)*2
for x in range(num_players):
    y_coors.append(125-seperation)


for x in range(1,num_players+1):

    fresh_turtle = Turtle()
    fresh_turtle.speed(0)
    fresh_turtle.pu()
    fresh_turtle.hideturtle()
    fresh_turtle.goto(-490, y_coors[x]-12)
    fresh_turtle.write(names[x],font=("Arial",16))

all_turtles = []
for x in range(1,num_players+1):

    fresh_turtle = Turtle(shape="turtle")
    fresh_turtle.pu()
    fresh_turtle.fillcolor(colours[x])
    fresh_turtle.pencolor(colours[x])
    fresh_turtle.goto(-400, y_coors[x])
    all_turtles.append(fresh_turtle)

turtle_names = {}
for x in range(1,num_players+1):
    turtle_names[all_turtles[x]] = names[x]

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

your_bet = Turtle()
your_bet.hideturtle()
your_bet.pu()
your_bet.goto(-20, 145)
your_bet.pd()
your_bet.write("Your bet: "+user_bet)



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
                turtle.forward(random.randint(0,15))


new_turtle = Turtle()
new_turtle.hideturtle()

if user_bet == turtle_names[winner]:
    
    new_turtle.pu()
    new_turtle.goto(-200,-15)
    new_turtle.pd()
    new_turtle.write("You win! 10 points to griffyndor!", font=("Arial",20))

else:

    new_turtle.pu()
    new_turtle.goto(-200,-15)
    new_turtle.pd()
    new_turtle.write("HAHAHAHAHA YOU IDIOT YOU LOST", font=("Arial",20))



screen.exitonclick()

#### FIX SO YOU CAN HAVE ANY NUMBER OF PEOPLE, HAVE A RANDOM COLOUR AND WORK ACCORDINGLY