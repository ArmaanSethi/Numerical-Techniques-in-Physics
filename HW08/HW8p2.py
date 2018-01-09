#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:18:51 2017

@author: armaan
"""
import numpy as np
import matplotlib.pyplot as plt


def CreateSystem():
    n = 100
    system = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if(i+1 == j):
                system[i][j] = 1 
            if(i == j):
                system[i][j] = -2
            if(i-1 == j):
                system[i][j] = 1
    system[0][n-1] = 1
    system[n-1][0] = 1
    return(system)

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
#    print('l', L)
#    print('d', D)
#    print('u', U)
#    print('ldu', L+D+U)
#    print('a', A)
    Dinv = np.zeros((n,n))
    for i in range(n):
        Dinv[i,i] = 1/(D[i,i])

        
    x = np.zeros((n,1))
    x0 = np.zeros((n,1))
    
    for i in range(n):
        x0[i,0] = b[i]/A[i][i] #Create Initial Guess
        
    
    LU = L+U
    iters = 0
    for i in range(n):
        while (abs(x[i] - x0[i])) > tol:
            x0 = x
            step1 = np.dot(LU, x0)
            step2 = np.dot((-1*Dinv), step1)
            step3 = np.dot(Dinv, b)
            x = w*(step2+step3) + (1-w)*x0
    #        print('max_diff', max_diff)
            iters+=1
#            print(iters)
    return (x, iters)

def analytical_sol(x):
    return 4*np.pi*np.sin(x)




A = CreateSystem()
h = np.linspace(0, 2*np.pi, 100)
b = np.zeros((100,1))
for i in range(len(h)):
    b[i] = -4 * np.pi * np.sin(h[i])
    
#print(b)
#print(A)


#Numerical Solution
#x_numerical = myJacobi(A, b , 1., 10**-4)
#print(x_numerical


 #in order to compare to analytical solution
#print(np.linalg.solve(A,b))


plt.figure()
plt.xlabel("x")
plt.ylabel("Phi")
plt.title("PART C")
plt.grid(True, linestyle='--')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
x_analytical = np.linspace(0, 2*np.pi, 100)
plt.scatter(x_analytical, analytical_sol(x_analytical), s = 3)
#plt.plot(x_analytical, x_numerical)    #UNCOMMENT THIS TO TEST MY NUMERICAL SOLUTION
plt.scatter(x_analytical, np.linalg.solve(A,b), s= 3)
plt.legend(('Analytical', 'Numerical'), loc='best')
