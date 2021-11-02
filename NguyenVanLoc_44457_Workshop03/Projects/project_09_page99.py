"""
Author: Nguyen Van Loc
Date: 19/09/2021

Program providing inputs

"""
data = input("Enter a number or press Enter to quit: ")
numbers = []

while True:
    #request input from user
    data = input("Enter a number or press Enter to quit: ")

    #set up the termination condition
    if data == "":
        break

    #convert inputs into floats
    numbers.append(float(data))

# these can all be done outside and after the while loop
count = len(numbers)
if count > 0:
    _sum = sum(numbers)
    product = 1.0
    for n in numbers:
        product *= n
    average = _sum / float(count)

    #display results
    print("The sum is", _sum)
    print("The product is", product)
    print("The average is", average)
else:
    print("Nothing was entered")