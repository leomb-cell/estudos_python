from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 20, "normal")
POSITION = (0 , 270)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed("fastest")
        self.goto(POSITION)
        self.score = 0    
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
    