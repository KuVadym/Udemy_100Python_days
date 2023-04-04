import time
from turtle import Screen
from snake import SnakeBody
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')

snake = SnakeBody()
food = Food()
score = Scoreboard()
    
geme_on = True
while geme_on:
    if snake.body[0].distance(food) < 15:
        food.refresh()
        score.score += 1
        snake.extend()
        score.refresh()

    if snake.body[0].xcor() > 280 or snake.body[0].xcor() < -280 or snake.body[0].ycor() > 280 or snake.body[0].ycor() < -280:
        geme_on = False
        score.game_over()
    snake.move()
    screen.listen()
    for blok in snake.body[1:]:
        if snake.body[0].distance(blok) == 0:
            geme_on = False
            score.game_over()

        
    screen.onkey(key='Left', fun=snake.turn_left)
    screen.onkey(key='Right', fun=snake.turn_right)
    screen.onkey(key='Up', fun=snake.turn_up)
    screen.onkey(key='Down', fun=snake.turn_down)

    
