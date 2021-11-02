"""
Author: Nguyen Van Loc
Date: 19/09/2021

program that takes the purchase price as input

"""
import random

def playRound(budget: int) -> tuple:
    sum = sumOfDice(random.randint(1,6), random.randint(1,6))
    if sum == 7:
        budget += 4
        return ("Win",budget)
    else:
        budget -= 1
        return ("Loss",budget)

def sumOfDice(die1: int, die2: int) -> int:
        return die1 + die2

def haveMoney(budget: int) -> bool:
    # This is a ternary expression it is an if statement in one line
    #     Truthy   Expression      Falsy
    return True if budget > 0 else False

def main():
    numRolls = 0
    outputString = "\t{0}\t\t{1}\t\t{2}"

    # To prevent a type error, the string is explicitly converted to int
    budget = int(input("How much do you want to add:"))

    # \t is the metacharacter representing a tab
    print("Number of rolls\t\tWin or Loss\tCurrent value of the pot")

    print(outputString.format(numRolls, "Put", budget))

    # The return value is a boolean type, thus the output is the expression
    while haveMoney(budget):
        # Python does not support the pre-increment or post-crement operator
        numRolls += 1
        output = playRound(budget)
        budget = output[1]
        print(outputString.format(numRolls, output[0], output[1]))

    print("Sorry you're out of money")

# Entry point for a Python program
if __name__ == "__main__":
    main()
    # Your solution works but it does not need a dedicated funct
    while True:
        userIn = input("Would you like to play again?")
        if 'yes' == userIn:
            main()
        else:
            print("Goodbye")
            break