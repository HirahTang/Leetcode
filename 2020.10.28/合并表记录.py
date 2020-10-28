#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:30:24 2020

@author: TH
"""
n = int(input())
input_dict = {}
for i in range(n):
    s = input()
    s = s.split(' ')
    
    if int(s[0]) in input_dict:
        input_dict[int(s[0])] += int(s[1])
    else:
        input_dict[int(s[0])] = int(s[1])
    
for i in sorted(input_dict.keys()):
    print(str(i)+" "+str(input_dict[i]))