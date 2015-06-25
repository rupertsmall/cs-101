# find the square root of a number

from sys import argv, exit

epsilon = .0000000001   # something tiny
error = 1               # something un-tiny

# get number from command line
if len(argv) < 2:
 exit('usage: '+argv[0]+' number')

else:
# order of magnitude for seed guess
 p = float(argv[1])
 remainder = p
 orderOfMagnitude = 1
 while remainder >= 10:
          remainder = remainder/10
          orderOfMagnitude += 1

 orderOfMagnitude /= 2
 guess = 10**orderOfMagnitude

# calculate sqrt() 
 while error > epsilon:
          guess = .5*guess + .5*p/guess
          error = abs(p-guess**2)

 print '\n',guess, guess**2,'\n'
