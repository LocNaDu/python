"""
Author: Nguyen Van Loc
Date: 04/09/2021

Problem: calculate the total charge for a customer’s video rentals.

New video rental =$3.00
Oldie rental =$2.00
"""
# Initialize the constants
NEW_RENTAL = 3.00
OLDIE_RENTAL = 2.00

# Request the inputs
newOnes = int(input("Enter the number of new videos:"))
oldOnes = int(input("Enter the number of oldies:"))

# Compute the results
totalCost = NEW_RENTAL * newOnes * OLDIE_RENTAL * oldOnes

# Display the results
print("the total cost is $" + str(round(totalCost, 2)))
