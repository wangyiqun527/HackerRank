import math
import os
import random
import re
import sys

# Arrays

# Left Rotation
def rotLeft(a, d):
    return a[d:]+ a[0:d]
    
# New Year Chaos: A person can bribe at most 2 times the person before him to swap places. Find minimual swaps to get to current queue. 
def minimumBribes(q):
    moves = 0
    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            return "Too chaotic"
        for j in range(max(0,val-2), pos):
            if q[j] > val:
                moves+=1
    return moves

   
    
    
