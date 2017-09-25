#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:26:32 2017

@author: Armaan Sethi
"""

def fib_loop(n):
    n0=0
    #return 0 if n = 0
    if(n==0):
        return n0
    n1=1
    #return 1 if n = 1
    if(n==1):
        return n1
    #fibanacci
    for i in range(n-1):
        n2 = n0 + n1
        n0 = n1
        n1 = n2
    return(n2)

def fib_recur(n):
    #return 0 if n = 0
    if(n==0):
        return 0
    #return 1 if n = 1
    if(n==1):
        return 1
    #fibanacci
    return fib_recur(n-2)+fib_recur(n-1)
    
    
for i in range(30):
    print(fib_loop(i), fib_recur(i))        
        