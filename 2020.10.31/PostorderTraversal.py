#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 00:25:31 2020

@author: TH
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):
        
        def _postorderTraversal(root, res):
            if root == None:
                return
            else:
                _postorderTraversal(root.left, res)
                _postorderTraversal(root.right, res)
                res.append(root.val)
                return res
        res = []
        return _postorderTraversal(root, res)