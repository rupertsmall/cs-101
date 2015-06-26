# find the factorial of n

from sys import argv, exit

#define factorial function
def factorial(n):
        if n==1:
                return n
        else:
                return n*factorial(n-1)

# get number from command line get factorial
if len(argv) < 2:
        exit('usage: '+argv[0]+' integer')

else:
        n = abs(int(round(float(argv[1]))))
        print factorial(n)
