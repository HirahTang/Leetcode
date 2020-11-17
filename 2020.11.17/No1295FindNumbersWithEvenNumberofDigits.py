#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:37:36 2020

@author: TH
"""
def findNumbers(nums):
    ct = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            ct += 1
    return ct