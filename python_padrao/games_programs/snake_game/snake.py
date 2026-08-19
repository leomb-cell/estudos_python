from turtle import Screen, Turtle
import time
# GLOBALS

STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self, screen, ):
        self.screen = screen
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        for i in range(0,3):
            new_bit = Turtle(shape='square')
            new_bit.color('white')
            new_bit.penup()
            new_bit.goto(STARTING_POSITION[i])
            self.snake_body.append(new_bit)
        self.screen.update()

    # moving

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        time.sleep(0.07)
        self.screen.update()

    # turning 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        new_bit = Turtle(shape='square')
        new_bit.color('white')
        new_bit.penup()
        new_bit.goto(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body.append(new_bit)