from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = self.start_paddle(position)

    def add_blok(self):
        paddle = Turtle()
        paddle.color('black')
        paddle.penup()
        paddle.resizemode("user")
        paddle.shape("square")
        paddle.shapesize(1, 5)
        paddle.setheading(90)
        return paddle

    def start_paddle(self, position):

        paddle = self.add_blok()
        paddle.goto(position, 0)
        paddle.color('white')
        return paddle



    def move_up(self):
        y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), y)

    def move_down(self):
        y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), y)

    
