# Day 10 : Binary Numbers

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    count = 0
    
    convert_to_binary = bin(n)
    
    while (n!=0):
        n = (n & (n<<1))
        count += 1
        
    
    print(count)
