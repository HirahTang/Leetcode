#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:52:48 2020

@author: TH
"""

# Firstly, for x1 and x2, we need to change them into 10-based number for calculation

# With N known, x1 and x2 would be converted to:
#     t is the length of x minus 1, e.g. for 123456, t = 5
#     for i in x1:
#         value += i * N ** t
#         t -= 1
        
#     Thus we got x1, x2 10-based and do the calculation
    
#     res_x
    
#     Then we convert res_x back to the N-based number
    
#     in the form of N**t * a1 + N**(t-1) * a2 + ... + N**1 * a(k-1) + N**0 * ak
#     return to a1a2a3...ak


 # We get the value of x1 - x2 (based 10)
 # To convert to base N
 
 # Each time, we calculate refresh x1-x2 to (x1-x2) / N, and take the residual w
 
 # finially, we referse the list of all the residual, and get what we desire.

def converttointeger(x):
    if ord(x) in range(48, 58):
        return int(x)
    elif ord(x) in range(97, 123):
        return int(ord(x) - 87)
    
def calcvalue(N, x):
    t = len(x) - 1  
    x_value = 0
    for i in range(0, len(x)):
        x_value += N**t * converttointeger(x[i])
        t-= 1
    
    return x_value

def calctoNbase(N, x_n):
    
    w = []
    while x_n >= N:
        
        w.append(x_n % N)
        x_n = int(x_n / N)
    
    for i in range(len(w)):
        if w[i] >= 10:
            w[i] = chr(w[i] + 87)
            
    w.append(x_n)
    w = w[::-1]
    w = list(map(str, w))
    # print (w)
    return ''.join(w)
    # print (w)
    # return w


def main(N, x1, x2):
    try:

        x1 = calcvalue(N, x1)
        x2 = calcvalue(N, x2)
    # print (x1, x2)
        output_v = x1 - x2

        if output_v >= 0:
            output_c = 0
            print(output_c, output_v)
        else:
            output_c = 1
            output_v = output_v * (-1)
            output_v = calctoNbase(N, output_v)
            print(output_c, "-"+output_v)
        
    except:
        output_c = -1
    # output_v = ''
        print (output_c)

input_ = input()
input_ = input_.split(' ')
N = int(input_[0])
x1 = input_[1]
x2 = input_[2]

if (len(x1) > 1 and x1[0] == '0') or (len(x2) > 1 and x2[0] == '0'):
    print (-1)
else:
    main(N, x1, x2)


# print (int(x1) - int(x2))





