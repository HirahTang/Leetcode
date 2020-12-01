#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:35:17 2020

@author: TH
"""
# def validMountainArray(arr): # Time Limit Exceeds
#     # p_end = len(arr) - 1
#     # p_start = 0
#     # ct = 0
#     # while True:
#     #     if arr[p_start + 1] > arr[p_start]:
#     #         p_start += 1
#     #     if arr[p_end - 1] > arr[p_end]:
#     #         p_end -= 1
        
#     #     if p_start == p_end:
#     #         return True
#     #     if ct == len(arr):
        
#     if arr[0] == max(arr) or arr[-1] == max(arr):
#         return False
    
#     for i in range(len(arr)):
#         if arr[i] == max(arr):
#             mid_p = i
    
#     arr_1 = arr[:mid_p + 1]
#     arr_2 = arr[-1:mid_p-1:-1]
    
#     for i in range(len(arr_1)-1):
#         if arr_1[i+1] <= arr_1[i]:
#             return False
    
#     for i in range(len(arr_2)-1):
#         if arr_2[i+1] <= arr_2[i]:
#             return False
    
    
#     return True

class Solution(object):
    def validMountainArray(self, A):
        
        '''Runtime: 196 ms, faster than 70.61%.
           Memory Usage: 15.4 MB, less than 33.16%'''
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1

    def validMountainArray2(self, arr):
        '''Runtime: 204ms, Memory Usage: 15.6MB'''
    
        p_start = 0
        p_end = len(arr) - 1
    
        max_ = max(arr)
        for i in range(len(arr)):
            if arr[i] == max_:
                p_max = i
    
        if arr[0] == max_ or arr[-1] == max_:
            return False
    
        while True:
            if p_start < p_max:
                if arr[p_start + 1] <= arr[p_start]:
                    return False
                else:
                    p_start += 1
            if p_end > p_max:
                if arr[p_end - 1] <= arr[p_end]:
                    return False
                else:
                    p_end -= 1
            elif p_start == p_end:
                return True
            else:
                continue
        

            
            