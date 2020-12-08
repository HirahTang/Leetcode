#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:11:11 2020

@author: TH
"""
from collections import Counter
class Solution:
    def maxOperations(self, nums, k):
        pairs = 0
        count_dict =  Counter(nums)
        if k%2 == 0 and k//2 in count_dict:
            pairs += count_dict[k//2] // 2
            count_dict[k//2] -= pairs * 2
            
            del count_dict[k//2]
        for i in count_dict:
            # print (count_dict, pairs)
            if count_dict[i] > 0 and k-i in count_dict:
               # count_dict[i] -= 1
                if count_dict[k-i] > 0:
                    pairs += min(count_dict[i], count_dict[k-i])
                    
                    tempi = count_dict[i] - min(count_dict[i], count_dict[k-i])
                    tempki = count_dict[k-i] -  min(count_dict[i], count_dict[k-i])
                    
                    count_dict[i] = tempi
                    count_dict[k - i] = tempki
                else:
                  #  count_dict[i] += 1
                    continue  
            else:
                continue
        return pairs