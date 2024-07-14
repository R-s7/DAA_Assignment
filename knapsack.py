import os
import sys
import random
import re
import math

def unboundedKnapsack(k, arr):
    d = [False] * (k + 1)
    d[0] = True
    for n in arr:
        for j in range(n, k + 1):
            if d[j - n]:
                d[j] = True
    max_s = 0
    for j in range(k, 0, -1):
        if d[j]:
            max_s = j
            break
    return max_s

if __name__ == '__main__':
    
    input_data = sys.stdin.read().strip().split('\n')
    
    t = int(input_data[0])
    
    index = 1
    results = []