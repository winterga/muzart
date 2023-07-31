import noteFinder as nf
import objectOrientedShapes as shapes
import turtle
import pygame

#code for initializing screen turtle object
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(1920,1080)
screen.tracer(0, 0)
screen.colormode(255)

drawBox = turtle.Turtle()
drawBox.hideturtle()
drawBox.speed(0)
drawBox.color('white')
drawBox.penup()
drawBox.goto(-100, -100)
drawBox.pendown()

for i in range(4):
    drawBox.forward(200)
    drawBox.left(90)

screen.update()

filename = '/vanderbiltCS/SyBBURE/SU23/Owl-City-Fireflies-m8.mp3'
#extracting data from note finder file 
muzart = nf.Muzart(file=filename)
#array of arrays ['note', string, intensity, duration]
noteList = muzart.run()
print(noteList)

def getNoteOctave(noteOctave): 
    if len(noteOctave) == 2: 
        return noteOctave[0], int(noteOctave[1])
    return noteOctave[0:2], int(noteOctave[2])

pygame.init() 
pygame.mixer.music.load(filename)
pygame.mixer.music.play()





#need to add noteList and put it into object oriented shapes -- for loop 
for item in noteList: 
    note, octave = getNoteOctave(item[0])
    drawingObj = shapes.createShape(note=note, octave=octave, intensity=item[1], duration=item[2], screen=screen)
    drawingObj.draw()

turtle.mainloop()





 




