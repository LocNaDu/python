"""
Author: Nguyen Van Loc
Date: 11/09/2021

Program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle.

"""
# Input lengths of the triangle sides:

x = int(input("x: "))

y = int(input("y: "))

z = int(input("z: "))

if (x**2) + (y**2) == z**2:
    print("Right-angled")
else:
    print("Not right-angled")