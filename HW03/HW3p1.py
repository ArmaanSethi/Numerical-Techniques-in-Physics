#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:03:51 2017

@author: armaan
"""
#No need to finish code
#A) Since I cannot use exponents, I must use multiplication and subtraction
def f(x):
    return (x*x*x)-750
# The derivative of f(x) can be written as
def f_prime(x):
    return 3*x*x

def main():
    x = np.arange(-100, 100, 0.01) 

main()