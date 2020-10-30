#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 01:08:42 2020

@author: TH
"""
n = int(input())
calc_list = []
for i in range(n):
    x = input().split(' ')
    x = list(map(int, x))
    calc_list.append(x)


for i in range(len(calc_list)):
    for j in range(len(calc_list)):
        if calc_list[i][j] == -3:
            mom = (i,j)
        if calc_list[i][j] == -2:
            kid = (i,j)
print (mom, kid)
# print (calc_list)