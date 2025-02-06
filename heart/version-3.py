import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Turtle setup
speed(0)            # Maximum drawing speed
bgcolor("black")    # Background color
pensize(2)          # Thickness of the lines
penup()

# Gradient fill effect
colors = ["#ff0000", "#ff3300", "#ff6600", "#ff9900", "#ffcc00", "#ffff00", "#ccff00", "#99ff00", "#66ff00", "#33ff00"]

# Drawing the heart with animation and gradient colors
for i in range(6000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    goto(x, y)
    
    # Change color every 600 iterations for the gradient effect
    color(colors[i // 600 % len(colors)])
    pendown()
    
hideturtle()        # Hide the turtle cursor
done()
