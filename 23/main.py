import time
import random
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard


CARS = 10
level = 0


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

score = Scoreboard()
turtle = Player()
screen.onkey(turtle.move, 'Up')

cars =[]
for _ in range(CARS):
    car = CarManager(level)
    car.start_car()
    cars.append(car)



game_is_on = True



while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    
    for car in cars:
        
        car.move()
        if car.xcor() < -310:
          #  car.goto(random.randint(310, 390), random.randint(-250, 240))
          #  car = CarManager()
          #  cars.append(car)
            cars.remove(car)
            

        if (turtle.xcor() < car.xcor()+5 or turtle.xcor() > car.xcor()-5) and turtle.distance(car)<= 20:
            print(turtle.xcor() > car.xcor()-5)
            print(turtle.xcor())
            print(car.xcor()-5)
            print('Game Over')
            score.game_over()
            game_is_on = False
    if turtle.level_up_condition:
        level += 1
        score.score +=1
        score.refresh()
        for car in cars:
            car.level_up()
            turtle.level_up_condition = False

    random_chance = random.randint(1, 6)
    if random_chance == 1:
        car = CarManager(level)
        car.new_car()
        cars.append(car)
    
    
