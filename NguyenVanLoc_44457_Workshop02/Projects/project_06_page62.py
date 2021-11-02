"""
Author: Nguyen Van Loc
Date: 05/09/2021

Given an object's mass and velocity, compute its momentum and kinetic energy.

"""

# Request the inputs
mass = float(input("Enter the object's mass:"))
velocity = float(input("Enter the object's velocity:"))

# Compute the results
momentus = mass * velocity
kineticEnergy = (mass * velocity ** 2)/2

# Display the results
print("the object's momentum is", momentus)
print("the object's kinetic energy is", kineticEnergy)
