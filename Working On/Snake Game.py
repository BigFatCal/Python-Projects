# Creating the snake game!

from turtle import *
import time

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
            turtle.turtlesize(1,1,0)
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
        turtle.hideturtle()
        turtle.pu()
        turtle.color("white")
        turtle.shape("square")
        turtle.goto(self.all_turtles[-1].xcor(), self.all_turtles[-1].ycor())
        self.all_turtles.append(turtle)
        screen.update()


# Starting the game!
snake = Snake()

game_on = True

while game_on:

    # binding each snake.method to a key
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.add_segment:
        # had to hide the turtle previously so it didn't show in the middle of the screen
        snake.all_turtles[-1].showturtle()

    screen.update()
    time.sleep(0.1)
    snake.move()


    # initial border detection, this may be changed
    if snake.all_turtles[0].xcor() >= 300 or snake.all_turtles[0].xcor() <= -300:

        game_on = False

    elif snake.all_turtles[0].ycor() >= 300 or snake.all_turtles[0].ycor() <= -300:

        game_on = False


screen.exitonclick()


