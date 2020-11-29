#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:08:45 2020

@author: TH
"""
import os
import time
import random

board = [" ", " "," "," "," "," "," "," "," ",]

def print_board():
    print ("   |   |   ")
    print (" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print ("   |   |   ")
    
    print ("---|---|---")
    
    print ("   |   |   ")
    print (" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print ("   |   |   ")
    
    print ("---|---|---")
    
    print ("   |   |   ")
    print (" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print ("   |   |   ")
    
while True:
    os.system("clear")
    print_board()
    choice = input("Choose an empty space for X: ")
    choice = int(choice)
    
    # Check to see if the space is empty first
    
    if board[choice] == " ":
        board[choice] = "X"
    else:
        continue
    
    # Check for X win
    
    if (board[0] == "X" and board[1] == "X" and board[2] == "X"):
        os.system("clear")
        print_board()
        print ("X wins")
        break
    