#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:00:18 2020

@author: TH
"""
class Solution:
    def thirdMax(self, nums):
        
        s_nums = sorted(set(nums))
        
        if len(s_nums) < 3:
            return max(nums)
        else:
            return s_nums[-3]
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)