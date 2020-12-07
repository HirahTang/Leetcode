#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:49:19 2020

@author: TH
"""
class Solution:
    def sortArrayByParity(self, A): # In-place
        odd_num = 0
        for i in range(len(A)):
            if A[i] % 2 != 0:
                odd_num += 1
            else:
                A[i], A[i-odd_num] = A[i-odd_num], A[i]
                
        return A
    def sortArrayByParity(self, A): # Two-passs
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])
    
    def sortArrayByParity(self, A): # Sort
        A.sort(key = lambda x: x % 2)
        return A