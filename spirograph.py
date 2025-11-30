import turtle as t
import random

kalam = t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color 

for _ in range(100):
    kalam.speed("fastest")
    kalam.color(random_color())
    kalam.circle(100)
    current_heading=kalam.heading()
    kalam.setheading(current_heading + 10)

screen = t.Screen()
screen.exitonclick()