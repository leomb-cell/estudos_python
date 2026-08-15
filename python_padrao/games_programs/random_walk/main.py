from turtle import Turtle, Screen, setup
from random import * # not good practice, too confusing
from PIL import Image
import time

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
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r,g,b)
    timmy.color(random_color)

def dashed_line(lenght):
    for i in range(int(lenght/10)):
        timmy.down()
        rand_color()
        timmy.forward(10)
        timmy.up()
        timmy.forward(10)

def rand_walk():
    for i in range(1000):
        timmy.width(2)
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

# caminhos para os arquivos

result_path = f"./python_padrao/games_programs/random_walk/art/results/{nome_resultado}.png"
eps_path = f"./python_padrao/games_programs/random_walk/art/eps/{nome_resultado}.eps"

timmy.getscreen().getcanvas().postscript(file=eps_path)
img = Image.open(eps_path)
img.save( result_path, "PNG")



# fechar a janela

screen.exitonclick()


