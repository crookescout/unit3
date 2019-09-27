#  Scout Crooke, 9/26/19,  this program calculates the area of a triangle given the length of its three sides

import math

side_a = float(input("What is the length of side a?"))
side_b = float(input("What is the length of side b?"))
side_c = float(input("What is the length of side c?"))


def area_of_triangle():
    s = (side_a + side_b + side_c) / 2
    a = math.sqrt(s * (s - side_a) * (s - side_b ) * (s - side_c))
    print("The area of a triangle with side lengths", str(side_a) + ",", str(side_b) + ",", "and", str(side_c), "equals", a)


area_of_triangle()
