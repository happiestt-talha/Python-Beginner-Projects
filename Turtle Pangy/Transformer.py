import turtle

turtle.setup(600, 600)

t = turtle.Pen()

t.hideturtle()


def askIntegerInput():
    correctInput = False
    number = 0
    while not correctInput:
        try:
            number = int(input("Enter an integer number: "))
            correctInput = True
        except ValueError:
            print('Error, please enter an integer number.')
    return number


exitProgram = False

while not exitProgram:
    print("1. Option 1: Translation")
    print("2. Option 2: Rotation")
    print("3. Option 3: Scaling")
    print("4. Exit")

    print("Choose an option from the menu:")

    option = askIntegerInput()
    t.clear()

    if option == 1:
        print("1. Draw a Line")
        print("2. Draw a Square")
        shapeOption = askIntegerInput()
        t.clear()

        if shapeOption == 1:
            print("Line")
            length = int(input("Enter the length of the line: "))

            t.forward(length)

            xTranslation = int(input("Translation in X direction: "))
            yTranslation = int(input("Translation in Y direction: "))

            t.penup()
            t.goto(xTranslation, yTranslation)
            t.pendown()

            t.color("blue")
            t.forward(length)

            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.color("black")

        elif shapeOption == 2:
            print("Square")
            sideLength = int(input("Enter the side length of the square: "))

            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)

            xTranslation = int(input("Translation in X direction: "))
            yTranslation = int(input("Translation in Y direction: "))

            t.penup()
            t.goto(xTranslation, yTranslation)
            t.pendown()

            t.color("blue")
            t.backward(sideLength)
            t.right(90)
            t.backward(sideLength)
            t.right(90)
            t.backward(sideLength)
            t.right(90)
            t.backward(sideLength)

            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.color("black")

        print("")

    elif option == 2:
        print("1. Draw a Line")
        print("2. Draw a Square")
        shapeOption = askIntegerInput()
        t.clear()

        if shapeOption == 1:
            print("Line")
            length = int(input("Enter the length of the line: "))

            t.forward(length)

            rotationAngle = int(input("Rotation angle in degrees: "))

            t.penup()
            t.goto(0, 0)
            t.left(rotationAngle)
            t.color("magenta")
            t.pendown()

            t.forward(length)

            t.penup()
            t.right(rotationAngle)
            t.goto(0, 0)
            t.pendown()
            t.color("black")

        elif shapeOption == 2:
            print("Square")
            sideLength = int(input("Enter the side length of the square: "))

            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)

            rotationAngle = int(input("Rotation angle in degrees: "))

            t.penup()
            t.goto(0, 0)
            t.left(rotationAngle)
            t.color("magenta")
            t.pendown()

            t.backward(sideLength)
            t.right(90)
            t.backward(sideLength)
            t.right(90)
            t.backward(sideLength)
            t.right(90)
            t.backward(sideLength)

            t.penup()
            t.right(rotationAngle)
            t.goto(0, 0)
            t.pendown()
            t.color("black")

        print("")

    elif option == 3:
        print("1. Draw a Line")
        print("2. Draw a Square")
        shapeOption = askIntegerInput()
        t.clear()

        if shapeOption == 1:
            print("Line")
            length = float(input("Enter the length of the line: "))

            t.forward(length)

            scalingFactor = float(input("Scaling factor: "))

            t.penup()
            t.goto(0, 0)
            t.pendown()

            t.color("red")
            t.forward(length * scalingFactor)

            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.color("black")

        elif shapeOption == 2:
            print("Square")
            sideLength = int(input("Enter the side length of the square: "))

            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)
            t.left(90)
            t.forward(sideLength)

            scalingFactor = float(input("Scaling factor: "))

            t.penup()
            t.goto(0, 0)
            t.color("red")
            t.pendown()

            t.backward(sideLength * scalingFactor)
            t.right(90)
            t.backward(sideLength * scalingFactor)
            t.right(90)
            t.backward(sideLength * scalingFactor)
            t.right(90)
            t.backward(sideLength * scalingFactor)

            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.color("black")

        print("")

    elif option == 4:
        exitProgram = True
    else:
        print("Please enter a number between 1 and 4.")

print("End")
