#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:38:52 2020

@author: TH
"""

class linkedlist:
    def __init__(self, val, next_):
        self.val = val
        self.next_ = next_
        

module = input()
relate_n = int(input())
modules = []
for i in range(relate_n):
    c_module = input()
    c_module = c_module.split('->')
    modules.append(c_module)
nodes = []    
for i in range(len(modules)):
    nodes.append(linkedlist(modules[i][0], modules[i][1]))
n = 0    
rel_list = [module]
# for i in range(len(nodes)):
#     if nodes[i].val_ == module:
#         rel_list.append(nodes[i].next_)
#         n += 1

def renew_l(n, rel_list, module, nodes):
    orig = len(rel_list)
    for i in rel_list:
        for j in range(len(nodes)):
            if nodes[j].val == i and nodes[j].next_ not in rel_list:
                rel_list.append(nodes[j].next_)
                n += 1
    if orig != len(rel_list):
        return renew_l(n, rel_list, module, nodes)
    else:
        return n
print (renew_l(n, rel_list, module, nodes))
                
    