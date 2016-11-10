# The problem can be found here:
# https://www.hackerrank.com/challenges/is-fibo

import os
import sys

#Initialize base numbers for generating fibonacci series
f1 = -1
f2 = 1

#Generate the fibonacci series
fibSeries = []
while f2 < 10**10:
    f1 = f1 + f2
    f2 = f1 + f2
    fibSeries.append(f1)
    fibSeries.append(f2)
    
    
n = int(input())
for i in range(n):
    num = int(input())
    if num in fibSeries:
        print("IsFibo")
    else:
        print("IsNotFibo")
