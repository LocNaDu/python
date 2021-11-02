"""
Author: Nguyen Van Loc
Date: 11/09/2021

The German mathematician Gottfried Leibniz developed the following method to approximate the value of π:
π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .
Write a program that allows the user to specify the number of iterations
used in this approximation and that displays the resulting value.
"""

iteration = int(input("n: "))

presumm = 0
A = 1
sign = True
for i in range(iteration):
    presumm = presumm + 1 / A if sign else presumm - 1 / A
    A += 2
    sign = not sign
pi = presumm * 4

print(pi)

# n==5,   output: 3.3396825396825403
# n==10,  output: 3.0418396189294032
# n==999, output: 3.142593654340044