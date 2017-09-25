#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:17:29 2017

@author: Armaan Sethi
"""

def maskn(lst, i):
    #iterate through list
    for idx, curr_element in enumerate(lst):
        #if current element is divisible by i, set it equal to 1
        if (curr_element%i==0):
            lst[idx] = 1
        #else set it equal to 0
        else:
            lst[idx] = 0
    return lst
            
print("   ", [50,48,51])
for i in range(1,11):
    print(str(i)+", ", maskn([50,48,51],i))