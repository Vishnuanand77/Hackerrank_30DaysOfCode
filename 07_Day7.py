# Day 7 : Arrays

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    for i in range(len(arr)-1, -1, -1):
        print(str(arr[i]) + " ", end="")