#Alex Karacaoglu

import random


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

def count_sequences(lis):
    count = 1
    x = lis[0]
    i = 1
    while (i < 50):
        if (x != lis[i]):
            count = count + 1
            x = lis[i]
        i = i + 1
    return count

def go():
    count =0
    for i in range(10**4):
        a = tossSequence(50)
        if (count_sequences(a) == 2):
            count = count + 1
    total = float(count)
    return (total / 10**4)
        

