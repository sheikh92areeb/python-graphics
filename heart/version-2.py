import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Turtle setup
speed(0)            # Fastest drawing speed
bgcolor("black")    # Background color
color("red")        # Pen color
pensize(2)          # Thickness of the lines
penup()             # Lift the pen to move without drawing

# Drawing the heart
for i in range(6000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    goto(x, y)
    pendown()       # Start drawing after the first point

# Finish the drawing
hideturtle()        # Hide the turtle cursor
done()
