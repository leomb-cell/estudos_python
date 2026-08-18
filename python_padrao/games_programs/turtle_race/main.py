from turtle import Turtle, Screen
import random

# variables

is_race_on = False
colors = ["green", "purple", "orange", "brown", "red", "blue"]
starting_Y_Position = [-160, -96, -32, 32, 96, 160]
turtles = []

# screen

screen = Screen()
screen.setup(500,400)

# initial positioning

for i in range(0,6):    
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_Y_Position[i])
    turtles.append(new_turtle)

# win function

def win_func(turtle):
    turtle.teleport(-125,0)
    turtle.hideturtle()
    turtle_name = turtles.index(turtle)
    if turtle_name == user_bet.lower():
        turtle.write(F"congratulations {colors[turtle_name]} won", align='center', font=('Arial', 36, 'normal'))
    else: 
        turtle.write(F"{colors[turtle_name]} won", align='left', font=('Arial', 36, 'normal'))


# getting bet

while True:    
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")
    user_bet = user_bet.lower()
    if user_bet:
        if user_bet in colors:
            is_race_on = True
            break
        else:
            print("Invalid turtle")    
    else: 
        print("Invalid turtle")

# actual race

while is_race_on:
    for turtle in turtles:
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= 230:
            is_race_on = False
            win_func(turtle)
            break


screen.exitonclick()