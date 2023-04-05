import time
from turtle import Screen
from pong import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong game')

paddle_first_pos = - 390
paddle_second_pos = 390


score = Scoreboard()
paddle_l = Paddle(paddle_first_pos)
paddle_r = Paddle(paddle_second_pos)
ball = Ball()

game_on = True

screen.listen()   
screen.onkey(key='w', fun=paddle_l.move_up)
screen.onkey(key='s', fun=paddle_l.move_down)

screen.onkey(key='Up', fun=paddle_r.move_up)
screen.onkey(key='Down', fun=paddle_r.move_down)

while game_on:
    ball.start()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_speed *=-1
    if (ball.distance(paddle_r.paddle) < 50 and ball.xcor() > 370) or (ball.distance(paddle_l.paddle) < 50 and ball.xcor() < -370):
        ball.x_speed *= -1
        if ball.x_speed > 0:
            ball.x_speed += 1
        else:
            ball.x_speed -= 1
        if ball.y_speed > 0:
            ball.y_speed += 1
        else:
            ball.y_speed -= 1
    if ball.xcor() > 390:
        ball.refresh()
        score.score_l +=1
        score.refresh()
    if ball.xcor() < -390:
        ball.refresh()
        score.score_r +=1
        score.refresh()
