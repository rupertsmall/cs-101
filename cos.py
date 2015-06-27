from sys import argv, exit
from math import pi, cos

# get number from command line
if len(argv) < 2:
 exit('usage: '+argv[0]+' number')

else:
# calculate cos 
 save = argv[1]                 # save for later
 X = abs(float(save))           # take abs() because cos(X) = cos(-X)
 X %= 2*pi
 if X > pi:                     # in this case cos(X) = cos(2pi - X)
        X = 2*pi - X
 print 'delta: ', X
 cosX = 1 - X**2/2 + X**4/24 - X**6/720 + X**8/40320 - X**10/3628800
 print 'approx cos(%s): %f' % (save, cosX)
 print 'actual cos(%s): %f' % (save, cos(X))
