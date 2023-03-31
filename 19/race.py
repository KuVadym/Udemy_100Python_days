from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500, 400)
bet = screen. textinput("MAke your bet", "Which turtle will win the race? Enter a color: ")

turtle_colors = ['green', 'red', 'blue', 'yellow', 'purple', 'black']
turtles = []

start_x = -230
start_y = -180

for _ in range(6):
    turtle = Turtle()
    color = turtle_colors[_]
    turtle.color(color)
    turtle.penup()
    turtle.goto(start_x, start_y)
    start_y += (360 / 6)
    turtle.shape('turtle')
    turtles.append(turtle)

def random_score():
    return random.randint(1,5)

race = True
winner = ''
while race:
    for turtle in turtles:
        turtle.forward(random_score())
        if turtle.xcor() >= 220:
            race = False
            winner = turtle

if winner.fillcolor() == bet:
    print("You win")
else:
    print(f"You lose. {winner.fillcolor().upper()} won.") 

