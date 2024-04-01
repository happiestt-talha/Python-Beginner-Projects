import turtle
import my_gar

# Named constants
X1 = 0
Y1 = 100
X2 = -100
Y2 = -100
X3 = 100
Y3 = -100
RADIUS = 50


def main():
    turtle.hideturtle()


# Draw a square.
my_gar.square(X2, Y2, (X3 - X2), 'gray')

# Draw some circles.
my_gar.circle(X1, Y1, RADIUS, 'blue')
my_gar.circle(X2, Y2, RADIUS, 'red')
my_gar.circle(X3, Y3, RADIUS, 'green')

# Draw some lines.
my_gar.line(X1, Y1, X2, Y2, 'black')
my_gar.line(X1, Y1, X3, Y3, 'black')
my_gar.line(X2, Y2, X3, Y3, 'black')

# Call the main function.
if __name__ == '__main__':
    main()

turtle.done()
