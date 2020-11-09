#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:20:33 2020

@author: TH
"""
def f1(s):
    o = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in s:
        if i not in o:
            count += 1
    return count

def f2(n):
    count  = 0
    for i in range(1, n+1):
        if i % 2 == 0 or i % 3 == 0:
            count += i
    return count

def f3(L):
    l_c = []
    for i in L:
        if i not in l_c:
            l_c.append(i)
        else: 
            return False
    return True

def f4(L):
    def ifprime(n):
        num = 0
        for i in range(n+1):
            if n % i == 0:
                num += 1
                
        if num > 2:
            return False
        else:
            return True
    count = 0    
    for i in L:
        if ifprime(i):
            count += 1
    return count