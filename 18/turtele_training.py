from turtle import Turtle, colormode
import random

turtle = Turtle()
colormode(255)
turtle.pensize(1)

# for _ in range(20):
#    if _ % 2 == 0:
#        turtle.penup()
#    else:
#        turtle.pendown()
#    turtle.forward(10)
    
sides = [3, 4, 5, 6, 7, 8]
colors = ['red', 'blue', 'green', 'yellow', 'brown', 'purple']

def create_figure(side):
    for _ in range(side):
        turtle.forward(100)
        turtle.left(360/side)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# for side in sides:
#   turtle.color(random.choice(colors))
#    create_figure(side)  



#while True:
#    turtle.pensize(5)
#    way = random.choice([90, 180, 270, 0])
#    turtle.left(way)
#    turtle.color(random_color())
#    turtle.forward(30)

for _ in range(36):
    turtle.color(random_color())
    turtle.speed('fastest')
    turtle.circle(50)
    turtle.left(10)

