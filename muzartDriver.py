import noteFinder as nf
import objectOrientedShapes as shapes
import turtle

#code for initializing screen turtle object
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(1920,1080)
screen.tracer(0)
screen.colormode(255)

#extracting data from note finder file 
muzart = nf.Muzart(file='/vanderbiltCS/SyBBURE/SU23/more-complicated-demo-song-2-both-hands.mp3')
#array of arrays ['note', string, intensity, duration]
noteList = muzart.run()

def getNoteOctave(noteOctave): 
    if len(noteOctave) == 2: 
        return noteOctave[0], int(noteOctave[1])
    return noteOctave[0:2], int(noteOctave[2])


drawBox = turtle.Turtle()
drawBox.penup() 
drawBox.goto(-150, -150)
drawBox.pendown()

for i in range(4): 
    drawBox.forward(300)
    drawBox.left(90)

#need to add noteList and put it into object oriented shapes -- for loop 
for item in noteList: 
    note, octave = getNoteOctave(item[0])
    drawingObj = shapes.createShape(note=note, octave=octave, intensity=item[1], duration=item[2], screen=screen)
    drawingObj.draw()







 




