import turtle
import random

def main():
    drawShape(1, "A")

    drawShape(1, "A#")

    drawShape(1, "B")

    drawShape(1, "C")

    drawShape(1, "A")
    turtle.done()

# draws shape based on octave number
# octave 0 - circle, 1 - elliptical, rest of shapes correlate w octave #
def drawShape(octave, note):
    octave = octave + 1  # fixes octave number to correlate w shape side

    screenWid = 960
    screenHei = 960
    turtle.screensize(canvwidth=screenWid, canvheight=screenHei, bg="black")

    #dict with note value locations 
    #first list - x coord, 2nd list - y coord 
    #change up dictionary values so they r not reliant on specific dim
    noteDict = {
        "A": [[0, 320], [0, 80]],
        "A#": [[0, 320], [80, 160]],
        "B": [[0, 320], [160, 240]],
        "C": [[0, 320], [240, 320]],
        "C#": [[320, 460], [0, 80]],
        "D": [[320, 460], [80, 160]],
        "D#": [[320, 460], [160, 240]],
        "E": [[320, 460], [240, 320]],
        "F": [[460, 640], [0, 80]],
        "F#": [[460, 640], [80, 160]],
        "G": [[460, 640], [160, 240]],
        "G#": [[460, 640], [240, 320]]
    }
    colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]

    coordRange = noteDict[note]
    xCoord = random.randint(coordRange[0][0], coordRange[0][1])
    yCoord = random.randint(coordRange[1][0], coordRange[1][1])  
     
    shape = turtle.Turtle()

    #xCoord = 100
    #yCoord = 100

    shape.penup()
    shape.goto(xCoord, yCoord)
    shape.pendown()

    shape.speed(0)

#these are all subject to change!!!! 
    radius = 50
    sideLength = 50


     #shapes section!
    shape.color(random.choice(colors))
    if octave == 1:
        shape.circle(radius)
    
    #draw elliptical 
    elif octave == 2:
        for i in range(2):
            shape.color(random.choice(colors))
            shape.circle(radius, 90)
            shape.circle(radius // 2, 90)
        shape.seth(-45)
    
    else:
        angle = int(360 / octave)
        shape.forward(sideLength)

        for i in range(octave):
            shape.color(random.choice(colors))
            shape.left(angle)
            shape.forward(sideLength)

    shape.write(octave)
    shape.write(note)


main()

