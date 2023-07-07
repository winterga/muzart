# File for plotting the notes based on octaves + notes 

import turtle
import random

def main():
    for i in range(11): 
        drawShape(i, "A") 
        drawShape(i, "G#") 

    turtle.done()


# draws shape based on octave number
# octave 0 - circle, 1 - elliptical, rest of shapes correlate w octave #
def drawShape(octave, note):
    octave = octave + 1  # fixes octave number to correlate w shape side

    #these parameters should be divisble by 12 plz + make it a square for simplicity reasons
    screenSize = 960
    
    turtle.screensize(canvwidth=screenSize, canvheight=screenSize, bg="black")

    rightMost = screenSize / 2 #480
    leftMost = -1 * rightMost #-480 
    oneSixth = screenSize / 6 #160
    negOneSixth = -1 * oneSixth #-160
    oneFourth = screenSize / 4 #240 
    negOneFourth = -1 * oneFourth #-240 
    
    
    #dict with note value locations 
    #first list - x coord, 2nd list - y coord 
    noteDict = {
        "A": [[leftMost, negOneSixth], [leftMost, negOneFourth]],
        "A#": [[leftMost, negOneSixth], [negOneFourth, 0]],
        "B": [[leftMost, negOneSixth], [0, oneFourth]],
        "C": [[leftMost, negOneSixth], [leftMost, negOneFourth]],
        "C#": [[negOneSixth, oneSixth], [oneFourth, rightMost]],
        "D": [[negOneSixth, oneSixth], [negOneFourth, 0]],
        "D#": [[negOneSixth, oneSixth], [0, oneFourth]],
        "E": [[negOneSixth, oneSixth], [oneFourth, 480]],
        "F": [[oneSixth, rightMost], [leftMost, negOneFourth]],
        "F#": [[oneSixth, rightMost], [negOneFourth, 0]],
        "G": [[oneSixth, rightMost], [0, oneFourth]],
        "G#": [[oneSixth, rightMost], [oneFourth, rightMost]]
    }


    colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]

    coordRange = noteDict[note]
    xCoord = random.randint(coordRange[0][0], coordRange[0][1])
    yCoord = random.randint(coordRange[1][0], coordRange[1][1])  
     
    shape = turtle.Turtle()

    shape.goto(xCoord, yCoord)

    shape.speed(0)
 
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

main()

