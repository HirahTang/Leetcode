#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:47:37 2020

@author: TH
"""

# 该问题可转换为最大长度为k的所有子节点的和等于根节点的二叉树数量问题。

# 构建二叉树来解决该问题，从k_c=2开始计算root为n的树，遍历所有长度为2的树之后，k_c += 1
# 对于已构建的树的子节点递归地重复构建新的二叉树，此方法得到了k_c下的所有二叉树
# 当k_c = k时，停止递归输出结果

class binarytree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
n = int(input())
k = int(input())
bin_list = []
res = 0
# def integerdecompose(n, k, res):
#     if k == 1:
#         res += 1
#         return res
#     else:
    
def findbranch(n, k, res, bin_list):
    for i in range(1, n // 2+1):
        if n-i > 0:
            bin_list.append(binarytree(n, i, n-i))
            res += 1
    k -= 1
        
        