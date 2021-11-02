"""
Author: Nguyen Van Loc
Date: 11/09/2021

Modify the guessing-game program of Section 3.5 so that the user thinks of a number that the computer must guess.
The computer must make no more than the minimum number of guesses,
and it must prevent the user from cheating by entering misleading hints.
Hint:
Use the math.log function to compute the minimum number of guesses needed after the lower and upper bounds are entered.

"""

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
maxattempt = (larger - smaller)

count = 0
guess = int((smaller + larger) / 2)
while count != maxattempt:
    count += 1
    guess = int((smaller + larger) / 2)
    print(smaller, larger)
    print("Your number is: ", guess)
    hlp = input("Enter =, <, or >: ")
    if hlp == '>':
        smaller = guess + 1
    elif hlp == '<':
        larger = guess - 1
    elif hlp == '=':
        print("Congratulations! You've got it in", count, "tries!")
        break
else:
    print("I'm out of guesses")

