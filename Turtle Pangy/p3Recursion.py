import turtle as t
t.bgcolor('black')
t.color('cyan')

# position turtle to left side by goto function
t.penup()
t.goto(-200, -200)
t.pendown()


def drew(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

    # t.goto(-200, -200)
    if size > 5:
        drew(size*0.75)


def hyp(size2):
    t.forward(size2)
    t.left(90)

    # t.goto(-200, -200)
    if size2 > 5:
        hyp(size2-5)


drew(150)
t.penup()
t.goto(0, 0)
t.pendown()
hyp(200)


t.done()
