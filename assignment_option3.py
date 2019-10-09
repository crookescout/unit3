# Scout Crooke, 10/1/19, This program draws a hexagon flower

import turtle


def get_side_length():
    """
    this function gets the length of a side of the hexagon from the user
    :return: integer value of the side length
    """
    return int(input("What is the length of a side of the hexagon?"))


def get_center_color():
    """
    this function gets the color of the center of the flower from the user
    :return: string value of the color of the center of the flower
    """
    return input("What is the color of the center of the flower?")


def get_petal_color():
    """
    this function gets the color of the flower petals from the user
    :return: string value of the color of the flower petals
    """
    return input("What is the color of the flower petal?")


def make_hexagon(color, length):
    """
    this function draws the center of the flower using the given color and length
    :param color:
    :param length:
    :return: none
    """
    turtle.color(color)
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(length)
        turtle.right(60)
    turtle.end_fill()


def make_petals(color, length):
    """
    this function draws the petal of the flower using the given color and length. It is needed because, otherwise,
    it would draw over the same hexagon over and over
    :param color:
    :param length:
    :return: none
    """
    turtle.color(color)
    turtle.begin_fill()
    for x in range(6):
        turtle.fd(length)
        turtle.left(60)
    turtle.end_fill()


def main():
    length = get_side_length()
    center = get_center_color()
    petal = get_petal_color()
    make_hexagon(center, length)
    for x in range(6):
        turtle.fd(length)
        turtle.right(60)
        make_petals(petal, length)


main()

turtle.exitonclick()