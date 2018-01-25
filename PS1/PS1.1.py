# Alex Karacaoglu
# Randomness and Computation
# Problem Set 1
# Due January 17

#1

# I am making the list of length 100000 of random floats from [0,1), then transforming
# the list by doing square root to all the elements. I then make a histogram
# that shows the distribution of these values. I use 50 bins. To run,
# click run module and the type: go() and hit enter, the plot should then be plotted
# and appear and correspond to the info created in the list

import random
import matplotlib.pyplot 

def squareRoot(i):
    return i**(1/2.0)

def go():
    random_list = [random.random() for i in range(10 ** 5)]
    finalList = [squareRoot(i) for i in random_list]

    matplotlib.pyplot.hist(finalList,50)
    matplotlib.pyplot.title("Histogram for Homework 1, Problem 1")
    matplotlib.pyplot.xlabel("Value")
    matplotlib.pyplot.ylabel("Frequency")

    matplotlib.pyplot.show()





