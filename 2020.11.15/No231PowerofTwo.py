#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:55:32 2020

@author: TH
"""
def isPowerOfTwo(n):
    '''
    
    Recursive Approach
    
    Runtime: 32ms, better than 57.28%
    Memory Usage: 14.1MB, better than 26.55%
    
    '''
    def powerofTworec(exp, n):
        if 2 ** exp > n:
            return False
        elif 2 ** exp == n:
            return True
        else:
            exp += 1
            return powerofTworec(exp, n)
    exp = 0
    return powerofTworec(exp, n)

def isPowerofTwo(n):
    '''
    
    Iterative Approach
    
    Runtime: 28ms, better than 82.2%
    Memory Usage: 14.2MB, better than 5.04%
    
    '''
    exp = 0
    while 2**exp <= n:
        if 2 ** exp == n:
            return True
        
        exp += 1
    return False

def isPowerofTwo(n):
    return n > 0 and not (n & n-1)


    