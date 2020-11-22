#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:44:41 2020

@author: TH
"""
def sortedSquares_sortedApproach(A):
    return sorted([i ** 2 for i in A])

def sortedSquares_twopointersApproach(A):
    answer = [0] * len(A)
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer[r - l] = left * left
            l += 1
        else:
            answer[r - l] = right * right
            r -= 1
    return answer