#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:32:53 2017

@author: armaan
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

def CreateSystem(kvec, mvec):
    n = mvec.shape[0]
    system = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if(i+1 == j):
#                print(i,j, kvec[j])
                system[i][j] = kvec[j]/mvec[i] 
            if(i == j):
#                print(i,j, -kvec[i] - kvec[i+1])
                system[i][j] = (-kvec[i] - kvec[i+1])/mvec[i]
            if(i-1 == j):
                system[i][j] = kvec[i]/mvec[i]
#                print(i,j, kvec[i])

    return(system)
    
def main():
    #my test values for part B
    k = np.array([6,5,4,3,2,1,7])
    m = np.array([1,2,3,4,5,6])
    CreateSystem(k, m)
    
    #Part C
    k_c = np.array([1,1,1])
    m_c = np.array([1,1])
    A_c = CreateSystem(k_c, m_c)    
    print('\nA\n', A_c)
    (E_c, V_c) = np.linalg.eig(A_c)
    print( '\nE\n', E_c, '\nV\n',   V_c)
    
    #Part D
    k_d = np.array([1,1,1,1])
    m_d = np.array([1,1,1])
    A_d = CreateSystem(k_d, m_d)    
    print('\nA\n', A_d)
    (E_d, V_d) = np.linalg.eig(A_d)
    print( '\nE\n', E_d, '\nV\n',   V_d)
    w = []
    for eigen in E_d:
        w .append( cmath.sqrt(eigen) )
        
    print('Angular Velocities', w)
    #Part E
    k_e = np.full((1001), 1)
    m_e = np.zeros((1000))
    
    for i in range(1000):
        if (i%2 == 0):
            m_e[i] = 1.5
        else:
            m_e[i] = 1

    A_e = CreateSystem(k_e, m_e)

    (E_e, V_e) = np.linalg.eig(A_e)
    plt.figure(figsize = (10,10))
    plt.hist(E_e, bins='sqrt') 
    plt.title("Masses of 1 an 1.5")
    plt.show()
#    print(E_e)
    k_f = np.full((1001), 1)
    m_f = np.zeros((1000))
    
    for i in range(1000):
        if (i%2 == 0):
            m_f[i] = 1.2
        else:
            m_f[i] = 1
    A_f = CreateSystem(k_f, m_f)
#    print('\n\nA\n',A_e)
    (E_f, V_f) = np.linalg.eig(A_f)

    plt.figure(figsize = (10,10))
    plt.hist(E_f, bins='sqrt') 
    plt.title("Masses of 1 an 1.2")
    plt.show()

    
main()
    