"""
Author: Nguyen Van Loc
Date: 11/09/2021

program displays the total population

One might start with a population of 500 organisms, a growth rate of 2,
and a growth period to achieve this rate of 6 hours after allowing 6 hours for growth,
we would have 1000 organisms, and after 12 hours, we would have 2000 organisms.

"""

# Request the inputs
organisms = int(input("Enter the initial number of organisms:"))
rateOfGrowth = int(input("Enter the rate of growth : "))
numOfhours = int(input("Enter the number of hours to achieve the rate of growth: "))
totalhours = int(input("Enter the total hours of growth: "))
hours=0
# Compute total population
while (hours <= totalhours):
    organisms*=rateOfGrowth
    hours += numOfhours
    if (hours==totalhours):
        break
# Display the results
print("The total population:" ,organisms)