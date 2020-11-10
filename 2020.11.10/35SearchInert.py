#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:29:08 2020

@author: TH
"""
def searchInsert(nums, target):

    def BinarySearch(list_, target, low, high):
        if high >= low:
            mid = (low + high) // 2
            if list_[mid] == target:
                return mid
        
            elif list_[mid] > target:
                return BinarySearch(list_, target, low, mid-1)
        
            else:
                return BinarySearch(list_, target, mid+1, high)
        
        else:
            return low
    low = 0
    high = len(nums)-1
    return BinarySearch(nums, target, low, high)