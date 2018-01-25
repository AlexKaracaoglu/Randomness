#Alex Karacaoglu

import random
import matplotlib.pyplot as plt
import math
import numpy

# 1c
def phi_1c(u):
    return math.ceil(-math.log(1-u,2))
samples1c = [phi_1c(random.random()) for i in range(10**6)]

# 1d
def get_expected():  
    expected = 0
    i = 0
    while i < 100:
        sample = samples1c
        expected = expected + numpy.mean(sample)
        i = i + 1
    return expected
def get_variance():
    variance = 0
    i = 0
    while i < 100:
        sample = samples1c
        variance = variance + numpy.var(sample)
        i = i + 1
    return variance

# 3c
def phi_3c(u):
    return ((9. * u)**.5) + 3.
samples3c = [phi_3c(random.random()) for i in range(10**6)]

# In order to test them, change the sample spot in the hist function to be the desired
# sample, either samples1c or samples3c. Then uncomment the last 2 lines.
# Also, in order to answer 1d, I made functions get_expected and get_variance
# So if you want to test these you can, and the output should be close to 200 as expected

#plt.hist(samples3c,bins=100,normed=True)
#plt.show()
