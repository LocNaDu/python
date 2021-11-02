"""
Author: Nguyen Van Loc
Date: 05/09/2021

Convert kilometers to nautical miles.

   1 kilometer = 1/10000 of the distance between the north pole and the equator
   there are 90 degrees between the north pole and the equator
   1 degree = 60 minutes of arc
   1 nautical mile = minute of arc

"""

# Request the inputs
klicks = float(input("Enter the number of kilometer:"))

# Compute the input
nauts = klicks * 90 * 60 / 10000.0

# Display the results
print("the number of nautical miles is", nauts)


