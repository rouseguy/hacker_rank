# The problem can be found here:
# https://www.hackerrank.com/challenges/find-digits


import sys

def findDigits(n):
    str_n = str(n)
    num_count = 0
    for i in str_n:
        if int(i) == 0:
            continue
        else:
            remainder = n%int(i)
            if remainder == 0:
                num_count = num_count + 1

    print(num_count)
        


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    findDigits(n)
