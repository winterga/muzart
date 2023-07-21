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
screen.colormode(255)

tim = turtle.Turtle()
tim.hideturtle()
tim.pencolor('black')
tim.penup()
tim.speed(0)

sw = turtle.Turtle()
sw.hideturtle()
sw.pencolor('white')
sw.penup()
sw.speed(0)
sw.goto(-375, -375)


dif = 0
rad = 1
note = 10
fract = 0
intensity = 100
xcoor = random.randint(-300, 300)
ycoortemp = random.randint(-300,300)-rad
scale = 1   
ycoor = 0
time = 0.01
r = 120
g = 120
b = 120

def drawcircle(rad, fract, r, g, b):
    tim.pendown()
    tim.fillcolor(r, g, b)
    tim.begin_fill()
    tim.circle(rad+fract)
    tim.end_fill()
    tim.penup()

def reversecircle(rad, fract):
    tim.pendown()
    tim.fillcolor('black')
    tim.begin_fill()
    tim.circle(rad+fract)
    tim.end_fill()
    tim.penup()

def drawtriangle(rad, fract, r, g, b):
    tim.pendown()
    tim.fillcolor((r, g, b))
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(2):
        tim.left(120)
        tim.fd(2*(rad+fract))
    tim.left(120)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def reversetriangle(rad, fract):
    tim.pendown()
    tim.fillcolor('black')
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(2):
        tim.left(120)
        tim.fd(2*(rad+fract))
    tim.left(120)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def drawsquare(rad, fract, r, g, b):
    tim.pendown()
    tim.fillcolor((r, g, b))
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(3):
        tim.left(90)
        tim.fd(2*(rad+fract))
    tim.left(90)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def reversesquare(rad, fract):
    tim.pendown()
    tim.fillcolor('black')
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(3):
        tim.left(90)
        tim.fd(2*(rad+fract))
    tim.left(90)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def screenwipe():
    sw.pendown()
    sw.fillcolor('black')
    sw.begin_fill()
    for y in range(4):
        sw.fd(750)
        sw.left(90)
    sw.end_fill()
    sw.penup()
    
def drawpent(rad, fract, r, g, b):
    tim.pendown()
    tim.fillcolor((r, g, b))
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(4):
        tim.left(72)
        tim.fd(2*(rad+fract))
    tim.left(72)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def reversepent(rad, fract):
    tim.pendown()
    tim.fillcolor('black')
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(4):
        tim.left(72)
        tim.fd(2*(rad+fract))
    tim.left(72)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def drawhex(rad, fract, r, g, b):
    tim.pendown()
    tim.fillcolor((r, g, b))
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(5):
        tim.left(60)
        tim.fd(2*(rad+fract))
    tim.left(60)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def reversehex(rad, fract):
    tim.pendown()
    tim.fillcolor('black')
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(5):
        tim.left(60)
        tim.fd(2*(rad+fract))
    tim.left(60)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def drawhept(rad, fract, r, g, b):
    tim.pendown()
    tim.fillcolor((r, g, b))
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(6):
        tim.left(51.428)
        tim.fd(2*(rad+fract))
    tim.left(51.428)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def reversehept(rad, fract):
    tim.pendown()
    tim.fillcolor('black')
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(6):
        tim.left(51.428)
        tim.fd(2*(rad+fract))
    tim.left(51.428)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def drawocto(rad, fract, r, g, b):
    tim.pendown()
    tim.fillcolor((r, g, b))
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(7):
        tim.left(45)
        tim.fd(2*(rad+fract))
    tim.left(45)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()

def reverseoct(rad, fract):
    tim.pendown()
    tim.fillcolor('black')
    tim.begin_fill()
    tim.fd(rad+fract)
    for y in range(5):
        tim.left(60)
        tim.fd(2*(rad+fract))
    tim.left(60)
    tim.fd(rad+fract)
    tim.end_fill()
    tim.penup()


tim.goto(xcoor, ycoortemp)

for i in range(intensity):
    exponent1 = time*(i-1)
    fract = fract + exponent1
    ycoor = ycoortemp - (fract)
    tim.goto(xcoor, ycoor)
    drawocto(rad, fract, r, g, b)
    screen.update()
    screenwipe()
    
    
exponents = 0
ycoortemp2 = ycoor

for z in range(intensity):
    exponent1 = time*(i-z)
    fract = fract - exponent1
    exponents += exponent1
    ycoor = ycoortemp2 + (exponents)
    tim.goto(xcoor, ycoor) 
    drawocto(rad, fract, r, g, b)
    screen.update()
    screenwipe()





turtle.mainloop()