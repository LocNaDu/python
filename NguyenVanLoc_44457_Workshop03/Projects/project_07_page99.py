"""
Author: Nguyen Van Loc
Date: 19/09/2021

program that displays a salary schedule

"""

# Request the inputs
startSalary = int(input("Please enter beginning salary: "))
percentIncrease = (float(input("Please enter percentage increase: ")) / 100)
numberYears = list(range(1,(int(input("Please enter number of years in schedule: ")) + 1)))

# Compute total population
def calculateSalary(startSalary, percentIncrease, numberYears):
  for year in numberYears:

    salaryInc = startSalary*percentIncrease
    newSalary = startSalary+salaryInc
    startSalary = newSalary
    print("{} year salary is  {:0.2f}".format(year, newSalary))

# Display the results
calculateSalary(startSalary, percentIncrease, numberYears)
