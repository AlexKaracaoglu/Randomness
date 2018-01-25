#Alex Karacaoglu
#PS 7
#2a
#To run, just run go()

import random

def four_and_six():
    a = random.randint(1,6)
    b = random.randint(1,6)
    result = a + b
    if (result == 6):
        if (a == 4 or b==4):
            return 1
        else:
            return 0
    return 0
def six():
    a = random.randint(1,6)
    b = random.randint(1,6)
    result = a + b
    if (result == 6):
        return 1
    else:
        return 0

def count_six():
    count =0
    for i in range(10**6):
        a = six()
        if (a ==1):
            count = count+1
    return float(count)

def count_four_and_six():
    count = 0
    for i in range(10**6):
        a = four_and_six()
        if (a ==1):
            count = count+1
    return float(count)

def go():
    return (count_four_and_six() / count_six())
    

        
        
    
