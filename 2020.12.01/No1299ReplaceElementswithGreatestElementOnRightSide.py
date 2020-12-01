#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:30:45 2020

@author: TH
"""
class Solution:
    def replaceElements(self, arr):
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr
    def replaceElements(self, A, mx = -1):
        for i in range(len(A) - 1, -1, -1):
            A[i], mx = mx, max(mx, A[i])
        return A
    
    def replaceElements(self, arr): # Not an in-line approach though
        out = [-1]
        greatest = 0
        for num in arr[::-1]:
            if greatest < num:
                greatest = num
            out.append(greatest)
        out.pop()
        return out[::-1]