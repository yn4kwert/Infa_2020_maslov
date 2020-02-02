from graph import *
#import Tkinter as tk
size_x=700
size_y=1000
windowSize(size_x, size_y)
canvasSize(size_x, size_y)

def fance(x,y,scale):
    N = 12
    penColor('black')
    penSize(2)
    brushColor(238, 197, 145)
    rectangle(x, y, x+500*scale, y+300*scale)
    h = (500*scale) / (N + 1)
    step = x + h
    for i in range(N):
        line(step, y, step, y+300*scale)
        step += h

def booth(x,y,scale):
    penColor('black')
    penSize(2)
    brushColor("brown")
    polygon([(x, y+80*scale),
             (x+90*scale, y+95*scale),
             (x+55*scale, y+20*scale),
             (x, y+80*scale)
             ])
    polygon([(x+90*scale, y+95*scale),
             (x+120*scale, y+70*scale),
             (x+85*scale, y),
             (x+55*scale, y+20*scale),
             (x+90*scale, y+95*scale)])
    brushColor(205, 155, 29)
    polygon([(x+90*scale, y+95*scale),
             (x+120*scale, y+70*scale),
             (x+120*scale, y+150*scale),
             (x+90*scale, y+175*scale),
             (x+90*scale, y+95*scale)
             ])
    polygon([(x+90*scale, y+95*scale),
             (x+90*scale, y+175*scale),
             (x, y+160*scale),
             (x, y+80*scale),
             (x+90*scale, y+95*scale)
             ])
    brushColor("black")
    circle(x+40*scale, y+125*scale, 25*scale)

def dog(x,y,scale,orientation):
    brushColor("gray")
    penColor('gray')
    oval(x, y+110*scale, x+30*scale*orientation, y+120*scale)
    oval(x+50*scale*orientation, y+130*scale, x+80*scale*orientation, y+140*scale)
    oval(x+10*scale*orientation, y+50*scale, x+35*scale*orientation, y+110*scale)
    oval(x+60*scale*orientation, y+70*scale, x+85*scale*orientation, y+130*scale)
    oval(x+20*scale*orientation, y+30*scale, x+120*scale*orientation, y+80*scale)
    oval(x+90*scale*orientation, y+20*scale, x+130*scale*orientation, y+60*scale)
    oval(x+120*scale*orientation, y+40*scale, x+150*scale*orientation, y+80*scale)
    oval(x+100*scale*orientation, y+20*scale, x+150*scale*orientation, y+60*scale)
    oval(x+110*scale*orientation, y+60*scale, x+120*scale*orientation, y+100*scale)
    oval(x+98*scale*orientation, y+98*scale, x+118*scale*orientation, y+108*scale)
    oval(x+140*scale*orientation, y+70*scale, x+150*scale*orientation, y+110*scale)
    oval(x+130*scale*orientation, y+105*scale, x+150*scale*orientation, y+115*scale)
    penColor('black')
    penSize(1)
    rectangle(x+10*scale*orientation, y, x+70*scale*orientation, y+60*scale)
    oval(x, y, x+20*scale*orientation, y+25*scale)
    oval(x+60*scale*orientation, y, x+80*scale*orientation,  y+25*scale)
    arc(x+20*scale*orientation,  y+40*scale, x+60*scale*orientation,  y+70*scale, 0, 180, ARC)
    brushColor("white")
    oval(x+25*scale*orientation,  y+20*scale, x+35*scale*orientation, y+25*scale)
    oval(x+45*scale*orientation, y+20*scale, x+55*scale*orientation, y+25*scale)
    polygon([(x+25*scale*orientation, y+45*scale),
             (x+27*scale*orientation, y+35*scale),
             (x+29*scale*orientation, y+42*scale),
             (x+25*scale*orientation, y+45*scale)
             ])
    polygon([(x+55*scale*orientation, y+45*scale),
             (x+53*scale*orientation, y+35*scale),
             (x+51*scale*orientation, y+42*scale),
             (x+55*scale*orientation, y+45*scale)
             ])
    brushColor("black")
    circle(x+30*scale*orientation, y+22*scale, 2*scale)
    circle(x+50*scale*orientation, y+22*scale, 2*scale)

brushColor('cyan')
rectangle (0, 0, size_x, 200)
brushColor('green')
rectangle (0, 500, size_x, size_y)
fance(200,50,1.32)
fance(0,200,1)
fance(0,300,0.8)
fance(480,300,0.8)

booth(50,480,0.7)
booth(350,480,0.7)
booth(520,550,1.3)

dog(30,560,1,1)
dog(400,570,1.1,-1)
dog(250,700,1.4,-1)
dog(500,800,3,1)
run()