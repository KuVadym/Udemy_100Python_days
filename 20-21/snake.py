from turtle import Turtle

class SnakeBody:
    def __init__(self):
        self.size = 3
        self.body = []
        self.start_snake()
        

    def start_snake(self):
        x_blok_cor = 0
        for blok in range(self.size):
            turtle = self.add_blok()
            turtle.color('white')
            turtle.goto(x_blok_cor, 0)
            x_blok_cor -= 20
            self.body.append(turtle)

    def move(self):
        blok_pos = ''
        for blok in reversed(self.body):
            if self.body.index(blok) == 0:
                blok.forward(20)
            else:
                blok_pos = self.body[self.body.index(blok) -1].position()
                blok.goto(blok_pos)
            

    def add_blok(self):
        turtle = Turtle()
        turtle.color('black')
        turtle.penup()
        turtle.resizemode("user")
        turtle.shape("square")
        turtle.shapesize(1, 1, 1)
        return turtle

    def extend(self):
        turtle = self.add_blok()
        turtle.goto(self.body[-1].position())
        turtle.color('white')
        self.body.append(turtle)
                
    
    def turn_left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180) 
        
    def turn_right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0) 

    def turn_up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90) 

    def turn_down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270) 

















