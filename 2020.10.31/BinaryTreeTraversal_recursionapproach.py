#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:51:26 2020

@author: TH
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def defineATree():
    lefttail = TreeNode(6)
    righttail = TreeNode(3)
    y = TreeNode(4, lefttail, righttail)
    
    rightmosttail = TreeNode(8)
    
    z = TreeNode(7, None, rightmosttail)
    
    x = TreeNode(5, y, z)
    
    return x

x = defineATree()
res = []
def preordertraversal(Tree, res):
    
    if Tree != None:
        res.append(Tree.val)
        preordertraversal(Tree.left, res)
        preordertraversal(Tree.right, res)
    
        return res
    else:
        return
    
def inordertraversal(Tree, res):
    
    if Tree != None:
        inordertraversal(Tree.left, res)
        res.append(Tree.val)
        inordertraversal(Tree.right, res)
        
        return res
    else:
        return 
    
def postordertraversal(Tree, res):
    
    if Tree != None:
        postordertraversal(Tree.left, res)
        
        postordertraversal(Tree.right, res)
        res.append(Tree.val)
        return res
    else:
        return 
    
