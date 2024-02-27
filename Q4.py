#coin flip

import random

def flip(n):
    head = 0
    tail = 0
    i = 1
    while i<=n:
        coin = random.randint(0, 1)           #randint return integer value in specified range (inclusive of end index)
        if(coin == 1):   #1 for head
            head += 1
        else:              #0 for tail
            tail +=1
        i += 1        
    print("No of heads =", head)
    print("No of tails =", tail)
    print("Probability of getting head =", head/n)
    print("Probability of getting tail =", tail/n)

n = int(input("Total no of coin flips = "))
flip(n)