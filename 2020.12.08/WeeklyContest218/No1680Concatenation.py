#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:41:58 2020

@author: TH
"""
class Solution:
    def concatenatedBinary(self, n):
        binsum = ''
        for i in range(1, n+1):
            binsum += bin(i)[2:]
        return int(binsum, 2) % (10 ** 9 + 7)
        