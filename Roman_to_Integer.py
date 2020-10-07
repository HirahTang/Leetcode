#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:48:55 2020

@author: TH
"""
def romanToInt(s: str) -> int:
    output_v = 0
    rom_dict = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
    for i in range(len(s)):
        output_v += rom_dict[s[i]]
    
    subtract_dict = {'IV':-2,
                     'IX':-2,
                     'XL':-20,
                     'XC':-20,
                     'CD':-200,
                     'CM':-200}
    sub_l = 0
    for i in range(1, len(s), 2):
        if s[i-1]+s[i] in subtract_dict:
            sub_l += subtract_dict[s[i-1]+s[i]]
            # print (s[i-1]+s[i])
    
    for i in range(2, len(s), 2):
        # print (s[i-1]+s[i])
        if s[i-1]+s[i] in subtract_dict:
            sub_l += subtract_dict[s[i-1]+s[i]]
            # print ('select\n')
    # print (sub_l)
    output_v = output_v + sub_l
    return output_v