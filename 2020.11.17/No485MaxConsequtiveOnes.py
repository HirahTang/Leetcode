#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:21:29 2020

@author: TH
"""

def findMaxConsecutiveOnes(nums):
    gmax_ = 0
    lmax_ = 0
    for i in nums:
        if i == 1:
            lmax_ += 1
        else:
            gmax_ = max(gmax_, lmax_)
            lmax_ = 0
    return max(gmax_, lmax_)