# Creating the snake game!

from turtle import *
import time
from random import randint

# Setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snakey Snakey Snake Snake")
screen.tracer(0)


# Creating a snake class that will create & control our snake
# Start coors and move distance are constants
START_COORS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:


    def __init__(self):
        self.all_turtles = []
        # creates a snake upon initialising 
        self.create_snake()
        # sets the head of the snake to the first 'turtle' in the snake body
        self.head = self.all_turtles[0]

    def create_snake(self):

        for pos in START_COORS:

            turtle = Turtle()
            turtle.pu()
            turtle.color("white")
            turtle.shape("square")
            turtle.turtlesize(1,1,1)
            turtle.goto(pos)
            self.all_turtles.append(turtle)
            screen.update()
    
    def move(self):

        for x in range(len(self.all_turtles)-1, 0, -1):

            # rather than moving all the sections of the snake, we just move
            # each snake to the position the snake before it is in
            # then we just move the first snake
            new_x = self.all_turtles[x-1].xcor()
            new_y = self.all_turtles[x-1].ycor()
            self.all_turtles[x].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def stop_moving(self):
        self.head.forward(0)

    # creating all the movements, using set heading rather than left() or right()
    def up(self):
        self.head.setheading(90)
    
    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    # adding a segment, this will be called when the snake eats an egg
    def add_segment(self):

        turtle = Turtle()
        turtle.pu()
        turtle.color("white")
        turtle.shape("square")
        turtle.turtlesize(1,1,0)
        turtle.goto(self.all_turtles[-1].xcor(), self.all_turtles[-1].ycor())
        self.all_turtles.append(turtle)
        screen.update()


# creating the eggs class, inheriting from the Turtle class first for better functionality
# max and min values set as constants to keep within screen.
MAX_VAL = 280
MIN_VAL = -280
class Eggs(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("red")    
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(MIN_VAL, MAX_VAL), randint(MIN_VAL, MAX_VAL))

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.pu()
        self.sety(275)
        self.pencolor("white")
        self.write(f"Score: {str(self.score)}", align="center", font=("Arial", 10, "normal"))

    def add_point(self):
        self.score += 1
        self.write(f"Score: {str(self.score)}", align="center", font=("Arial", 10, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score



def game_over(score):

    oops = Turtle()
    oops.hideturtle()
    oops.pu()
    oops.sety(250)
    oops.pencolor("white")
    oops.write("HAHAHAH YOU SUCK", align="center", font=("Arial", 24, "normal"))
    
    loser = Turtle()
    loser.hideturtle()
    loser.pu()
    loser.sety(-270)
    loser.pencolor("white")
    loser.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))

# Starting the game!

snake = Snake()
eggo = Eggs()
score_board = Score()

user_input = screen.textinput("Ready?", "Welcome to snakey snakey snake snake\nPress any key then Enter to play!")

if user_input:
    game_on = True

while game_on:

        # binding each snake.method to a key
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.update()
    time.sleep(0.1)
    snake.move()

        # detect collision with egg
    if snake.head.distance(eggo) < 20:
        eggo.refresh()
        snake.add_segment()
        score_board.clear()
        score_board.add_point()


        # initial border detection, this may be changed
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:

        game_on = False

    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:

        game_on = False

        # detect heads collision with it's own tail
    for seg in snake.all_turtles[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False

score_board.clear()
game_over(score_board.score)

screen.exitonclick()


