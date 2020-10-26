#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:44:10 2020

@author: TH
"""
def maxSubArrayKadane(nums):
        c = nums[0]
        g = nums[0]
    # print (i, c, g)
        for i in nums[1:]:
        # print (i, c, g)
            if i+c > i:
                c += i
                if c > g:
                    g = c
                else:
                    continue
            else:
                c = i
                if c > g:
                    g = c
                else:
                    continue
    # print (i, c, g)
        return g
    
def maxSubArrayBruteForce(nums):
    max_array = []
    for i in range(len(nums)):
        max_array.append(nums[i])
        for j in range(i, len(nums)):
            # print (nums[i:j])
            max_array.append(sum(nums[i:j+1]))
    return max(max_array)

# def maxSubArrayDAC(nums):

#     # The end of divide
    
#     if not nums:
#         return None
#     if len(nums) == 1:
#         return nums[0]
#     # if len(nums) == 1:
#     #     return nums[0]
    
#     left = maxSubArrayDnC(nums[:len(nums)//2]) 
#     right = maxSubArrayDnC(nums[len(nums)//2:]) 
    
    
#     max_l = nums[]
    # if left
    # if sum(left) > 0:
        