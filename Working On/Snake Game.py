# Creating the snake game!

from turtle import *
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snakey Snakey Snake Snake")
screen.tracer(0)


START_COORS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:


    def __init__(self):
        self.all_turtles = []
        self.create_snake()
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

            new_x = self.all_turtles[x-1].xcor()
            new_y = self.all_turtles[x-1].ycor()
            self.all_turtles[x].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):

        self.head.setheading(90)
    
    def down(self):

        self.head.setheading(270)

    def left(self):

        self.head.setheading(180)

    def right(self):

        self.head.setheading(0)

    def add_seg(self):

        turtle = Turtle()
        turtle.hideturtle()
        turtle.pu()
        turtle.color("white")
        turtle.shape("square")
        self.all_turtles.append(turtle)
        screen.update()


snake = Snake()

game_on = True

while game_on:

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.add_seg:
        snake.all_turtles[-1].showturtle()

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.all_turtles[0].xcor() >= 300 or snake.all_turtles[0].xcor() <= -300:

        game_on = False

    elif snake.all_turtles[0].ycor() >= 300 or snake.all_turtles[0].ycor() <= -300:

        game_on = False

    



screen.exitonclick()


