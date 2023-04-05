from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(-30, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.score_l} : {self.score_r}", False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Arial", 24, "normal"))
