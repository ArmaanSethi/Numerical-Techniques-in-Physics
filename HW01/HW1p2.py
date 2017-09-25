#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:03:54 2017

@author: Armaan Sethi
"""
import math

def taylor_sin(x0, n):
    #should return 0 or is not a valid test case(is negative)
    if(n%2==0 or n <= 0):
        return 0
    else:
        #positive term
        if(n%4== 1):
            return x0**n/(math.factorial(n))
        #negative terms
        else:
            return -x0**n/(math.factorial(n))


for i in range (20):
    print(str(i) + ", ", taylor_sin(1.7,i))
