#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:14:23 2020

@author: TH
"""
def removeElement(nums, val):
    # Take the number of removed into account, 
    # every time move each element back forward rem_n positions
    rem_n = 0
    
    for i in range(len(nums)):
        
        if nums[i] == val:
            rem_n += 1
        elif nums[i] != val:
            nums[i - rem_n] = nums[i]
        else:
            continue
     #   nums = nums[:len(nums)-rem_n]
    return len(nums) - rem_n