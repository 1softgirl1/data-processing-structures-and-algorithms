import random
import turtle


def tree1(branchLen, t):
    if branchLen > 5:  # базовый случай - остановка рекурсии
        if branchLen > 30:
            t.pensize(branchLen / 10)  # толстые ствол и основные ветки
            t.color("brown")  # ствол и толстые ветки - коричневые
        elif branchLen > 15:
            t.pensize(3)  # средние ветки
            t.color("peru")  # тонкие ветки - светло-коричневые
        else:
            t.pensize(2)  # тонкие веточки
            t.color("green")  # самые короткие - зеленые листья

        t.forward(branchLen)
        t.right(20)
        tree1(branchLen - 15, t)
        t.left(40)
        tree1(branchLen - 15, t)
        t.right(20)

        # Возвращаемся назад с теми же настройками пера
        if branchLen > 30:
            t.color("brown")
            t.pensize(branchLen / 10)
        elif branchLen > 15:
            t.color("peru")
            t.pensize(3)
        else:
            t.color("green")
            t.pensize(2)

        t.backward(branchLen)  # возвращаемся к началу ветки


def tree2(branchLen, t):
    if branchLen > 5:
        if branchLen > 30:
            t.pensize(branchLen / 10)
            t.color("brown")
        elif branchLen > 15:
            t.pensize(3)
            t.color("peru")
        else:
            t.pensize(2)
            t.color("green")

        t.forward(branchLen)
        right_angle = random.randint(15, 45)
        t.right(right_angle)
        tree3(branchLen - 15, t)  # рекурсивно рисуем правую ветку
        left_angle = random.randint(15, 45)
        t.left(left_angle)
        tree3(branchLen - 15, t)  # рекурсивно рисуем левую ветку
        t.right(left_angle - right_angle)  # Возвращаемся к исходному направлению

        # Возвращаемся назад с теми же настройками пера
        if branchLen > 30:
            t.color("brown")
            t.pensize(branchLen / 10)
        elif branchLen > 15:
            t.color("peru")
            t.pensize(3)
        else:
            t.color("green")
            t.pensize(2)

        t.backward(branchLen)

def tree3(branchLen, t):
     if branchLen > 5:
         if branchLen > 30:
             t.pensize(branchLen / 10)
             t.color("brown")
         elif branchLen > 15:
             t.pensize(3)
             t.color("peru")
         else:
             t.pensize(2)
             t.color("green")


         t.forward(branchLen)
         right_angle = random.randint(15, 45)
         t.right(right_angle)
         tree2(branchLen - random.randint(10, 20), t)  # рекурсивно рисуем правую ветку
         left_angle = random.randint(15, 45)
         t.left(left_angle)
         tree2(branchLen - random.randint(10, 20), t)  # рекурсивно рисуем левую ветку
         t.right(left_angle - right_angle) # Возвращаемся к исходному направлению

         # Возвращаемся назад с теми же настройками пера
         if branchLen > 30:
             t.color("brown")
             t.pensize(branchLen / 10)
         elif branchLen > 15:
             t.color("peru")
             t.pensize(3)
         else:
             t.color("green")
             t.pensize(2)

         t.backward(branchLen) # возвращаемся к началу ветки


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)

    # Первое дерево (симметричное)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    tree1(75, t)

    # Второе дерево (случайные углы)
    t.up()
    t.right(90)
    t.forward(200)
    t.left(90)
    t.down()
    tree2(75, t)

    # Третье дерево (случайные углы и длины)
    t.up()
    t.right(90)
    t.forward(-400)
    t.left(90)
    t.down()
    tree3(75, t)

    t.hideturtle()
    myWin.exitonclick()



main()