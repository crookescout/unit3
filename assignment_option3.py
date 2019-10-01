# Scout Crooke, 10/1/19, This program draws a hexagon flower

import turtle


def get_side_length():
    return float(input("What is the length of a side of the hexagon?"))


def get_center_color():
    return input("What is the color of the center of the flower?")


def get_petal_color():
    return input("What is the color of the flower petal?")


def make_hexagon(color, length):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(length)
        turtle.left(60)
    turtle.end_fill()


def make_petals(color, length):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(6):
        turtle.fd(length)
        turtle.left(60)
    turtle.end_fill()


def main():
    length = get_side_length()
    center = get_center_color()
    get_petal_color()
    make_hexagon(center, length)


main()

turtle.exitonclick()