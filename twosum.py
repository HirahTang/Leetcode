#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:32:25 2020

@author: TH
"""

class Solution:
    def twoSum(self, nums, target: int):
        prevMap = {} # val : index
        
        
        for i,n in enumerate(nums):
            
            if target - n in prevMap:
                return [prevMap[target-n], i]
            prevMap[n] = i
            