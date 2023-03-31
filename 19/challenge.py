import colorgram
from turtle import Turtle, colormode, Screen
import random


turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_back():
    turtle.forward(-10)

def turn_left():
    turtle.left(5)

def turn_right():
    turtle.right(5)

def clear_all():
    turtle.clear()
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_all)
screen.exitonclick()
