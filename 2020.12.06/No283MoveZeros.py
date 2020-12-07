#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 00:17:31 2020

@author: TH
"""

class Solution:
    def moveZeroes(self, nums):
        
        # if len(nums) > 1:
            
        
        mov_num = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                mov_num += 1
            else:
                if mov_num == 0:
                    continue
                else:
                    nums[i - mov_num] = nums[i]
                    nums[i] = 0
        return nums