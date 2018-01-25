# Alex Karacaoglu
# Randomness and Computation
# Problem Set 1
# Due January 17

#2

# I wrote an isPeak function that checks to see if a random 3-tuple is a peak.
# I then caluclate the number of peaks, and make a fraction that shows the amount
# of peaks over the total 1000000 3-tuples in the list. To run, do the same as
# problem 1: run the module and the type: go()    and hit enter

import random
from fractions import Fraction

def isPeak((a,b,c)):
    if (a < b) and (b > c):
        return(True)
    else:
        return(False)

def go():
    values = [1,2,3,4,5,6]
    peaks = [(random.choice(values),random.choice(values),random.choice(values))  for i in range(10 ** 6)]    

    numberOfPeaks = [i for i in peaks if isPeak(i)]
    x = len(numberOfPeaks)
    y = len(peaks)
    print 'The amount of peaks in this simulation is: ' + str(x) + '/' + str(y)
    z = float(x)/y
    print "And this is equivalent to: " + str(z)
    print "Feel free to run another simulation, the values will be a bit differet, but will stay in the same ballpark"



        
    
   

    
    
    

