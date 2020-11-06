#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:04:30 2020

@author: TH
"""
A = [int(i) for i in input().split(' ')]
B = [int(i) for i in input().split(' ')]

A_n = A[0]
B_n = B[0]

A = A[1:]
B = B[1:]

A = sorted(A)
B = sorted(B)
ia = 0
ib = 0
diff = abs(A[ia] - B[ib])
while True:
    if A[ia] > B[ib]:
        ib += 1
        diff = min(diff, abs(A[ia] - B[ib]))
        if ib == B_n - 1:
            break
        else:
            continue
    elif A[ia] < B[ib]:
        ia += 1
        diff = min(diff, abs(A[ia] - B[ib]))
        if ia == A_n - 1:
            break
        else:
            continue
    else:
        diff = 0
        break
    
print (diff)