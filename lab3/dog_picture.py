from graph import *
#import Tkinter as tk

x1 = 0; y1 = 100
x2 = 500; y2 = 300
N=12
brushColor(	238, 197, 145)
rectangle (x1, y1, x2, y2)
brushColor('cyan')
rectangle (0, 0, x2, y1)
brushColor('green')
rectangle (0, y2, x2, 1000)
h = (x2 - x1) / (N + 1)
x = x1 + h
for i in range (N):
    line(x, y1, x, y2)
    x += h
penColor('black')
penSize(2)
brushColor("brown")
polygon([(300,320), (390,335),
         (355,260), (300,320)])
polygon([(390,335), (420,310),(385,240),
         (355,260), (390,335)])
brushColor(	205, 155, 29)
polygon([(390,335), (420,310),(420,390),
         (390,415), (390,335)])
polygon([(390,335), (390,415), (300,400),(300,320),
         (390,335)])
brushColor("black")
circle(340, 365, 25)
brushColor("gray")
penColor('gray')
oval(50,450,80,460)
oval(100,470,130,480)
oval(60,390,85,450)
oval(110,410,135,470)
oval(70,370,170,420)
oval(140,360,180,400)
oval(170,380,200,420)
oval(150,360,200,400)
oval(160,400,170,440)
oval(148,438,168,448)
oval(190,410,200,450)
oval(180,445,200,455)
penColor('black')
penSize(1)
rectangle (60,340,120,400)
oval(50,340,70,365)
oval(110,340,130,365)
arc(70, 380, 110, 410, 0, 180, ARC)
brushColor("white")
oval(75,360,85,365)
oval(95,360,105,365)
polygon([(75,385), (77,375), (79,382),
         (75,385)])
polygon([(105,385), (103,375), (101,382),
         (105,385)])
brushColor("black")
circle(80,362,2)
circle(100,362,2)


run()