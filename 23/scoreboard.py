from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.speed("fastest")
        self.penup()
        self.color("black")
        self.goto(-280, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.score}", False, align="left", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=FONT)

