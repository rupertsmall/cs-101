from sys import argv, exit
from math import pi, sin

# get number from command line
if len(argv) < 2:
 exit('usage: '+argv[0]+' number')

else:
# calculate sin
 save = argv[1]                 # save for later
 X = float(save)
 X %= 2*pi
 if X > pi:
        X = -X + pi
 elif X < -pi:
        X = -X - pi
 print 'delta: ', X
 sinX = X - X**3/6 + X**5/120 - X**7/5040 + X**9/362880 - X**11/39916800
 print 'approx sin(%s): %f' % (save, sinX)
 print 'actual sin(%s): %f' % (save, sin(X))
