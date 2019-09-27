#  Scout Crooke, 9/26/19, this program uses letters to spell MISSISSIPPI

import turtle
turtle.speed(0)
turtle.pencolor("purple")
turtle.pensize(2)

turtle.penup()
turtle.back(300)
turtle.pendown()


def make_m():
    turtle.left(90)
    turtle.fd(100)
    turtle.right(120)
    turtle.fd(50)
    turtle.left(60)
    turtle.fd(50)
    turtle.right(120)
    turtle.fd(100)


make_m()

turtle.penup()
turtle.left(90)
turtle.forward(10)
turtle.pendown()


def make_i():
    turtle.fd(28)
    turtle.left(180)
    turtle.fd(14)
    turtle.right(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(14)
    turtle.left(180)
    turtle.fd(28)


make_i()

turtle.penup()
turtle.forward(80)
turtle.pendown()



def make_s():
    turtle.left(140)
    turtle.fd(30)
    turtle.left(80)
    turtle.fd(30)
    turtle.left(50)
    turtle.fd(40)
    turtle.left(70)
    turtle.fd(45)
    turtle.right(70)
    turtle.fd(40)
    turtle.right(65)
    turtle.fd(30)
    turtle.right(55)
    turtle.fd(30)


make_s()

turtle.penup()
turtle.right(90)
turtle.fd(100)
turtle.right(50)
turtle.pendown()

make_s()


turtle.exitonclick()
