#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:39:33 2020

@author: TH
"""
def q1(input_num):
    output = ''
    while input_num > 8:
        output = str(input_num % 8) + output # 除八取余
        input_num = int(input_num / 8) #更新除数
    output = str(input_num) + output    # 除数小于8，余数自身，作为第一位
    return int(output)

def q2():
    x = input().split(' ')
    
    rown = int(x[0])
    coln = int(x[1])
    matrix = []
    
    for i in range(rown):
        input_ = input().split(' ')
        input_ = [int(i) for i in input_]
        matrix.append(input_)
    output = [matrix[0][0]]
    row = 0
    col = 0
    for steps in range(1, rown + coln - 1):
        if row < rown - 1 and col < coln - 1:
            
            if matrix[row+1][col] > matrix[row][col+1]:
                row += 1
                output.append(matrix[row][col])
            else:
                col += 1
                output.append(matrix[row][col])
        else:
            if row == rown-1:
                col += 1
                output.append(matrix[row][col])
            elif col == coln-1:
                row += 1
                output.append(matrix[row][col])
            else:
                continue
    return sum(output), output


def checkpalindrome(x):
        if len(x)%2 == 0:
            parta = x[:int(len(x)/2)]
            partb = x[-int(len(x)/2):]
            return parta == partb[::-1]
        
        else:
            parta = x[:int(len(x)/2)]
            partb = x[-(int(len(x)/2)):]
            return parta == partb[::-1]
            # return True

def q3(string):
    output = {}
    for i in range(len(string)):
        for j in range(len(string)):
            # print (string[i:j+1])
            # if checkpalindrome(string[i:j+1]) == True:
            if string[i:j+1] != '':
                if checkpalindrome(string[i:j+1]):
                    
                    output[string[i:j+1]] = len(string[i:j+1])
    
    return (output.values)