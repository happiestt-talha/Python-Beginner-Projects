import turtle

turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(2)

# Function to draw a star


def draw_star(size):
    turtle.color('yellow')
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

# Function to draw a flower


def draw_flower(petals):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for i in range(petals):
        turtle.color(colors[i % len(colors)])
        turtle.circle(100)
        turtle.right(360 / petals)

# Function to draw a spiral


def draw_spiral():
    colors = ['cyan', 'magenta', 'yellow', 'white']
    for i in range(360):
        turtle.pencolor(colors[i % len(colors)])
        turtle.forward(i)
        turtle.left(59)


# Position the turtle at a good starting point
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

# Draw a star
draw_star(150)

# Position the turtle for the next shape
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()

# Draw a flower with 6 petals
draw_flower(6)

# Position the turtle for the last shape
turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()

# Draw a spiral pattern
draw_spiral()

turtle.done()
