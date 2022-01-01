import turtle

turtle.bgcolor('black')
turtle.speed(7)
turtle.pensize(2)
turtle.pencolor('blue')

def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4

def design():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)

design()
turtle.done()