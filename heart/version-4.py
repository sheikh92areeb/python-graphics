import math
from turtle import *
import time

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Turtle setup
speed(0)            # Maximum drawing speed
bgcolor("black")    # Background color
pensize(2)
penup()

# Smooth gradient colors (red to pink to yellow)
colors = ["#ff0000", "#ff3300", "#ff6600", "#ff9900", "#ffcc00", "#ffff00", "#ff66ff", "#ff33cc", "#ff0099"]

# Pulsing animation effect
scale = 1
for _ in range(3):  # Pulse the heart 3 times
    for i in range(6000):
        x = hearta(i) * 20 * scale
        y = heartb(i) * 20 * scale
        goto(x, y)
        color(colors[i // 667 % len(colors)])  # Smooth color transition
        pendown()
    
    scale += 0.1  # Increase scale for pulsing effect
    time.sleep(0.5)  # Pause for half a second between pulses
    clear()  # Clear the drawing for the next pulse
    penup()

hideturtle()
done()
