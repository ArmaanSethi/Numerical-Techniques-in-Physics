#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: armaan
"""
import numpy as np
import matplotlib.pyplot as plt

def triSolve(M, b, upperOrLower):
    n = M.shape[0]
    s = np.zeros([n], dtype=float)

    if(upperOrLower):
        #Upper
        for i in range(n):
            subtract = 0
            for j in range(i):
                subtract += s[n-j-1] * M[n-i-1][n-j-1]            
            s[n-1-i] = (b[n-1-i] - subtract)/M[n-1-i][n-1-i]
    else:
        #Lower
        for i in range(n):
            subtract = 0
            for j in range(0, i):
                subtract += s[j] * M[i][j]
            s[i] = (b[i]-subtract)/M[i][i]
            
            
#    print(s, s.T)
    #print("SOLVE:", np.matrix(s).T)
    return s.T #Transpose to make it column vector
        


def checkSolve(M, x, b):
    n = M.shape[0]
    s = np.zeros([n], dtype=float)
    for i in range(n):
        sumRow = 0
        for j in range(n):
            sumRow+= M[i][j]*x[j]
        s[i] = sumRow - b[i]
    
    #print("Residual", s)
    return s
        
    
def turnIntoTriangle(M):
    upperOrLower = np.random.randint(2)
    n = M.shape[0]
    if(upperOrLower):
        for i in range(1,n):
            for j in range(i):
                M[i][j] = 0
    else:
        for i in range(n):
            for j in range(i+1, n):
                M[i][j] = 0
                
    return M, upperOrLower

def main():
    #Test Values
#    Mu = np.array([[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1],[0,0,0,0,1]])
#    bu = np.array([5,4,3,2,1])
#    
#    Ml = np.array([[1,0,0,0,0],[1,1,0,0,0],[1,1,1,0,0],[1,1,1,1,0],[1,1,1,1,1]])
#    bl = np.array([1,3,6,10,15])
    
    
#    
    #PART C
    Mh = np.array([[9,0,0],[-4,2,0],[1,0,5]])
    bh = np.array([8,1,4])
    xh = triSolve(Mh, bh, 0)
    res = checkSolve(Mh, xh, bh)
    print("PART C")
    print("M\n", Mh)
    print("B\n",bh)
    print("x\n",xh)
    print("res\n",res)
    
    #PART D
    #Randomize
    print("\n\n\nPART D")
    n = int(abs(np.random.randn()*100)) + 1 #use a gaussian to choose the size of everything
    print("N: ", n)
    M = np.random.rand(n,n)
    b = np.random.rand(n)
    (M, upperOrLower) = turnIntoTriangle(M)
    print('M: \n', M,'\n\nb: \n',b,'\n\nUpperOrLower: ',upperOrLower)
    #Solve
    x = triSolve(M, b, 0)
    residual = checkSolve(M, x, b)
    print("\n\nx", x, '\nResidual', residual)

main()
