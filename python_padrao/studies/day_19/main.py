from turtle import Turtle, Screen

# screen

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")

# turtles

timmy = Turtle()
timmy.color('green')
timmy.penup()
timmy.goto(x=-230, y=-160)

tommy = Turtle()
tommy.color('purple')
tommy.penup()
tommy.goto(x=-230, y=-80)

johnny = Turtle()
johnny.color('orange')
johnny.penup()
johnny.goto(x=-230, y=0)

jenny = Turtle()
jenny.color('red')
jenny.penup()
jenny.goto(x=-230, y=80)

benny = Turtle()
benny.color('blue')
benny.penup()
benny.goto(x=-230, y=160)

# movements






screen.exitonclick()