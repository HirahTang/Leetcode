#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:03:47 2020

@author: TH
"""
def maxArea(height):
    '''
    
    For the first attempt, which catch a 192ms in runtime (surpass 8.2% users) and 
    a 39.2MB in memory usage, which surpass 7.23% users, I applied a recursive approach.
    
    Start with the leftmost line and the rightmost line, calculate the area
    
    Then take the shorter line, and renew that value(left += 1 if left one is smaller, 
                                                     right -= 1 if right one is smaller)
    and recalculate the area, if the area is getting bigger, renew the area, otherwise continue
    Untill the left index is larger than the right index, return the final largest area.
    
    '''
    def areacalc(right, left, height):
        return (right - left) * min(height[left], height[right])
    left = 0
    right = len(height) - 1
    
    area = areacalc(right, left, height)
    
    def recursiveMaxarea(left, right, area, height):
        if right > left:
            
            left_l = height[left]
            right_l = height[right]
            
            if left_l > right_l:
                right -= 1
                n_area = areacalc(right, left, height)
                if n_area >= area:
                    area = n_area
                return recursiveMaxarea(left, right, area, height)
                
            else:
                left += 1
                n_area = areacalc(right, left, height)
                if n_area >= area:
                    area = n_area
                return recursiveMaxarea(left, right, area, height)
            
            
        else:
            return area
        
    
    return recursiveMaxarea(left, right, area, height)

def maxArea(height):
    