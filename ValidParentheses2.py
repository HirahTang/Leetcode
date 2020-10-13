#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:25:18 2020

@author: TH
"""

def isValid(s) -> bool:
    d = {'(':')',
         '[':']',
         '{':'}'
         }
    stack = []
    for i in s:
        if i in d:
            stack.append(d[i])
        elif i in stack:
            out = stack.pop()
            if out != i:
                return False
        else:
            return False
    return stack == []
            
print (isValid('({{{{}}}))'))

