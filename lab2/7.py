import turtle


def draw_triangle(t, points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()


def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def fractal_mountain(t, points, depth):
    if depth == 0:
        # Выбираем цвет в зависимости от высоты
        avg_y = (points[0][1] + points[1][1] + points[2][1]) / 3
        if avg_y > 100:
            color = "white"
        else:
            color = "gray"
        draw_triangle(t, points, color)
    else:
        # Находим середины сторон
        mid1 = get_mid(points[0], points[1])
        mid2 = get_mid(points[1], points[2])
        mid3 = get_mid(points[2], points[0])

        # Рекурсивно рисуем 4 меньших треугольника
        fractal_mountain(t, [points[0], mid1, mid3], depth - 1)
        fractal_mountain(t, [points[1], mid1, mid2], depth - 1)
        fractal_mountain(t, [points[2], mid2, mid3], depth - 1)
        fractal_mountain(t, [mid1, mid2, mid3], depth - 1)


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)

    # Начальный большой треугольник (основание горы)
    base_points = [(-300, -200), (300, -200), (0, 200)]

    # Рисуем фрактальные горы (без смещения)
    fractal_mountain(t, base_points, depth=4)

    t.hideturtle()
    screen.exitonclick()


if __name__ == "__main__":
    main()