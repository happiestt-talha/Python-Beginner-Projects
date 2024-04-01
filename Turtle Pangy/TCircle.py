import turtle

turtle.bgcolor('cyan')
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor('green')


def drawcircle(radius):
    for i in range(15):
        turtle.circle(radius)
        radius -= 4  # Decrease the radius to create a spiral effect


def drawdesign():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)


drawdesign()
turtle.done()
