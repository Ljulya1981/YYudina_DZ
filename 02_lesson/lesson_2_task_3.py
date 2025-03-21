import math


def square(l_side):
    return l_side * l_side


l_side = int(input("Длина стороны квадрата: "))
print(f"Площадь квадрата: {math.ceil(square(l_side))}")
