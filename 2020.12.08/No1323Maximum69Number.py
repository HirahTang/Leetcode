#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:10:30 2020

@author: TH
"""
class Solution:
    def maximum69Number (self, num):
        str_ = str(num)
        str_ = [i for i in str_]
        for i in range(len(str_)):
            if str_[i] == '6':
                str_[i] = '9'
                break
            else:
                continue
        return int(''.join(str_))
            
        