#Alex Karacaoglu

import random
import matplotlib.pyplot as plt

# 2:
def phi2(u):
    return (u-1)**(1./3)+1 
samples2 = [phi2(random.random()) for i in range(10**6)]
plt.hist(samples2,bins=100,normed=True)
plt.show()

#3
def phi3b(u):
    return u**(2./3) 
#samples3b = [sum([phi3b(random.random()) for i in range(100)]) for i in range(10**5)]
#plt.hist(samples3b,bins=100,normed=True)
#plt.show()

#5
def tossSequence(n):
    first = random.randint(0,1)
    listFlips = [first]
    i = 1
    previous = first
    while (i<=n):
        if previous == 0:
            rand = random.randint(1,100)
            if rand > 98:
                new = 1
            else:
                new = 0
        if previous == 1:
            rand = random.randint(1,100)
            if rand > 98:
                new = 0
            else:
                new = 1
        listFlips.append(new)
        previous = new
        i= i + 1
    return listFlips

def countHeads(n):
    heads = 0
    listFlips = tossSequence(n)
    for i in range(len(listFlips)):
        heads = heads + listFlips[i]
    return heads
#samples5 = [countHeads(500) for i in range(10**4)]
#plt.hist(samples5,bins=50,normed=True)
#plt.show()

        
    
        
