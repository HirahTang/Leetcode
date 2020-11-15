#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:51:24 2020

@author: TH
"""
# class tree:
#     def __init__(self, val = 0, left = None, right = None):
#     # def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# def levelOrder(root): # My Approach 5/34

    

    # res = [[root.val],[]]
    # level = 1
        
    # def breadthFirst(root, res, level):
    #     if root == None:
    #         return
    #     try:
    #         res[level].append(root.left.val)
    #         res[level].append(root.right.val)
    #         breadthFirst(root.left, res, level+1)
    #         breadthFirst(root.right, res, level+1)
    #     except:
    #         res.append([])
    #         breadthFirst(root.left, res, level)
    #         breadthFirst(root.right, res, level)
    # breadthFirst(root, res, level)
    # ct = 0
    # for i in res:
    #     if i == []:
    #         ct += 1
    # for i in range(ct):
    #     res.remove([])
    # return res
    
def levelOrder(root):
    if not root:
        return []
    ans, level = [], [root]
    
    while level:
        ans.append([i.val for i in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans
        



example = [3,9,20,0,0,15,7]





rightleft = TreeNode(example[5])
rightright = TreeNode(example[6])

nodeleft = TreeNode(example[1])
noderight = TreeNode(example[2], rightleft, rightright)

node = TreeNode(example[0], nodeleft, noderight)
