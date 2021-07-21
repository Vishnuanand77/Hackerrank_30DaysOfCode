# Day 20 : Sorting

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip()) #Size of the array

    a = list(map(int, input().rstrip().split())) #The array itself

    numSwaps = 0 #Integer to keep track of number of swaps
    
    #Implementing bubble sort
    for i in range(n):
        
        for j in range(n-1):
            if (a[j] > a[j+1]) : #Swap using a temporary variable
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numSwaps += 1
        if numSwaps == 0 :
            break
    
    print("Array is sorted in " + str(numSwaps) +  " swaps.") 
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[n-1]))
    
