#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 22:50:54 2020

@author: TH
"""
def findDuplicate1(nums): # Exceed time limits
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                ret = nums[i]
                break
    return ret

def findDuplicate2(nums):
    res_l = []
    for i in range(len(nums)):
        if nums[i] in res_l:
            return nums[i]
            # print (res_l)
        else:
            res_l.append(nums[i])
        
def findDuplicate3(nums): # Sorted Approach
    l_ = sorted(nums)
    for i in range(1, len(nums)):
        if l_[i] == l_[i-1]:
            return l_[i]
        
def findDuplicate(nums): # Set approach

    '''

    Runtime: 60 ms, faster than 84.78% of Python3 online submissions 
    Memory Usage: 18.6 MB, less than 6.97% of Python3 online submissions '''

    res = set()
    for i in nums:
        if i in res:
            return i
        else:
            res.add(i)