from graph import *
penColor("black")
penSize(2)
brushColor("yellow")
circle(200, 200, 100)

brushColor("red")
circle(160, 180, 25)
circle(240, 180, 20)
brushColor("black")
circle(160, 180, 10)
circle(240, 180, 10)
rectangle(260, 260, 140, 240)
polygon([(100,100), (190,170), (200,160),
         (110,90), (100,100)])
polygon([(210,170), (200,160), (280,120),
         (290,130), (210,170)])
run()