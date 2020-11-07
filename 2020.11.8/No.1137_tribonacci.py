#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:47:58 2020

@author: TH
"""
def tribonacci(n):
    res = [0, 1, 1]
    if n <= 2:
        return res[n]
    c = len(res) - 1
    while len(res) <= n:
        res.append(res[c] + res[c-1] + res[c-2])
        c = len(res) - 1
    return res[-1]
        



def tribonaccirec(n):
    def recursive(res, n_c, n):
        if n_c == n:
            # print ('return', res)
            # w = res[-1]
            return res[-1]
            # return res[-1]
        fib = res[-1] + res[-2] + res[-3]
        res.append(fib)
        n_c += 1
        # print (res, n_c, n, res[-1])
        recursive(res, n_c, n)
        return res[-1]
    res = [0, 1, 1]
    if n <= 2:
        return res[n]
    
    
    return recursive(res, 2, n)
    # print (res)