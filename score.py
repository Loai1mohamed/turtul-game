from turtle import Turtle

font = ("Times New Roman", 15, "normal")
Font = ("Times New Roman", 50, "normal")
align = "center"
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score_written()


    def score_written(self):
        self.write(f"score {self.score}", align=align, font=font)


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over ", align=align, font=Font)


    def score_incress(self):
        self.score += 1
        self.clear()
        self.score_written()

