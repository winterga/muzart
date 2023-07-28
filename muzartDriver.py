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

#part where we 

def getNoteOctave(noteOctave): 
    if len(noteOctave) == 2: 
        return noteOctave[0], int(noteOctave[1])
    return noteOctave[0:2], int(noteOctave[2])



#need to add noteList and put it into object oriented shapes -- for loop 
for item in noteList: 
    note, octave = getNoteOctave(item[0])
    drawingObj = shapes.createShape(note, octave, item[1], item[2], screen = screen)
    drawingObj.draw()







 




