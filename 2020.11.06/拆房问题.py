#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:48:04 2020

@author: TH
"""
input_ = [int(i) for i in input().split(' ')]
target = input_[0]
input_ = input_[1:]
l_ = []

def recursiveRemove(l_, target):
    if sum(l_) > target:
        recursiveRemove(l_[1:], target)
    else:
        return l_
    
        
res = []   


for i in input_:
    
    l_.append(i)
    # print (l_)
    if sum(l_) < target:
        continue
    elif sum(l_) >= target:
        # res.append(len(l_))
        while sum(l_) >= target:
            res.append(len(l_))
            # if l_[-1] < l_[0]:
            l_ = l_[1:]
            # else:
            #     l_ = l_[2:]
            # if sum(l_) == target:
            #     res.append(len(l_))
            #     break
        
        # l_ = recursiveRemove(l_, target)
        # if sum(l_) == target:
        #     res.append(len(l_))
    else:
        res.append(len(l_))
        
if len(res) == 0:
    print (0)
else:
    print (min(res))