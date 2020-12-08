#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:51:32 2020

@author: TH
"""
class Solution:
    def heightChecker(self, heights):
        # print ('test')
        st = 0
        # j = 0
        j_l = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != j_l[i]:
                st += 1
            else:
                continue
            
        return st