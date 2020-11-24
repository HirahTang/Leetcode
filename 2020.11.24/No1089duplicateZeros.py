#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:08:35 2020

@author: TH
"""
def duplicateZeros(arr):
     # The first step:
         # Decide how many zeros are going to duplicate - dup_n
         # then the elements to the result is arr[:dup_n]
    dup_n = 0
    p = 0      # The second pointer to the list, normally += 1, 
    # += 2 when encounter a zero
    # For each time pointer p renews, check whether p is at the edge of list (p > len(arr) - 1)
    # If so, break, we get the sublist to be duplicated
    for i in range(len(arr)):
        if arr[i] == 0:
            p += 1
            if p <= len(arr) - 1:
                dup_n += 1
                p += 1
                if p > len(arr) - 1:
                    break
            else:
                break
        else:
            p += 1
            if p > len(arr) - 1:
                break
            
    # The second step:
        # From right to left, put elements of the sublist to the original list
        # When it's 0, duplicate it (put 0 for twice) and dup_n -= 1.
        # When dup_n == 1, 0 would not be duplicated even if encouters it.
    sub = arr[:-dup_n]
    sub_ct = 0
    for i in sub:
        if i == 0:
            sub_ct += 1
            
    # Adjustment for edge cases:
        # if the last zero would not be duplicated, we assign a diff_reg as 1
        # and make it to zero for the first zero encountered (from right to left)
        # So the upcoming steps could be performed fluently
            
    diff_reg = 0
    if sub_ct != dup_n:
        diff_reg += 1
        
        
    p2 = len(arr) - 1
    for i in sub[::-1]:
        if i == 0 and dup_n > 0:
            if diff_reg != 0:
                diff_reg -= 1
                arr[p2] = i
                p2 -= 1
            else:
                arr[p2] = i
                p2 -= 1
                arr[p2] = i
                p2 -= 1
                dup_n -= 1
        else:
            arr[p2] = i
            p2 -= 1
    return arr

def duplicateZeros(arr): 
    # This approach is the Leetcode official solution, 
    # with similar space complexity and
# Slightly higher time complexity than mine.
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
                
def duplicateZeros(arr): #  The most popular approach on discussion board
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n-1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0: 
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0
            