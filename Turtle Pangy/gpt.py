import turtle
import math

t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(10)


def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.pensize(2)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_lines(x, y, radius, num_lines, color):
    angle_increment = 360 / num_lines
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(2)
    t.pencolor(color)

    for _ in range(num_lines):
        t.forward(radius)
        t.backward(radius)
        t.left(angle_increment)


if __name__ == '__main__':
    colors = ['crimson', 'snow', 'blue', 'lime', 'gold']
    radius = 200
    num_lines = 12

    for i in range(5):
        draw_circle(0, 0, radius - i * 40, colors[i])

    draw_lines(0, 0, radius - 40 * 4, num_lines, 'white')

    turtle.done()
