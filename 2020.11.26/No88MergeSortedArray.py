#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:00:23 2020

@author: TH
"""
# def merge(nums1, m, nums2, n):
    
    
#     if n == 0:
#             return nums1
    
        
#     if m > 0:
#         point1 = m-1
#     else:
#         point1 = 0
#     # if
#     # point1 = m - 1
#     point2 = n - 1
    
#     for i in range(m+n-1, -1, -1):
#         if nums1[point1] > nums2[point2]:
            
#             # print ('num1 - 1', nums1[point1])
#             print (nums1, i, point2)
#             print (nums1[point1], nums2[point2])
            
#             nums1[i] = nums1[point1]
#             nums1[point1] = 0
#             if point1 > 0:
#                 point1 -= 1
#             else:
#                 point2 -= 0
#             # if point1 == -1:
#             #     break
#         else:
            
#             # print ('num2 - 1', nums2[point2])
            
#             nums1[i] = nums2[point2]
#             print (nums1, i, point2)
#             print (nums1[point1], nums2[point2])
#             # point2 -= 1
#             if point2 > 0:
#                 point2 -= 1
#             else:
#                 point1 -= 0
#     return nums1

def merge2(nums1, m, nums2, n):
    for i in range(len(nums1[m:m+n])):
        nums1[m+i] = nums2[i]
    x = sorted(nums1)
    for i in range(len(nums1)):
        nums1[i] = x[i]
    return sorted(nums1)


def mergemyapproach(nums1, m, nums2, n): # Not applicable on merge([0], 0, [1], 1)
    numa = nums1[:m]
    p1 = len(numa) - 1
    p2 = n - 1
    if p1 < 0:
        return nums2
    elif p2 < 0:
        return nums1
    # print (nums1)
    for i in range(len(nums1)-1, -1, -1):
        if numa[p1] > nums2[p2]:
            nums1[i] = numa[p1]
            print (nums1, p1, p2, 'p1')
            if p1 > 0:
                p1 -= 1
            else:
                numa[p1] = 0
        else:
            nums1[i] = nums2[p2]
            print (nums1, p1, p2, 'p2')
            if p2 > 0:
                p2 -= 1
            else:
                nums2[p2] = 0
    return nums1

def mergesol(nums1, m, nums2, n):
    while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]