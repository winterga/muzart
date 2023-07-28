# import noteFinder as nf
# import objectOrientedShapes as shapes
# import turtle

#code for initializing screen turtle object
# screen = turtle.Screen()
# screen.bgcolor('black')
# screen.setup(1920,1080)
# screen.tracer(0)
# screen.colormode(255)

# #extracting data from note finder file 
# muzart = nf.Muzart(file='/vanderbiltCS/SyBBURE/SU23/more-complicated-demo-song-2-both-hands.mp3')
# #array of arrays ['note', string, intensity, duration]
# noteList = muzart.run()

#part where we 

def getOctave(noteOctave): 
    if len(noteOctave) == 2: 
        return noteOctave[0], int(noteOctave[1])
    return noteOctave[0:2], int(noteOctave[2])

print(getOctave("C8"))


# #need to add noteList and put it into object oriented shapes -- for loop 
# for note in noteList: 
#     drawingObj = shapes.createShape(note[0], note[1], note[2])







 




