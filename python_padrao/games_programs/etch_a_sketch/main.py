from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# functions

def move_forward():
    tim.forward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def move_backward():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
# start screen listening

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()