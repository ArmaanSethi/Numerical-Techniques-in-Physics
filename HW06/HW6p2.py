#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: armaan
"""

import numpy as np
import matplotlib.pyplot as plt


def getMatrix(tvec):
    M = np.zeros((3,3))
    for i in range(3):
        M[i][0] = 1
        M[i][1] = tvec[i]
        M[i][2] = (1/2)*tvec[i]**2
    return M

def checkConditioning(tvec):
    M = getMatrix(tvec)
    det = np.linalg.det(M)
    norm = np.linalg.norm(M) #Frobenius norm	(same formula as textbook according to numpy docs)
#    print(det, norm)
#    print(M)
    return det/norm


def main(): 
    ratios_c = []
    ratios_d = []    
    
    #Part C
    x = np.linspace(0.1,5, num=200)
#    print(x)
    for t in x:
        ratios_c.append( checkConditioning(np.array([0,t,2*t])) )
        
#    print(ratios_c)
    plt.figure(figsize=(10,10))
    plt.xlabel("t")
    plt.ylabel("ratio")
    plt.title('Part C')
    plt.scatter(x, ratios_c, s=2)
    
    #Part D
    x = np.linspace(0,10, num=400)
    for t in x:
        ratios_d.append( checkConditioning(np.array([0,t,10])) )
    plt.figure(figsize=(10,10))
    plt.xlabel("t")
    plt.ylabel("ratio")
    plt.title('Part D')
    plt.scatter(x, ratios_d, s=2)
    
    #Part E
    M1 = getMatrix(np.array([0,5,10]))
    x1 = np.array([0.30, 4.425, 14.30]) #meters
    M2 = getMatrix(np.array([0,1,10]))
    x2 = np.array([0.30, 0.665, 14.30])
    xva1 = np.linalg.solve(M1, x1)
    print("Best Fit for Strategy 1", xva1)
    xva2 = np.linalg.solve(M2, x2)
    print("Best Fit for Strategy 1", xva2) 
    
    #Part F
#    dx = 0.005
#    lowerBound1 = np.zeros(3)
#    upperBound1 = np.zeros(3)
#    lowerBound1[0] = x1[0]
#    upperBound1[0] = x1[0]
#    lowerBound1[1] = x1[1] - dx
#    upperBound1[1] = x1[1] + dx
#    lowerBound1[2] = x1[2] - dx
#    upperBound1[2] = x1[2] + dx
#
#    what1 = np.linalg.solve(M1, lowerBound1)
#    what2 = np.linalg.solve(M1, upperBound1)
#    print(what1)
#    print(what2)
#    
#    lowerBound2 = np.zeros(3)
#    upperBound2 = np.zeros(3)
#    lowerBound2[0] = x2[0]
#    upperBound2[0] = x2[0]
#    lowerBound2[1] = x2[1] - dx
#    upperBound2[1] = x2[1] + dx
#    lowerBound2[2] = x2[2] - dx
#    upperBound2[2] = x2[2] + dx
#    what1 = np.linalg.solve(M2, lowerBound2)
#    what2 = np.linalg.solve(M2, upperBound2)
#    print(what1)
#    print(what2)

main()