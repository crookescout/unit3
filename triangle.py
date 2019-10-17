#  Scout Crooke, 9/26/19,  this program calculates the area of a triangle given the length of its three sides

import math


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


side_a = float(input("What is the length of side a?"))
side_b = float(input("What is the length of side b?"))
side_c = float(input("What is the length of side c?"))

a = area_of_triangle(side_a, side_b, side_c)

print("The area of a triangle with side lengths", str(side_a) + ",", str(side_b) + ",", "and", str(side_c), "equals", a)
