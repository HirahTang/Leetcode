#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:41:16 2020

@author: TH
"""
def romanToInt(s: str) -> int:
    rom_dict = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
    
    res = 0
    i = 0
    while i < len(s):
        print (res, s[i])
        s1 = rom_dict[s[i]]
        if i + 1 < len(s):
            s2 = rom_dict[s[i+1]]
            if s1 >= s2:
                res += s1
                i += 1
            else:
                res += (s2 - s1)
                i += 2
        else:
            res += s1
            i += 1
        
    return res
        