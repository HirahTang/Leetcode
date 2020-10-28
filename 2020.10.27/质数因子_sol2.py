#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:01:23 2020

@author: TH
"""
a, res = int(input()), []
for i in range(2, a // 2 + 1):
    while a % i == 0:
        a = a / i
        res.append(i)
print(" ".join(map(str, res)) + " " if res else str(a) + " ")