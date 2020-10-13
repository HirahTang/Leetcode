#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:03:25 2020

@author: TH
"""
def runningSum(nums):
    output = []
    n = 0
    for i in range(len(nums)):
        n += nums[i]
        output.append(n)
            
            #output.append(sum(nums[:i+1]))
    return output
print (runningSum([1,2,3,4]))