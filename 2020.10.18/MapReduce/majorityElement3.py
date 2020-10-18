#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:16:51 2020

@author: TH
"""
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        common = c.most_common(1)[0][0] # returns a list of sets, so we want to grab the first item in the set 
        return common