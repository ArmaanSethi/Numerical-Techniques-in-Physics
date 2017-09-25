#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:03:51 2017

@author: armaan
"""
import numpy as np
import matplotlib.pyplot as plt
    
def func(x):
    return x**5 - 3*x**3 + 15*x**2 + 29*x + 9

def dfunc(x):
    return 5*x**4 - 9*x**2 + 30*x +29

def gNewt(x):
    return x - func(x)/dfunc(x)

def dgNewt(x):
    return (2 * (15 - 9*x + 10*x**3) * (9 + 29*x + 15*x**2 - 3*x**3 + x**5))/(29 + 30*x - 9*x**2 + 5*x**4)**2

def g1(x):
    return (x**4 - 3*x**2 + 15*x**1 + 9)/(-29)

def dg1(x):
    return (-15 + 6*x - 4*x**3)/29

def fixed_pt(g,xstart,tol):
    x = g(xstart)
    while(abs(g(x))-x < tol):
        x = g(x)
    return x


#x_new = x_old - f(x)/f'(x)
    
def plot(f):
    #create domain
    x = np.arange(-2.5,  0, 0.01) 
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f.__name__)
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    #only relavent when plotting derivative
    if(f.__name__[0] == 'd'):
        plt.axhline(y=1, color='b')
    plt.ylim(-2,2)#plot it once without this line to get an idea of how the functions look, then use this to better examine roots and df < 1
    plt.plot(x,f(x))

    
def main():
    plot(func)
    plt.figure()
    plot(dgNewt)
    plt.figure()
    plot(dg1)
    
    print("gNewt\tstarting at  0\t", fixed_pt(gNewt, -0, 1e-20))
    print("gNewt\tstarting at -1\t", fixed_pt(gNewt, -1, 1e-20))
    print("gNewt\tstarting at -2\t", fixed_pt(gNewt, -2, 1e-20))
    print("g1\tstarting at  0\t", fixed_pt(g1, -0, 1e-20))
    print("g1\tstarting at -1\t", fixed_pt(g1, -1, 1e-20))
    print("g1\tstarting at -2\t", fixed_pt(g1, -2, 1e-20))

main()