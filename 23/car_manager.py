from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.color(choice(COLORS))
        self.penup()
        self.shape('square')
        self.setheading(180)
        self.shapesize(1, 2)
        self.speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level
#       self.goto(randint(0, 400), randint(-250, 240))
        

    def start_car(self):
        self.goto(randint(0, 300), randint(-250, 240))

        
    def new_car(self):
        self.goto(310, randint(-250, 240))
    

    def move(self):
        self.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
        

        
        
