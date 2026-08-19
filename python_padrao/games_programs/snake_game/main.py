from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


# variables

game_is_on = True

# screen config

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# create a snake body

snake = Snake(screen)

# create food

food = Food()

# show score

score = ScoreBoard()

# user control

screen.listen()
screen.onkeypress(key="w", fun=snake.up)
screen.onkeypress(key="a", fun=snake.left)
screen.onkeypress(key="s", fun=snake.down)
screen.onkeypress(key="d", fun=snake.right)

# game loop
 
while game_is_on:
    screen.update()
    snake.move()
    # food collision

    if snake.head.distance(food) < 16:
        print("nom nom nom")
        food.refresh()
        score.increase_score()
        snake.grow()

    



































# exiting and keeping the screen

screen.exitonclick()