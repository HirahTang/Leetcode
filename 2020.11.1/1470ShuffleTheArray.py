#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 16:26:46 2020

@author: TH
"""
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n]
        nums2 = nums[n:]
        output = []
        for i in range(n):
            output.append(nums1[i])
            output.append(nums2[i])
        return output