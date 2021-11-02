"""
Author: Nguyen Van Loc
Date: 04/09/2021
Problem: calculate the surface area of a cube

the input is the cube's edge.
the output is the surface area of the cube.
"""

# Request the inputs
edge = float(input("Enter the cube's edge:"))

# Compute the surface area
surfaceArea = edge * edge * 6

# Display the surface area
print("the surface area is", surfaceArea,"square units.")
