# calculate the n'th root of p

from sys import argv, exit

epsilon = .0000000001   # something tiny
error = 1               # something un-tiny

# get number from command line
if len(argv) < 3:
 exit('usage: '+argv[0]+' number root')

else:
# order of magnitude for seed guess
 p = float(argv[1])
 n = float(argv[2]) # take the n'th root of p
 remainder = p
 orderOfMagnitude = 1
 while remainder >= 10:
          remainder = remainder/10
          orderOfMagnitude += 1

 orderOfMagnitude /= n
 guess = 10**orderOfMagnitude

# calculate sqrt() 
 while error > epsilon:
          guess = ((n-1)/n)*guess + (p/n)/guess**(n-1)
          error = abs(p-guess**n)

 print '\n',guess, guess**n,'\n'
