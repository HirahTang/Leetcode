#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:46:37 2020

@author: TH
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def _preorderTraversal(self, root: TreeNode, arr):
        if root is None:
            return
        arr.append(root.val)
        self._preorderTraversal(root.left, arr)
        self._preorderTraversal(root.right, arr)
    
    def preorderTraversal(self, root: TreeNode):
        res = []
        self._preorderTraversal(root, res)
        
        return res
    
                