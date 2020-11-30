#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:24:50 2020

@author: TH
"""
def checkIfExist(arr):
    ct = 0
    for i in arr:
        if i == 0:
            ct += 1
    if ct > 1:
        return True
    half = set(arr)
    for i in arr:
        if i//2 in half and i % 2 == 0 and i != 0:
            return True
        
        # elif i % 2 == 0:
        #     half.add(i//2)
        else:
            continue
    return False
            

def checkIfExist(arr):
    seen = set()
    for i in arr:
          # if 2 * i in seen or i % 2 == 0 and i // 2 in seen:
       if 2 * i in seen or i / 2 in seen: # credit to @PeterBohai
           return True
       seen.add(i)
    return False