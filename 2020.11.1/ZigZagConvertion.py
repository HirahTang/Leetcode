#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 16:46:22 2020

@author: TH
"""
def convert(s, numRows): # My current Approach
    if numRows == 1:
        return s
    unit_n = 2 * numRows - 2
    while len(s) / unit_n != int(len(s) / unit_n): # Padding
        s+= '*'
        
    res = [[] for i in range(numRows)]
    res_prep = []
    for i in range(0, len(s), unit_n):
        res_prep.append(s[i:i+unit_n])
        
    for i in range(len(res_prep)):
        for j in range(unit_n):
            if j < numRows:
                # print (res_prep[i][j], i, j)
                res[j].append(res_prep[i][j])
                
            elif j >= numRows:
                # print (res_prep[i][j], i, j)
                res[2*(numRows-1) - j].append(res_prep[i][j])
            # print (res_prep[i][j], i, j)
        # print ('\n')
    
    for i in range(len(res)):
        res[i] = ''.join(res[i])
    return (''.join(''.join(res).split('*')))
    