#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: armaan
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def  ModelSpectrum(c1,c2,v01,v02,g1,g2,v):
    L1 = (1/(np.pi))*(1/2)*g1 * ((v-v01)**2+((1/2)*(g1))**2)**-1
    L2 = (np.pi**-1)*(1/2)*g2* ((v-v02)**2+((1/2)*(g2))**2)**-1
    return c1*L1 + c2*L2

def ModelSpectrum2(x,v):
    L1 = (1/(np.pi))*(1/2)*x[4] * ((v-x[2])**2+((1/2)*(x[4]))**2)**-1
    L2 = (np.pi**-1)*(1/2)*x[5]* ((v-x[3])**2+((1/2)*(x[5]))**2)**-1
    return x[0]*L1 + x[1]*L2

def ModelSpectrum3(x,v,Sv):
    L1 = (1/(np.pi))*(1/2)*x[4] * ((v-x[2])**2+((1/2)*(x[4]))**2)**-1
    L2 = (np.pi**-1)*(1/2)*x[5]* ((v-x[3])**2+((1/2)*(x[5]))**2)**-1
    return (x[0]*L1 + x[1]*L2)-Sv
    
    
def main():
    #Part A
    data = np.loadtxt(open("HW5p3data.csv", "rb"), delimiter=",")    

    #Part B
    v = []
    sv = []
    for i in range(len(data)):
        v.append(data[i][0])
        sv.append(data[i][1])
        
    plt.figure()
    plt.xlabel("v")
    plt.ylabel("sv")
    plt.title('Part B')
    plt.scatter(v, sv, s = 3)
    #Part C
    plt.figure()
    plt.xlabel("v")
    plt.ylabel("sv")
    plt.title('Part C')
    plt.scatter(v, ModelSpectrum(0.2,0.1,20200,20600,6,6,np.asanyarray(v)), s=3)
    #Part D
    plt.figure()
    plt.xlabel("v")
    plt.ylabel("sv")
    plt.title('Part D')
    plt.scatter(v, ModelSpectrum2([0.2,0.1,20200,20600,6,6], np.asarray(v)), s=3)
    #Part E
    plt.figure()
    plt.xlabel("v")
    plt.ylabel("sv")
    plt.title('Part E')
    plt.scatter(v, ModelSpectrum3([0.2,0.1,20200,20600,6,6], np.asarray(v), np.asarray(sv)), s=3)
    #Part F
    res = opt.leastsq(ModelSpectrum3, [0.2,0.1,20200,20600,6,6], args = (v, sv))
    #Part G
    x1 = res[0]
    print(x1)
    plt.figure()
    plt.xlabel("v")
    plt.ylabel("sv")
    plt.title('Part G')
    plt.plot(v, ModelSpectrum3(x1,v,sv))
    #Part H
    plt.figure()
    plt.xlabel("v")
    plt.ylabel("sv")
    plt.title('Part H')
    vmesh = np.arange(20000,21000.01, 1)
    plt.scatter(v, sv, s = 4, color = 'g')
    plt.plot(vmesh, ModelSpectrum2(x1,vmesh))
        
main()
