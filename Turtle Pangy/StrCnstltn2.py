import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("midnightblue")  # Background color

# Create the turtle
star_turtle = turtle.Turtle()
star_turtle.speed(1)
star_turtle.color("white")

# Draw stars in the constellation


def draw_star(x, y):
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    for _ in range(5):
        star_turtle.forward(20)
        star_turtle.right(144)


# Draw the constellation
stars_coordinates = [(0, 0), (100, 150), (-120, 200), (-70, 50), (150, -100)]
for x, y in stars_coordinates:
    draw_star(x, y)

# Hide the turtle
star_turtle.hideturtle()

# Keep the window open until it's manually closed
turtle.done()
