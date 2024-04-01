import turtle

turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(2)

# Function to draw a snowflake


def draw_snowflake_side(size, depth):
    if depth == 0:
        turtle.forward(size)
    else:
        size /= 3.0
        draw_snowflake_side(size, depth-1)
        turtle.left(60)
        draw_snowflake_side(size, depth-1)
        turtle.right(120)
        draw_snowflake_side(size, depth-1)
        turtle.left(60)
        draw_snowflake_side(size, depth-1)


def draw_snowflake(size, depth):
    turtle.color('white')
    for _ in range(3):
        draw_snowflake_side(size, depth)
        turtle.right(120)

# Function to draw a geometric pattern


def draw_geometric_pattern(sides, size, repetitions):
    for _ in range(repetitions):
        for _ in range(sides):
            turtle.forward(size)
            turtle.right(360 / sides)
        size += 10
        turtle.right(360 / repetitions)

# Function to draw a colorful spiral


def draw_colorful_spiral():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for i in range(360):
        turtle.pencolor(colors[i % len(colors)])
        turtle.forward(i)
        turtle.right(59)


# Position the turtle at a good starting point for each design
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

# Draw a snowflake with depth 4
draw_snowflake(300, 4)

# Position the turtle for the next design
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()

# Draw a geometric pattern with 7 sides, starting size 50, and 15 repetitions
draw_geometric_pattern(7, 50, 15)

# Position the turtle for the last design
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

# Draw a colorful spiral pattern
draw_colorful_spiral()

turtle.done()
