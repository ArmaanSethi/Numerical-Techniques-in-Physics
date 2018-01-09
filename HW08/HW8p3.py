#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:33:57 2017

@author: armaan
"""

import numpy as np
import matplotlib.pyplot as plt
def myJacobi(A, b, w, tol):    
    n = A.shape[0]
    D = np.copy(A)
    U = np.copy(A)
    L =  np.copy(A)
    for i in range (n):
        for j in range(n):
            if i < j:
                D[i][j] = 0
                L[i][j] = 0
            if i == j:
                U[i][j] = 0
                L[i][j] = 0
            if i > j:
                D[i,j] = 0
                U[i][j] = 0
    Dinv = np.zeros((n,n))
    for i in range(n):
        Dinv[i,i] = 1/D[i,i]
#    print(Dinv)
    
    x = np.zeros_like(b)
    for i in range(len(b)):
        x[i] = b[i]/A[i][i] #Create Initial Guess
    
    max_diff = np.inf #make sure max_diff > tolerance for beginning
    LU = L+U
    iters = 0
    while max_diff > tol:
        x0 = x
        step1 = np.dot(LU, x0)
        step2 = np.dot((-1*Dinv), step1)
        step3 = np.dot(Dinv, b)
        x = w*(step2+step3) + (1-w)*x0
        max_diff = 0
#        print("Current solution:", x)
        diff = x - x0
#        print('diff', diff)
        for d in diff:
            if abs(d) > max_diff:
                max_diff= abs(d)
#        print('max_diff', max_diff)
        
        iters+=1
    return (x, iters)


A = np.array([[-4, 1, 0, 1, 0, 0, 0, 0, 0],
              [1, -4, 1, 0, 1, 0, 0, 0, 0],
              [0, 1, -4, 1, 0, 1, 0, 0, 0],
              [1, 0, 1, -4, 1, 0, 1, 0, 0],
              [0, 1, 0, 1, -4, 1, 0, 1, 0],
              [0, 0, 1, 0, 1, -4, 1, 0, 1],
              [0, 0, 0, 1, 0, 1, -4, 1, 0],
              [0, 0, 0, 0, 1, 0, 1, -4, 1],
              [0, 0, 0, 0, 0, 1, 0, 1, -4]], dtype= float)
    
b = np.array([[0],
              [0],
              [100],
              [0],
              [0],
              [100],
              [200],
              [200],
              [300]], dtype =float)
    
print(np.linalg.solve(A,b))
#A2 = np.array([[4, -1, 0, 1, 0, 0, 0, 0, 0],
#              [1, -4, 1, 0, 1, 0, 0, 0, 0],
#              [0, 1, -4, 0, 0, 1, 0, 0, 0],
#              [1, 0, 0, -4, 1, 0, 1, 0, 0],
#              [0, 1, 0, 1, -4, 1, 0, 1, 0],
#              [0, 0, 1, 0, 1, -4, 0, 0, 1],
#              [0, 0, 0, 1, 0, 0, -4, 1, 0],
#              [0, 0, 0, 0, 1, 0, 1, -4, 1],
#              [0, 0, 0, 0, 0, 1, 0, 1, -4]], dtype= float)

A2 = -1 * A
print(A)
print(b)


x = myJacobi(A, b, 1, 10**-4)
print(x)
x2 = myJacobi(A2, b, 1, 10**-4)
print('\n\ncorrected \n\n',x2)
