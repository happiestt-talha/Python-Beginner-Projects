import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("midnightblue")  # Set a beautiful background color

# Create the turtle
star_turtle = turtle.Turtle()
star_turtle.speed(1)
star_turtle.color("white")

# Define the star points for the constellation
star_points = [
    (-50, 50),
    (0, 100),
    (50, 50),
    (0, 0),
    (-25, -75),
    (25, -75),
]

# Draw the stars and connect them
for point in star_points:
    star_turtle.penup()
    star_turtle.goto(point)
    star_turtle.pendown()
    star_turtle.dot(5)  # Draw a star at each point

# Connect the stars to form the constellation
star_turtle.penup()
star_turtle.goto(star_points[0])
star_turtle.pendown()
for point in star_points[1:]:
    star_turtle.goto(point)

# Hide the turtle
star_turtle.hideturtle()

# Keep the window open until the user closes it
turtle.done()
