#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 14:29:21 2020

@author: TH
"""


class Solution:
    def longestCommonPrefix(self, s) -> str:
        if len(s) == 0:
            return ''
        n = 0
        while True:
            for i in s:
                if n >= len(s[0]):
                    return s[0]
                if s[0][:n+1] == i[:n+1]:
                    continue
                else:
                    return s[0][:n]
            n += 1