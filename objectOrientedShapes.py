
#notes for rotations
#90 degree rotation x,y -> -y,x
#180 x,y -> -x, -y
#270 x,y -> y, -x
#i'm not sure how the drawing of spirals might be affected by rotations?

from abc import ABC, abstractmethod

import turtle
import random
import math
import time

# function to scale intensity values to red value
def scale_to_red(val):
    return int(round(255 * val))

# function to scale intensity values to green value
def scale_to_green(val):
    # if val <= 0.5:
    return int(round(255 * (1 - 2 * math.fabs(val - 0.5))))
    # else:
    #     return int(round(255 * (2 * math.fabs(val - 0.5))))

# function to scale intensity values to blue value
def scale_to_blue(val):
    return int(round(255 * (1 - val)))

"""Abstract Base Class for Shape hierarchy

    Defines a common interface for all shapes in the hierarchy.

    Parameters
    ----------
    arg1 : turtle.Screen
        turtle screen object taken from turtle module - this is the canvas on which the shapes will be drawn
    arg2 : str
        note value of a given time period for an audio file - describes the location of the shape on the canvas
    arg3 : float
        intensity value of a given time period for an audio file - describes the color of the shape on the canvas
    arg4 : float
        time that a given note is played for in an audio file - describes the size of the shape on the canvas

    See Also
    --------
    Oval
    Sprial
    Circle
    Triangle
    Square
    Pentagon
    Hexagon
    Heptagon
    Octagon

"""

class Shape(ABC):
  def __init__(self, screen: turtle.Screen, note = "C", intensity = 0, duration = 0):
    # assert isinstance(screen, turtle.Screen), "You must pass in a turtle.Screen object!"
    self.note = note
    self.intensity = intensity
    self.duration = duration
    self.screen = screen
    self.noteDict = {
        "A": [[-400, 0], [295, 450]],
        "A#": [[-400, 0], [295, 450]],
        "B": [[-400, 0], [295, 450]],
        "C": [[-400, 0], [295, 450]],
        "C#": [[0, 400], [295, 450]],
        "D": [[0, 400], [295, 450]],
        "D#": [[0, 400], [295, 450]],
        "E": [[0, 400], [295, 450]],
        "F": [[-100, 100], [150, 295]],
        "F#": [[-100, 100], [150, 295]],
        "G": [[-100, 100], [150, 295]],
        "G#": [[-100, 100], [150, 295]],
    }
    
    #create turtle objects
    self.turtObjs = [turtle.Turtle() for i in range(4)]

    for obj in self.turtObjs:
        obj.hideturtle()
        obj.pencolor('black')
        obj.penup()
        obj.speed(0)

   #initialize filler vairables

    self.rad = 15
    self.fract = 0 #important
    self.yCoor = 0
    self.xCoor = 0
    self.timePerSlice = 0.01 #added radial length every slice
    self.shapeDif = int((round(self.duration*30))/2)
    self.fps = 60
    self.frame_time = 1/self.fps # 0.1 for 10 fps 

    #cover shapes previously drawn; allows for visuals to appear smooth and not leave traces behind
  def screenwipe(self):
    self.turtObjs[0].clear()
    self.turtObjs[1].clear()
    self.turtObjs[2].clear()
    self.turtObjs[3].clear()
  #   sw = turtle.Turtle()
  #   sw.hideturtle()
  #   sw.pencolor('white')
  #   sw.penup()
  #   sw.speed(0)
  #   sw.goto(-960, -540)
  #   sw.pendown()
  #   sw.fillcolor('black')
  #   sw.begin_fill()
  #   for y in range(2):
  #       sw.fd(1920)
  #       sw.left(90)
  #       sw.fd(1080)
  #       sw.left(90)
  #   sw.end_fill()
  #   sw.penup()

  #generate random coordinate based on the note
  def getCoords(self):
    coordRange = self.noteDict[self.note]

    xCoor = random.randint(coordRange[0][0], coordRange[0][1])
    yCoor = random.randint(coordRange[1][0], coordRange[1][1])

    return xCoor, yCoor

  #generate color from normalzied intensity values read in
  def getRGB(self):
    r = scale_to_red(self.intensity)
    g = scale_to_green(self.intensity)
    b = scale_to_blue(self.intensity)
    return r, g, b

  @abstractmethod
  def draw(self):
    pass

# factory function to create different shapes
def createShape(note, octave, intensity, duration, screen: turtle.Screen):
  if octave == 0:
    return Spiral(note=note, intensity=intensity, duration=duration, screen=screen)

  elif octave == 1:
    return Oval(note=note, intensity=intensity, duration=duration, screen=screen)

  elif octave == 2:
    return Circle(note=note, intensity=intensity, duration=duration, screen=screen)

  elif octave == 3:
    return Triangle(note=note, intensity=intensity, duration=duration, screen=screen)

  elif octave == 4:
    return Square(note=note, intensity=intensity, duration=duration, screen=screen)

  elif octave == 5:
    return Pentagon(note=note, intensity=intensity, duration=duration, screen=screen)

  elif octave == 6:
    return Hexagon(note=note, intensity=intensity, duration=duration, screen=screen)

  elif octave == 7:
    return Heptagon(note=note, intensity=intensity, duration=duration, screen=screen)

#spiral, oval, circle, then # of sides


class Spiral(Shape):
  def __init__(self, note, intensity, duration, screen):
    super().__init__(note=note, intensity=intensity, duration=duration, screen=screen)

  def draw(self):
    xCoorTemp, yCoorTemp = self.getCoords()
    r, g, b = self.getRGB()

    #code for drawing a spiral
    def drawSpiral(r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.pencolor(r, g, b)
        for i in range(self.intensity):
            obj.forward(self.rad+self.fract+i)
            obj.right(15)
        # obj.pencolor('black')
        obj.penup()

    #initial placement of turtle objects
    self.turtObjs[0].goto(xCoorTemp, yCoorTemp)
    self.turtObjs[1].goto(-yCoorTemp, xCoorTemp)
    self.turtObjs[2].goto(-xCoorTemp, -yCoorTemp)
    self.turtObjs[3].goto(yCoorTemp, -xCoorTemp)

    self.xCoor = xCoorTemp

    #code for growing shapes
    for i in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-1)
        self.fract = self.fract + exponent1
        self.yCoor = yCoorTemp - (self.fract)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawSpiral(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.yCoor

    #code for shrinking shapes
    for z in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawSpiral(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

class Oval(Shape):
  def __init__(self, note, intensity, duration, screen):
    super().__init__(note=note, intensity=intensity, duration=duration, screen=screen)

  def draw(self):
    xCoorTemp, yCoorTemp = self.getCoords()
    r, g, b = self.getRGB()

    def drawOval(r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.fillcolor(r, g, b)
        obj.begin_fill()
        for i in range(2):
              obj.circle(self.rad + self.fract, 90)
              obj.circle(self.rad + self.fract// 2, 90)
        obj.end_fill()
        obj.penup()

    #initial placement of turtle objects
    self.turtObjs[0].goto(xCoorTemp, yCoorTemp)
    self.turtObjs[1].goto(-yCoorTemp, xCoorTemp)
    self.turtObjs[2].goto(-xCoorTemp, -yCoorTemp)
    self.turtObjs[3].goto(yCoorTemp, -xCoorTemp)

    self.xCoor = xCoorTemp

    #code for growing shapes
    for i in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-1)
        self.fract = self.fract + exponent1
        self.yCoor = yCoorTemp - (self.fract)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawOval(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.yCoor

    #code for shrinking shapes
    for z in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawOval(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()


#can we just have a general polygon shape or should we do square, triangle, pentagon, etc
class Circle(Shape):
  def __init__(self, note, intensity, duration, screen):
    super().__init__(note=note, intensity=intensity, duration=duration, screen=screen)

  def draw(self):
    xCoorTemp, yCoorTemp = self.getCoords()
    r, g, b = self.getRGB()

    def drawCircle(r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.fillcolor(r, g, b)
        obj.begin_fill()
        obj.circle(self.rad+self.fract)
        obj.end_fill()
        obj.penup()

    #initial placement of turtle objects
    self.turtObjs[0].goto(xCoorTemp, yCoorTemp)
    self.turtObjs[1].goto(-yCoorTemp, xCoorTemp)
    self.turtObjs[2].goto(-xCoorTemp, -yCoorTemp)
    self.turtObjs[3].goto(yCoorTemp, -xCoorTemp)

    self.xCoor = xCoorTemp

    #code for growing shapes
    for i in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-1)
        self.fract = self.fract + exponent1
        self.yCoor = yCoorTemp - (self.fract)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawCircle(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.yCoor

    #code for shrinking shapes
    for z in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawCircle(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()


class Triangle(Shape):
  def __init__(self, note, intensity, duration, screen):
    super().__init__(note=note, intensity=intensity, duration=duration, screen=screen)

  def draw(self):
    xCoorTemp, yCoorTemp = self.getCoords()
    r, g, b = self.getRGB()

    def drawTriangle(r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.fillcolor((r, g, b))
        obj.begin_fill()
        obj.fd(self.rad+self.fract)
        for y in range(2):
            obj.left(120)
            obj.fd(2*(self.rad+self.fract))
        obj.left(120)
        obj.fd(self.rad+self.fract)
        obj.end_fill()
        obj.penup()

    #initial placement of turtle objects
    self.turtObjs[0].goto(xCoorTemp, yCoorTemp)
    self.turtObjs[1].goto(-yCoorTemp, xCoorTemp)
    self.turtObjs[2].goto(-xCoorTemp, -yCoorTemp)
    self.turtObjs[3].goto(yCoorTemp, -xCoorTemp)

    self.xCoor = xCoorTemp

    #code for growing shapes
    for i in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-1)
        self.fract = self.fract + exponent1
        self.yCoor = yCoorTemp - (self.fract)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawTriangle(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.yCoor

    #code for shrinking shapes
    for z in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawTriangle(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

class Square(Shape):
  def __init__(self, note, intensity, duration, screen):
    super().__init__(note=note, intensity=intensity, duration=duration, screen=screen)

  def draw(self):
    xCoorTemp, yCoorTemp = self.getCoords()
    r, g, b = self.getRGB()

    def drawSquare(r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.fillcolor((r, g, b))
        obj.begin_fill()
        obj.fd(self.rad+self.fract)
        for y in range(3):
            obj.left(90)
            obj.fd(2*(self.rad+self.fract))
        obj.left(90)
        obj.fd(self.rad+self.fract)
        obj.end_fill()
        obj.penup()

    #initial placement of turtle objects
    self.turtObjs[0].goto(xCoorTemp, yCoorTemp)
    self.turtObjs[1].goto(-yCoorTemp, xCoorTemp)
    self.turtObjs[2].goto(-xCoorTemp, -yCoorTemp)
    self.turtObjs[3].goto(yCoorTemp, -xCoorTemp)

    self.xCoor = xCoorTemp

    #code for growing shapes
    for i in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-1)
        self.fract = self.fract + exponent1
        self.yCoor = yCoorTemp - (self.fract)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawSquare(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.yCoor

    #code for shrinking shapes
    for z in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawSquare(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()


class Pentagon(Shape):
  def __init__(self, note, intensity, duration, screen):
    super().__init__(note=note, intensity=intensity, duration=duration, screen=screen)

  def draw(self):
    xCoorTemp, yCoorTemp = self.getCoords()
    r, g, b = self.getRGB()

    def drawPentagon(r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.fillcolor((r, g, b))
        obj.begin_fill()
        obj.fd(self.rad+self.fract)
        for y in range(4):
            obj.left(72)
            obj.fd(2*(self.rad+self.fract))
        obj.left(72)
        obj.fd(self.rad+self.fract)
        obj.end_fill()
        obj.penup()

    #initial placement of turtle objects
    self.turtObjs[0].goto(xCoorTemp, yCoorTemp)
    self.turtObjs[1].goto(-yCoorTemp, xCoorTemp)
    self.turtObjs[2].goto(-xCoorTemp, -yCoorTemp)
    self.turtObjs[3].goto(yCoorTemp, -xCoorTemp)

    self.xCoor = xCoorTemp

    #code for growing shapes
    for i in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-1)
        self.fract = self.fract + exponent1
        self.yCoor = yCoorTemp - (self.fract)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawPentagon(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.yCoor

    #code for shrinking shapes
    for z in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawPentagon(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

class Hexagon(Shape):
  def __init__(self, note, intensity, duration, screen):
    super().__init__(note=note, intensity=intensity, duration=duration, screen=screen)

  def draw(self):
    xCoorTemp, yCoorTemp = self.getCoords()
    r, g, b = self.getRGB()

    def drawHexagon(r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.fillcolor((r, g, b))
        obj.begin_fill()
        obj.fd(self.rad+self.fract)
        for y in range(5):
            obj.left(60)
            obj.fd(2*(self.rad+self.fract))
        obj.left(60)
        obj.fd(self.rad+self.fract)
        obj.end_fill()
        obj.penup()

    #initial placement of turtle objects
    self.turtObjs[0].goto(xCoorTemp, yCoorTemp)
    self.turtObjs[1].goto(-yCoorTemp, xCoorTemp)
    self.turtObjs[2].goto(-xCoorTemp, -yCoorTemp)
    self.turtObjs[3].goto(yCoorTemp, -xCoorTemp)

    self.xCoor = xCoorTemp
    #code for growing shapes
    for i in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-1)
        self.fract = self.fract + exponent1
        self.yCoor = yCoorTemp - (self.fract)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawHexagon(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.yCoor

    #code for shrinking shapes
    for z in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawHexagon(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

class Heptagon(Shape):
  def __init__(self, note, intensity, duration, screen):
    super().__init__(note=note, intensity=intensity, duration=duration, screen=screen)

  def draw(self):
    xCoorTemp, yCoorTemp = self.getCoords()
    r, g, b = self.getRGB()

    def drawHeptagon(r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.fillcolor((r, g, b))
        obj.begin_fill()
        obj.fd(self.rad+self.fract)
        for y in range(6):
            obj.left(51.428)
            obj.fd(2*(self.rad+self.fract))
        obj.left(51.428)
        obj.fd(self.rad+self.fract)
        obj.end_fill()
        obj.penup()

    #initial placement of turtle objects
    self.turtObjs[0].goto(xCoorTemp, yCoorTemp)
    self.turtObjs[1].goto(-yCoorTemp, xCoorTemp)
    self.turtObjs[2].goto(-xCoorTemp, -yCoorTemp)
    self.turtObjs[3].goto(yCoorTemp, -xCoorTemp)

    self.xCoor = xCoorTemp
    #code for growing shapes
    for i in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-1)
        self.fract = self.fract + exponent1
        self.yCoor = yCoorTemp - (self.fract)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawHeptagon(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.yCoor

    #code for shrinking shapes
    for z in range(self.shapeDif):
        exponent1 = self.timePerSlice*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        self.turtObjs[0].goto(self.xCoor, self.yCoor)
        self.turtObjs[1].goto(-self.yCoor, self.xCoor)
        self.turtObjs[2].goto(-self.xCoor, -self.yCoor)
        self.turtObjs[3].goto(self.yCoor, -self.xCoor)
        drawHeptagon(r, g, b)
        time.sleep(self.frame_time)
        self.screen.update()
        self.screenwipe()




