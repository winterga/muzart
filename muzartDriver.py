import noteFinder as nf
import objectOrientedShapes as shapes
import turtle

#code for initializing screen turtle object
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(1920,1080)
screen.tracer(0)
screen.colormode(255)

muzart = nf.Muzart(file='/vanderbiltCS/SyBBURE/SU23/more-complicated-demo-song-2-both-hands.mp3')
noteList = muzart.run()




