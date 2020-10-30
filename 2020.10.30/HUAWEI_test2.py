#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:49:19 2020

@author: TH
"""

# For each input n: n = i + (i+1) + ... + (i + k)

# Find out all the integer i and k for n

# If we have k and n, we can get i, i = (2n - k ** 2 - k) / (2k + 2)
# if i is a valid integer, then i + (i+1) + ... + (i+k) is a valid input

# So for any n, how do we know the largest possible k?

# We start with the current n, everytime n+=1, check if n is the sum of 1 + 2 + 3 + ... + x

# Once we get a valid n + t, which can represent as a form 1 + 2 + 3 + ... + x,
# we will know the largest possible value of k, as k is always equal or smaller than x

# k <= x, So we iterate from 0 to x, calculate i each time, get all the cases where i 
# is an integer, which is a valid output
import math
n = int(input())

def CheckTheLargestK(n): #  This function get the largest possible K
    
    while int((math.sqrt(1 + 8 * n) - 1) / 2) != (math.sqrt(1 + 8 * n) - 1) / 2:
        n += 1
    return int((math.sqrt(1 + 8 * n) - 1) / 2)

def printfunc(n, i, k):
    output_l = [i+j for j in range(k+1)]
    output_l = map(str, output_l)
    print (str(n)+"="+'+'.join(output_l))
    # print (i, k)
k = CheckTheLargestK(n)
sum_ = 1
print ("{}={}".format(n,n))
for k_ in range(1, k):
    i = (2*n - k_**2 - k_) / (2*k_ + 2)
    if i == int(i):
        printfunc(n, int(i), k_)
        sum_+=1
print ("Result:{}".format(sum_))
        
    