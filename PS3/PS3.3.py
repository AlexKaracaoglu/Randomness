#Alex Karacaoglu
#To run, run the module then do final(n) and sub in n as a pretty big number
#And you should get something pretty close to .000118 as found in the previous
#part of the problem

import random
import string

def toString(list):
    a = len(list)
    s =''
    for i in range(a):
        s = s + list[i]
    return s
        
def makeString():
    return toString([chr(random.randint(97,122)) for i in range(4)])

def check(string):
    if 'pi' in string:
        if 'it' in string:
            return 1
        else:
            return 0
    else:
        return 0

def count(lists):
    a = 0
    for i in range(len(lists)):
        if check(lists[i]) == 1:
            a += 1
        else:
            a += 0
    return a

a = [makeString() for i in range(100)]
def final(n):
    lista = [makeString() for i in range(n)]
    a = count(lista)
    return float(a) / n
    
