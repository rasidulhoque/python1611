import turtle

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)


def draw_circles(size):
    turtle.pencolor('red')
    turtle.circle(size)
    draw_circles(size + 5)

draw_circles(30)    