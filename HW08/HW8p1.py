#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 01:10:29 2017

@author: armaan
"""

import numpy as np
import matplotlib.pyplot as plt

def myJacobi(Ain,bin,win,tolin):
    n = len(bin)
    R = np.zeros([n,n])
    Dinv = np.zeros([n,n])
    xold = np.zeros([n,1])
    for i in range(0,n):
        Dinv[i,i]=1./Ain[i,i]
        xold[i] = bin[i]/Ain[i,i]
        for j in range(0,n):
            if j != i:
                R[i,j]=Ain[i,j]
    xnew = win*(np.dot(-Dinv,np.dot(R,xold))+np.dot(Dinv,bin))+(1-win)*xold
    errflag = 0
    nits = 1
    while errflag == 0:
        nits += 1
        xold = xnew.copy()
        xnew = win*(np.dot(-Dinv,np.dot(R,xold))+np.dot(Dinv,bin))+(1-win)*xold
        errflag = 1
        for i in range(0,n): # ALL elements must be < tolerance to exit while loop
            if np.abs(xold[i]-xnew[i])>tolin:
                errflag = 0
    return (nits,xnew)

def myJacobi2(A, b, w, tol):    
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
#    print('l', L)
#    print('d', D)
#    print('u', U)
#    print('ldu', L+D+U)
#    print('a', A)
    Dinv = np.zeros((n,n))
    for i in range(n):
        Dinv[i,i] = 1/(D[i,i])

        
    new_x = np.zeros((n,1))
    x0 = np.zeros((n,1))
    
    for i in range(n):
        x0[i,0] = b[i]/A[i][i] #Create Initial Guess
        
    
    LU = L+U
    iters = 0
    for i in range(n): #in order to not use np.all()
        while (abs(new_x[i] - x0[i])) > tol:
            x0 = new_x
            step1 = np.dot(LU, x0)
            step2 = np.dot((-1*Dinv), step1)
            step3 = np.dot(Dinv, b)
            new_x = w*(step2+step3) + (1-w)*x0
    #        print('max_diff', max_diff)
            iters+=1
#            print(iters)
    return (new_x, iters)
    

A_1 = np.array([[1.01, 0.99],
              [0.99, 1.01]])
B_1 = np.array([[2.0],[2.0]])
 
A_2 = np.array([[1.5, 0.5],
              [0.5, 1.5]])
B_2 = np.array([[2.0],[2.0]])


A_3 = np.array([[9.,10.,2.],
                [1.,6.,3.],
                [10.,-1.,2.]])
    
B_3 = np.array([[7.],[ 8.],[ 1.]])

x_1 = myJacobi(A_1, B_1, 1.0, 10**-4)
x_2 = myJacobi(A_2, B_2, 1.0, 10**-4)
w = 1.0
tol = 1e-4

(nout, xout) = myJacobi(A_1, B_1, w, tol)
print(xout, nout)

(nout, xout) = myJacobi(A_2, B_2, w, tol)
print(xout, nout)

print(np.linalg.solve(A_1, B_1))

#
#
#
##PART B
#w_list = np.linspace(0,2, num=50)
#x_3 = []
#for w in w_list:
#    a = myJacobi(A_3, B_3, w, 10**-4) 
#    print("Hard At Work")
#    x_3.append( a )
#
#
#print('\n\n')
#print ('x_1\n',x_1)
#print ('x_2\n',x_2)
#
#
#print('Solution 1: \n', np.linalg.solve(A_1, B_1))
#print('Solution 2: \n', np.linalg.solve(A_2, B_2))
#solution3 =  np.linalg.solve(A_3, B_3)
#print('Solution 3: \n',solution3)
#
#good_points = []
#good_w = []
#good_iterations = []
#for i in range(len(x_3)):
#    if (x_3[i][0][0] - solution3[0] < 10**-1) and  (x_3[i][0][1] - solution3[1] < 10**-1) and  (x_3[i][0][2] - solution3[2] < 10**-1):
#        good_points.append(x_3[i][0])
#        good_iterations.append(x_3[i][1])
#        good_w.append(w_list[i])
#        
##print(good_iterations, len(good_iterations))
##print(good_w, len(good_w))
#
#plt.figure()
#plt.xlabel("w value")
#plt.ylabel("iterations")
#plt.title("PART B")
#plt.grid(True, linestyle='--')
#plt.axhline(y=0, color='k')
#plt.axvline(x=0, color='k')
#
#plt.scatter(good_w, good_iterations)
#
#
#
