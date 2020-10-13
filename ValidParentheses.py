#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:58:15 2020

@author: TH
"""
# =============================================================================
# def isValid(s) -> bool:
#     for index, value in enumerate(s):
#         if value == '(':
#             for indexj, valuej in enumerate(s[index:]):
#                 if valuej == ')':
#                     if indexj % 2 == 1:
#                         print (valuej)
#                         break
#                     else:
#                         return False
#                 
#                 # return False
#         elif value == '{':
#             for indexj, valuej in enumerate(s[index:]):
#                 if valuej == '}':
#                     if indexj % 2 == 1:
#                         print (valuej)
#                         break
#                     else:
#                         return False
#                     
#                 
#                 # return False
#         elif value == '[':
#             for indexj, valuej in enumerate(s[index:]):
#                 if valuej == ']':
#                     if indexj % 2 == 1:
#                         print (valuej)
#                         break
#                     else:
#                         return False
#                 
#                 # return False
#     return True
# 
# print (isValid('([[)'))
# =============================================================================

def isValid(s) -> bool:
    # for index, value in enumerate(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        s = s.replace('()', '')
    return s == ''
print (isValid('({[]})'))