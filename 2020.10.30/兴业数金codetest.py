#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:40:57 2020

@author: TH
"""
import sys
import re
import string
output_dict = {}
while True:
        # 读取每一行
    # line = sys.stdin.readline()
    line = input()
    for c in string.punctuation:
        line = line.replace(c, "")
    line = line.strip(" ")
    output =  line.split(' ')
    
    
    
    for i in range(len(output)):
        output[i] = output[i].lower()
        
        if output[i] in output_dict:
            output_dict[output[i]] += 1
        else:
            output_dict[output[i]] = 1
        
    
    if line == '':
        break

# print (output_dict)

for i in output_dict:
    print ('{},{}'.format(i, output_dict[i]) )
