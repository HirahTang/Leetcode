#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:54:57 2020

@author: TH
"""
input_ = int(input())
def ifprime(n):
    factor_l = []
    for i in range(1, n+1):
        if n%i == 0:
            factor_l.append(i)
        else:
            continue
    return len(factor_l) == 2
output = []



while ifprime(input_) == False:
    
    # input_ = int(input_ / 2)
    # output.append(input_)
    for i in range(2, input_+1):
        if ifprime(i):
            if input_%i == 0:
                output.append(i)
                input_ = int(input_/i)
                break
                
output.append(input_)
print (' '.join(map(str, output)))
# print (ifprime(input_))