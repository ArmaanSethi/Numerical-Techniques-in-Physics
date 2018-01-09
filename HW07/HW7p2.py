#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:03:18 2017

@author: armaan
"""
import numpy as np
import scipy 

def LUdecomp(Ain,bin):
    #Identical to GaussElimin except for the few noted lines
    n=len(bin)
    A = Ain.copy() 
    D = np.zeros((n,n))
    L = np.zeros((n,n))#added this line to create L
    b = bin.copy()
    for i in range(0,n-1):
        for j in range(i+1,n):
            c = A[j,i]/A[i,i]  
            A[j,i] = 0.0  
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n]  
            b[j] = b[j]-c*b[i]  
            L[j,i] = c#ADDED THIS LINE TO MAKE L
            
        L[i,i] = 1#make the diagonals 1
        c2 = A[i,i]
        A[i]  = A[i]*(1/c2)
        D[i,i] = c2
    
    c2 = A[n-1,n-1]
    A[n-1]  = A[n-1]*(1/c2)
    D[n-1,n-1] = c2
    L[n-1,n-1] = 1
    return (A, L, D, b)   


def main():
    a1 = np.array([[4,-2,1],[-3,-1,4],[1,-1,3]], dtype=float)
    b1 = np.array([15, 8, 13], dtype=float)
    
    a2 = np.array([[2,2,3,2],[0,2,0,1],[4,-3,0,1],[6,1,-6,5]], dtype = float)
    b2 = np.array([-2,0,-7,6], dtype = float)
    
    
    print('\na1\n', a1)
    print('b1\n', b1)

    (u1, l1, d1, b1) = LUdecomp(a1, b1)
    print("\nU1\n", u1, "\nL1\n", l1,'\nb1\n', b1,'\nd1\n', d1, '\nCheck\n', np.dot(np.dot(l1,d1), u1))


    print('\n\na2\n', a2)
    print('b2\n', b2)
    (u2, l2, d2, b2) = LUdecomp(a2, b2)
    print("\nU2\n", u2, "\nL2\n", l2,'\nb2\n', b2, '\nd2\n', d2, '\nCheck\n', np.dot(np.dot(l2,d2), u2))
    
    print(1/d2)
main()