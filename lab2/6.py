import turtle


def dragon(t, length, depth, sign=1):
    if depth == 0:
        t.forward(length)
    else:
        t.left(45 * sign)
        dragon(t, length / 1.414, depth - 1, 1)
        t.right(90 * sign)
        dragon(t, length / 1.414, depth - 1, -1)
        t.left(45 * sign)



def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(800, 600)
    t.speed(0)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    dragon(t, 200, 10)
    t.hideturtle()
    screen.exitonclick()


main()