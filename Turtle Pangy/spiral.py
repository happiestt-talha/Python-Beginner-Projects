import turtle
import math

t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)


def draw_flower(petals, radius, color1, color2):
    angle = 360 / petals

    for _ in range(petals):
        t.color(color1)
        t.circle(radius)
        t.color(color2)
        t.circle(radius / 2)
        t.right(180 - angle)


if __name__ == '__main__':
    t.penup()
    t.goto(0, 0)
    t.pendown()

    flower_petals = 12
    flower_radius = 100

    draw_flower(flower_petals, flower_radius, 'red', 'yellow')

    t.hideturtle()
    turtle.done()
