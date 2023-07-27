
#notes for rotations
#90 degree rotation x,y -> -y,x
#180 x,y -> -x, -y
#270 x,y -> y, -x
#i'm not sure how the drawing of spirals might be affected by rotations?

from abc import ABC, abstractmethod

# class Shape(ABC):
#     abstractmethod
#     def area(self):
#         pass

#     staticmethod
#     def create_shape(shape_type, *args, **kwargs):
#         if shape_type == 'rectangle':
#             return Rectangle(*args, **kwargs)
#         elif shape_type == 'circle':
#             return Circle(*args, **kwargs)
#         else:
#             raise ValueError("Invalid shape_type. Supported values are 'rectangle' or 'circle'.")

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius



import turtle
import random
from abc import ABC, abstractmethod

# in driver file
# screenSize = 960
# turtle.screensize(canvwidth=screenSize, canvheight=screenSize, bg="black")
# screen = turtle.Screen()
# screen.bgcolor('black')


class Shape(ABC):
  def __init__(self, note = 0, intensity = 0, duration = 0):
    self.note = note
    self.intensity = intensity
    self.duration = duration
    #add our four turtles here?? -- want them to be accessible by all the subclasses plz
    #add function

    self.turtObjs = [turtle.Turtle() for i in range(4)]

    for obj in self.turtObjs:
        obj.hideturtle()
        obj.jim.pencolor('black')
        obj.jim.penup()
        obj.jim.speed(0)

   #initialize filler vairables

    self.r = 1
    self.fract = 0 #important
    self.yCoor = 0
    self.xCoor = 0


  def screenwipe():
    sw = turtle.Turtle()
    sw.hideturtle()
    sw.pencolor('white')
    sw.penup()
    sw.speed(0)
    sw.goto(-960, -540)
    sw.pendown()
    sw.fillcolor('black')
    sw.begin_fill()
    for y in range(2):
        sw.fd(1920)
        sw.left(90)
        sw.fd(1080)
        sw.left(90)
    sw.end_fill()
    sw.penup()

  #generate random coordinate based on the note
  def getCoords(self):
    noteDict = {
        "A": [[-271, 0], [144, 384]],
        "A#": [[-271, 0], [144, 384]],
        "B": [[-271, 0], [144, 384]],
        "C": [[-96, 0], [96, 144]],
        "C#": [[-96, 0], [96, 144]],
        "D": [[-96, 0], [96, 144]],
        "D#": [[0, 271], [144, 384]],
        "E": [[0, 271], [144, 384]],
        "F": [[0, 271], [144, 384]],
        "F#": [[0, 96], [96, 144]],
        "G": [[0, 96], [96, 144]],
        "G#": [[0, 96], [96, 144]],
    }

    coordRange = noteDict[self.note]

    xCoor = random.randint(coordRange[0][0], coordRange[0][1])
    yCoor = random.randint(coordRange[1][0], coordRange[1][1])
    coordinates = [xCoor, yCoor]

    return coordinates

  def getRGB(self):
    #using intensity for color
    r = "10"
    g = "20"
    b = "30"
    color = [r, g, b]
    return color

  @abstractmethod
  def draw(self):
    pass

def createShape(self, note, octave, intensity, duration):
  if octave == 0:
    return Spiral(note, intensity, duration)

  elif octave == 1:
    return Oval(note, intensity, duration)

  elif octave == 2:
    return Circle(note, intensity, duration)

  elif octave == 3:
    return Triangle(note, intensity, duration)

  elif octave == 4:
    return Square(note, intensity, duration)

  elif octave == 5:
    return Pentagon(note, intensity, duration)

  elif octave == 6:
    return Hexagon(note, intensity, duration)

  elif octave == 7:
    return Heptagon(note, intensity, duration)

#spiral, oval, circle, then # of sides


class Spiral(Shape):
  def __init__(note, intensity, duration):
    super().__init__(note, intensity, duration)

  def draw(self):
    xCoorTemp,yCoorTemp = getCoords()
    r, g, b = getRGB()

    #code for drawing a spiral
    def drawSpiral(self, r, g, b):
      for obj in self.turtObjs:
        obj.pendown()
        obj.pencolor(r, g, b)
        for i in range(intensity):
            obj.forward(self.rad+self.fract+i)
            obj.right(15)
        obj.pencolor('black')
        obj.penup()

    #initial placement of turtle objects
    obj[0].goto(self.xCoorTemp, self.yCoorTemp)
    obj[1].goto(-self.yCoorTemp, self.xCoorTemp)
    obj[2].goto(-self.xCoorTemp, -self.yCoorTemp)
    obj[3].goto(self.yCoorTemp, -self.xCoorTemp)

    #code for growing shapes
    for i in range((int(duration*100))/2):
        exponent1 = 0.01*(i-1)
        self.fract = self.fract + exponent1
        self.ycoor = yCoorTemp - (self.fract)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawSpiral(r, g, b)
        screen.update()
        screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.ycoor

    #code for shrinking shapes
    for z in range((int(duration*100))/2):
        exponent1 = 0.01*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawSpiral(r, g, b)
        screen.update()
        screenwipe()

class Oval(Shape):
  def __init__(note, intensity, duration):
    super().__init__(note, intensity, duration)

  def draw(self):
    xCoorTemp,yCoorTemp = getCoords()
    r, g, b = getRGB()

    def drawOval(self, r, g, b):
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
    obj[0].goto(self.xCoorTemp, self.yCoorTemp)
    obj[1].goto(-self.yCoorTemp, self.xCoorTemp)
    obj[2].goto(-self.xCoorTemp, -self.yCoorTemp)
    obj[3].goto(self.yCoorTemp, -self.xCoorTemp)

    #code for growing shapes
    for i in range((int(duration*100))/2):
        exponent1 = 0.01*(i-1)
        self.fract = self.fract + exponent1
        self.ycoor = yCoorTemp - (self.fract)
        obj[0].goto(self.xCoor, self.yCoor)         
        obj[1].goto(-self.yCoor, self.xCoor)         
        obj[2].goto(-self.xCoor, -self.yCoor)         
        obj[3].goto(self.yCoor, -self.xCoor)(self.xCoor, self.yCoor)
        drawOval(r, g, b)
        screen.update()
        screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.ycoor

    #code for shrinking shapes
    for z in range((int(duration*100))/2):
        exponent1 = 0.01*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawOval(r, g, b)
        screen.update()
        screenwipe()


#can we just have a general polygon shape or should we do square, triangle, pentagon, etc
class Circle(Shape):
  def __init__(note, intensity, duration):
    super().__init__(note, intensity, duration)

  def draw(self):
    xCoor,yCoorTemp = getCoords()
    r, g, b = getRGB()

    def drawCircle():
      for obj in self.turtObjs:
        obj.pendown()
        obj.fillcolor(r, g, b)
        obj.begin_fill()
        obj.circle(self.rad+self.fract)
        obj.end_fill()
        obj.penup()

    #initial placement of turtle objects
    obj[0].goto(self.xCoorTemp, self.yCoorTemp)
    obj[1].goto(-self.yCoorTemp, self.xCoorTemp)
    obj[2].goto(-self.xCoorTemp, -self.yCoorTemp)
    obj[3].goto(self.yCoorTemp, -self.xCoorTemp)

    #code for growing shapes
    for i in range((int(duration*100))/2):
        exponent1 = 0.01*(i-1)
        self.fract = self.fract + exponent1
        self.ycoor = yCoorTemp - (self.fract)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawCircle(r, g, b)
        screen.update()
        screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.ycoor

    #code for shrinking shapes
    for z in range((int(duration*100))/2):
        exponent1 = 0.01*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawCircle(r, g, b)
        screen.update()
        screenwipe()


class Triangle(Shape):
  def __init__(note, intensity, duration):
    super().__init__(note, intensity, duration)

  def draw(self):
    xCoor,yCoorTemp = getCoords()
    r, g, b = getRGB()

    def drawTriangle():
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
    obj[0].goto(self.xCoorTemp, self.yCoorTemp)
    obj[1].goto(-self.yCoorTemp, self.xCoorTemp)
    obj[2].goto(-self.xCoorTemp, -self.yCoorTemp)
    obj[3].goto(self.yCoorTemp, -self.xCoorTemp)

    #code for growing shapes
    for i in range((int(duration*100))/2):
        exponent1 = 0.01*(i-1)
        self.fract = self.fract + exponent1
        self.ycoor = yCoorTemp - (self.fract)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawTriangle(r, g, b)
        screen.update()
        screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.ycoor

    #code for shrinking shapes
    for z in range((int(duration*100))/2):
        exponent1 = 0.01*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawTriangle(r, g, b)
        screen.update()
        screenwipe()

class Square(Shape):
  def __init__(note, intensity, duration):
    super().__init__(note, intensity, duration)

  def draw(self):
    xCoor,yCoorTemp = getCoords()
    r, g, b = getRGB()

    def drawSquare(self, r, g, b):
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
    obj[0].goto(self.xCoorTemp, self.yCoorTemp)
    obj[1].goto(-self.yCoorTemp, self.xCoorTemp)
    obj[2].goto(-self.xCoorTemp, -self.yCoorTemp)
    obj[3].goto(self.yCoorTemp, -self.xCoorTemp)

    #code for growing shapes
    for i in range((int(duration*100))/2):
        exponent1 = 0.01*(i-1)
        self.fract = self.fract + exponent1
        self.ycoor = yCoorTemp - (self.fract)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawSquare(r, g, b)
        screen.update()
        screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.ycoor

    #code for shrinking shapes
    for z in range((int(duration*100))/2):
        exponent1 = 0.01*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawSquare(r, g, b)
        screen.update()
        screenwipe()


class Pentagon(Shape):
  def __init__(note, intensity, duration):
    super().__init__(note, intensity, duration)

  def draw(self):
    xCoor,yCoorTemp = getCoords()
    r, g, b = getRGB()

    def drawPentagon(self, r, g, b):
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
    obj[0].goto(self.xCoorTemp, self.yCoorTemp)
    obj[1].goto(-self.yCoorTemp, self.xCoorTemp)
    obj[2].goto(-self.xCoorTemp, -self.yCoorTemp)
    obj[3].goto(self.yCoorTemp, -self.xCoorTemp)

    #code for growing shapes
    for i in range((int(duration*100))/2):
        exponent1 = 0.01*(i-1)
        self.fract = self.fract + exponent1
        self.ycoor = yCoorTemp - (self.fract)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawPentagon(r, g, b)
        screen.update()
        screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.ycoor

    #code for shrinking shapes
    for z in range((int(duration*100))/2):
        exponent1 = 0.01*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawPentagon(r, g, b)
        screen.update()
        screenwipe()

class Hexagon(Shape):
  def __init__(note, intensity, duration):
    super().__init__(note, intensity, duration)

  def draw(self):
    xCoor,yCoorTemp = getCoords()
    r, g, b = getRGB()

    def drawHexagon(self, r, g, b):
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
    obj[0].goto(self.xCoorTemp, self.yCoorTemp)
    obj[1].goto(-self.yCoorTemp, self.xCoorTemp)
    obj[2].goto(-self.xCoorTemp, -self.yCoorTemp)
    obj[3].goto(self.yCoorTemp, -self.xCoorTemp)

    #code for growing shapes
    for i in range((int(duration*100))/2):
        exponent1 = 0.01*(i-1)
        self.fract = self.fract + exponent1
        self.ycoor = yCoorTemp - (self.fract)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawHexagon(r, g, b)
        screen.update()
        screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.ycoor

    #code for shrinking shapes
    for z in range((int(duration*100))/2):
        exponent1 = 0.01*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawHexagon(r, g, b)
        screen.update()
        screenwipe()

class Heptagon(Shape):
  def __init__(note, intensity, duration):
    super().__init__(note, intensity, duration)

  def draw(self):
    xCoor,yCoorTemp = getCoords()
    r, g, b = getRGB()

    def drawHeptagon(self, r, g, b):
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
    obj[0].goto(self.xCoorTemp, self.yCoorTemp)
    obj[1].goto(-self.yCoorTemp, self.xCoorTemp)
    obj[2].goto(-self.xCoorTemp, -self.yCoorTemp)
    obj[3].goto(self.yCoorTemp, -self.xCoorTemp)

    #code for growing shapes
    for i in range((int(duration*100))/2):
        exponent1 = 0.01*(i-1)
        self.fract = self.fract + exponent1
        self.ycoor = yCoorTemp - (self.fract)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawHeptagon(r, g, b)
        screen.update()
        screenwipe()

    #variable reset
    exponents = 0
    yCoorTemp2 = self.ycoor

    #code for shrinking shapes
    for z in range((int(duration*100))/2):
        exponent1 = 0.01*(i-z)
        self.fract = self.fract - exponent1
        exponents += exponent1
        self.yCoor = yCoorTemp2 + (exponents)
        obj[0].goto(self.xCoor, self.yCoor)
        obj[1].goto(-self.yCoor, self.xCoor)
        obj[2].goto(-self.xCoor, -self.yCoor)
        obj[3].goto(self.yCoor, -self.xCoor)
        drawHeptagon(r, g, b)
        screen.update()
        screenwipe()



turtle.mainloop()

