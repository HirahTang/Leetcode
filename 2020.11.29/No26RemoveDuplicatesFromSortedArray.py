#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:57:51 2020

@author: TH
"""
def removeDuplicates(nums):
    local = glob = dup_n = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[local]:
            local = i
            glob += 1
            nums[glob] = nums[i]
        else:
            dup_n += 1
    return len(nums) - dup_n
    # return  len(nums) - dup_n, nums
        # nums[i] = nums[i+]