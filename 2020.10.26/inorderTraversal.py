#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:54:42 2020

@author: TH
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _inorderTraversal(self, root: TreeNode, arr):
        if root is None:
            return
        
        self._inorderTraversal(root.left, arr)
        arr.append(root.val)
        self._inorderTraversal(root.right, arr)
    def inorderTraversal(self, root: TreeNode):
        res = []
        self._inorderTraversal(root, res)
        return res