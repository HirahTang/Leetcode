#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:00:43 2020

@author: TH
"""
class Solution:
    def interpret(self, command):
        output = ''
        for i in range(len(command)):
            if command[i] == '(':
                if command[i+1] == ')':
                    output += 'o'
                    i += 1
                else:
                    output += 'al'
                    i += 3
            elif command[i] == 'G':
                output += 'G'
            else:
                continue
        return output
        