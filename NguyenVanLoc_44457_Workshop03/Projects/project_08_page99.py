"""
Author: Nguyen Van Loc
Date: 19/09/2021

program that lets the user enter two integers and then prints each
step in the process of using the Euclidean algorithm to find their GCD

"""

# Request the inputs
a=int(input('A  \n'))
b=int(input('B  \n'))

# Compute total population
def gcd(m,n):
    z=abs(m-n)
    if (m-n)==0:
        return n
    else:
        return gcd(z,min(m,n))

# Display the results
print(gcd(a,b))