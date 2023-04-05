from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.shapesize(1, 1, 1)
        self.speed("fastest")
        self.x_speed = 1 
        self.y_speed = 1
        self.refresh()

    def refresh(self):
        start_score = [-2, -1, 1, 2]
        self.goto(0, 0)
        self.x_speed = random.choice(start_score) 
        self.y_speed = random.choice(start_score)

    def start(self):
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)
