from turtle import Turtle, Screen, setup
from random import * # not good practice, too confusing
from PIL import Image

# # instanciando a classe Turtle

timmy = Turtle()
timmy.shape('turtle')
timmy.speed(0)

setup(width=1000, height=1000, startx=500, starty=400)

# instanciando a classe Screen

screen = Screen()
screen.colormode(255)

# changing color
def rand_color():
    timmy.color(randint(0,255), randint(0,255), randint(0,255))

def dashed_line(lenght):
    for i in range(int(lenght/10)):
        timmy.down()
        rand_color()
        timmy.forward(10)
        timmy.up()
        timmy.forward(10)

def rand_walk():
    for i in range(1000):
        timmy.width(randint(1,10))
        rand_color()
        rand_len = randint(1,200)
        rand_radius = choice([0, 90, 180, 270])
        timmy.forward(rand_len)
        timmy.setheading(rand_radius)    

        # teleportando se sair dos limites

            # eixo x

        if timmy.xcor() > 1000 or timmy.xcor() < -990:
            print(f"hit the side at x:{timmy.xcor()}, y:{timmy.ycor()} ")
            timmy.teleport(randint(-1000,1000), randint(-490,490))
            timmy.right(rand_radius)

            # eixo y
        if timmy.ycor() > 500 or timmy.ycor() < -490:
            print(f"hit the side at x:{timmy.xcor()}, y:{timmy.ycor()} ")
            timmy.teleport(randint(-1000,1000), randint(-490,490))
            timmy.right(rand_radius)

rand_walk()
timmy.hideturtle()

# salvando resultado em png

while True:

    nome_resultado = str(input("Qual o nome do arquivo? "))

    if nome_resultado != '': break

timmy.getscreen().getcanvas().postscript(file="./python_padrao/studies/day_18/desenho.eps")
img = Image.open("./python_padrao/studies/day_18/desenho.eps")
img.save(f"./python_padrao/studies/day_18/{nome_resultado}.png", "PNG")

screen.exitonclick()


