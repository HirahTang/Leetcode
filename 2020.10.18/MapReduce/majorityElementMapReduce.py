#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:48:03 2020

@author: TH
"""
def count_(n, nums):
    ct = 0
    for i in nums:
        if i == n:
            ct += 1
    return ct
    
def majorityElement(nums):
        
    
    # End of iteration
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    # Divide the problem
    left  = majorityElement(nums[:len(nums)//2])
    right = majorityElement(nums[len(nums)//2:])
        
    # Conquer and combine subproblems
    if left == right:
        return left
    if count_(left, nums) > count_(right, nums):
        return left
    else:
        return right 
    
    
    