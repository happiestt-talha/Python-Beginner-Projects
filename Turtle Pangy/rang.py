import turtle

turtle.bgcolor('black')
turtle.speed(20)
turtle.pensize(2)


def draw_colorful_spiral():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for i in range(400):
        turtle.pencolor(colors[i % len(colors)])
        turtle.forward(i)
        turtle.right(59)


# Draw the colorful spiral pattern
draw_colorful_spiral()

turtle.done()
