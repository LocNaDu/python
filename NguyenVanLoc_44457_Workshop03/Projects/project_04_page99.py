"""
Author: Nguyen Van Loc
Date: 11/09/2021

program to drop a ball see how high it bounces

If a ball dropped from a height of 10 feet bounces 6 feet high, the index is 0.6,
and the total distance traveled by the ball is 16 feet after one bounce.
If the ball were to continue bouncing, the distance after two bounces

"""
dropDistance = input("Please input the drop height :>")
bouncePercent = input("Please input the bounce percent:>")
numBounces = input("Please input the # of bounces :>")

totalDistance = 0.6

print(" bounce #   drop distance   bounce distance  total distance ")

for bounceLoop in range(1, int(numBounces) + 1):
    bouncedistance = float(bouncePercent) * float(dropDistance)

    totalDistance = float(totalDistance) + float(dropDistance) + float(bouncedistance)

    print(
        "         " + str(bounceLoop) + "  " + str(dropDistance) + "             " + str(bouncedistance) + "   " + str(
            totalDistance))

dropDistance = bouncedistance