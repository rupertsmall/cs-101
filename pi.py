# calculate pi

from math import sin, cos, sqrt

epsilon = 0.00000001
error = 1
guess = 1.0     # seed guess for pi/4

while error > epsilon:
        guess = guess - (sin(guess) - 1/(sqrt(2)))/cos(guess)
        error = abs(sin(guess) - (1/sqrt(2)))

# root is pi/4 so multiply by 4 to get pi
print guess, guess*4
