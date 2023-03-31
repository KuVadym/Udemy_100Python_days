###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, colormode, Screen
import random


turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

screen.listen()
screen.onkey(key='space', fun=move_forwards)
