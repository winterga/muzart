#prettypictures

import numpy as np
import turtle
import matplotlib.pyplot as plt
import random

#Coords Key:
#   C = 
#   C# =
#   D =
#   D# =
#   E =
#   F =
#   F# =
#   G =
#   G# =
#   A =
#   A# =
#   B =



screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(750,750)
screen.tracer(0)

tim = turtle.Turtle()

tim.hideturtle()
tim.pencolor('black')
tim.penup()
tim.speed(0)
dif = 0
r =1
note = 10
fract = 0
intensity = 200
xcoor = random.randint(-100,100)
ycoortemp = random.randint(-100,100)-r
scale = 1   
ycoor = 0
curi = 0

tim.goto(xcoor, ycoortemp)
def drawcircle(r, fract):
    tim.pendown()
    tim.fillcolor('red')
    tim.begin_fill()
    tim.circle(r+fract)
    tim.end_fill()
    tim.penup()

def reversecircle(r, fract):
    tim.pendown()
    tim.fillcolor('black')
    tim.begin_fill()
    tim.circle(r+fract)
    tim.end_fill()
    tim.penup()

for i in range(intensity):
    exponent1 = 0.01*(i-1)
    fract = fract + exponent1
    ycoor = ycoortemp-(fract)
    tim.goto(xcoor, ycoor)
    drawcircle(r, fract)
    screen.update()
    reversecircle(r, fract)
    

ycoortemp2 = ycoor

for z in range(intensity):
    exponent1 = 0.01*(i-1)
    fract = fract - exponent1
    ycoor += (exponent1)
    tim.goto(xcoor, ycoor) 
    i -= 1
    drawcircle(r, fract)
    screen.update()
    reversecircle(r+5, fract)
    





turtle.mainloop()