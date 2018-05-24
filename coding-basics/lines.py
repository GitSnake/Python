import turtle
import random

cols=['blue','green','red','yellow']

turtle.speed(0)

for c in range(100):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    turtle.color(random.choice(cols))
    turtle.goto(x,y)