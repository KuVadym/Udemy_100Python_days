from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(-30, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score {self.score}", False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Arial", 24, "normal"))
