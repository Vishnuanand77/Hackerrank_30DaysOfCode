# Day16 : Exceptions - String to Integer

#!/bin/python3

import math
import os
import random
import re
import sys


S = input()

#We can use try catch to handle exceptions

try :
    print(int(S))
except ValueError:
    print("Bad String")