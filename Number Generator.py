# This is a random number generator and the maximum difference is between negative 1 billion to positive 10 billion.






# start




# import
from io import FileIO
import os
import math


# setting
mini = 0.0
maxi = 0.0

print('Do you want your results to be a decimal or an integer? (\'d\' for decimal or \'i\' for integer)')
input()
if input := 'd':
    print('Minimum number?')
    af_mini = input()
    mini += float(af_mini)