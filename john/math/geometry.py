import math

def circle_area(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    return area

def rectangle_area(length, width):
    return length * width

def square_area(length):
    return rectangle_area(length, length)

