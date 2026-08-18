from turtle import Screen, Turtle
import time

# variables

sneak_body = []
starting_positions = [(0,0), (-20, 0), (-40, 0)]
game_is_on = True

# functions

def create_sneak():
    for i in range(0,3):
        new_bit = Turtle(shape='square')
        new_bit.color('white')
        new_bit.penup()
        new_bit.goto(starting_positions[i])
        sneak_body.append(new_bit)
    screen.update()
    time.sleep(1)


def move_snake(sneak):
    for i in range(len(sneak), 0, -1):
        bit = sneak[i-1]
        bit.forward(0.05)
    screen.update()

# def turn(angle):
    

# screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# create a snake body

create_sneak()

while game_is_on:
    move_snake(sneak_body)




































# exiting and keeping the screen

screen.exitonclick()