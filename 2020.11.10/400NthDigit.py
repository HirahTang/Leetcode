#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:50:34 2020

@author: TH
"""
# def findNthDigit(n):
#     if n < 10:
#         return n
#     # elif n == 10:
#     #     return 1
#     # elif n == 11:
#     #     return 
#     else:
#         k = 0
#         sum_ = 0
#         while sum_ < n:
#             k += 1
#             sum_ += k * 9 * (10 ** (k-1))
        
#         sum_ -= k * 9 * (10 ** (k-1))
    
#         num = int((n - sum_) / k)
#         p = (n - sum_) % k
        
#         return [p-1]
        # plus = int(residual / k)
        # res = residual % k
    
    # return str(10 ** (k-1) + plus)[res-1]
    
        # return sum_, k, plus, str(10 ** (k-1) + plus), res, str(10 ** (k-1) + plus)[res]
    
    # return 
    
import math    
def findNthDigit(n):
    len_int = 1
    sum_ = 0
    while n > sum_ + len_int * 9 * 10 ** (len_int-1):
        sum_ += len_int * 9 * 10 ** (len_int-1)
        len_int += 1
        
    if len(str(n)) == 1:
        return str(n)
    
    
    closest_dig = 10 ** (len_int-1)-1 + math.ceil((n - sum_) / len_int)
    # if n-sum_ < len_int:
    #     closest_dig += 1
    # int((n - sum_) / len_int)
    
    if (n-sum_) % len_int == 0:
        return str(closest_dig)[-1]
    else:
        return str(closest_dig)[(n-sum_) % len_int - 1]
    # return closest_dig, (n-sum_) % len_int
    
    # n - 
    
    