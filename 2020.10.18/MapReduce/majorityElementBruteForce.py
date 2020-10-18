#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:40:33 2020

@author: TH
"""

def majorityElement(nums):
    for i in nums:
        n = 0
        for j in nums:
            if j == i:
                n += 1
        if n >= len(nums)/2:
            return i
    