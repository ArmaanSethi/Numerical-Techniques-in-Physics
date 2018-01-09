#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:46:15 2017

@author: armaan
"""
import numpy as np
import scipy
import math
"""Part 3A to Test It"""
def test(x):
    return (1-x**2)**0.5
"""Weight Function"""
def W(x):
    return 2*(1-x**2)**(-0.5)

"""Function From Problem in Textbook"""
def C(z):
    return ((np.sqrt(2)-1)**2 - (np.sqrt(1+z**2)-1)**2) **(-0.5)

def f(z): 
    return np.sqrt( (np.sqrt(2) - 1)**2 - ( np.sqrt(1+z**2) - 1 )**2 )

"""Solve Abscissas"""
def absc(n):
    x_list = []
    for i in range(n):
        x_list.append( np.cos((2*i-1)*np.pi/(2*n)) )
#    print(x_list)
    return x_list
    
"""Solve Weight Function"""
def weight(n):
    return np.pi/n

def funcCheb(f, N):
    summation = 0
    x = absc(N)
    for i in range(N):
        summation+= f(x[i])/W(x[i])

    summation = weight(N)*summation
    return summation

a3 = funcCheb(test, 3)

print("Part 3a: ",a3 , "\tError: ", a3-np.pi/4)

actual = scipy.integrate.quad(C, 0, 1)
print(actual)

#Since My First Guess seems to be the cloesest to being accurate
#No need to manually solve for it
x = funcCheb(C,9)
print("Error: ", abs(x-actual[0]) )
x = funcCheb(C,10)
print("Error: ", abs(x-actual[0]) )


x = funcCheb(C,10000)
print('sci\t\t', actual[0])
print("Large N: \t", '{0:.16f}'.format(x) )

print('wolf\t\t',  3.26670225210615)
