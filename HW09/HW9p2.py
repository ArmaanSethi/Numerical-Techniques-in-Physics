#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:23:57 2017

@author: armaan
"""
import numpy as np
import matplotlib.pyplot as plt

def SimpsonIntegrate(f, a, b, n):
    #Make sure n is not divisible by 6
    if n%6 == 0:
        n+=1
        
    dx = float(b-a)/n
    xall = np.linspace(a,b,n+1) 
    """Trapezoidal"""
    Trap = (f(a) + f(b))/2
    for i in range(len(xall)-1):
        Trap += f(xall[i])
        
    Trap = Trap*dx
    """Simpson's 1/3"""
    Sim1_3 = f(a)+f(b)
    for i in range(1,len(xall)-1):
        if i%2 == 1:
            Sim1_3 += 4.*f(xall[i])
        else:
            Sim1_3 += 2.*f(xall[i])
    Sim1_3 = Sim1_3*dx/3.
    
    """Simposon's 3/8"""
    Sim3_8 = f(a) + f(b)
    for i in range(1,len(xall)-1):
        if i%3 == 0:
            Sim3_8 += 2.*f(xall[i])
        else:
            Sim3_8 += 3.*f(xall[i])
            
    Sim3_8 = Sim3_8*0.375*dx
    
    return(Trap, Sim1_3, Sim3_8)

def func3(y):
    return 2*y**2 * (2-y**2)**(0.5)

def func2(x):
    return (1-x**2)**(0.5)

def main():
    n = 1000
    x = np.linspace(0,1, num = 200)
    plt.figure(figsize = (8,8))
    plt.scatter(x, func2(x), s= 3)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Func2 Over Range of Limits")
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(("sqrt(1-x^2)",))
    
    
    plt.figure(figsize = (8,8))
    plt.scatter(x, func3(x), s= 3)
    plt.xlabel("y")
    plt.ylabel("f(y)")
    plt.title("Func3 Over Range of Limits")
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(("2y^2*sqrt(2-y^2)",))
    
    Ix = SimpsonIntegrate(func2, 0, 1, n)
    Iy = SimpsonIntegrate(func3, 0, 1, n)
    v = np.pi/4 #Actual Value
    
    print("\nFunc2: sqrt(1-x^2)" )
    print("Trapezoidal", Ix[0], "\tError: ", Ix[0]-v, "\nSimpson's 1/3", 
          Ix[1], "\tError: ", Ix[1]-v, "\nSimpson's 3/8", Ix[2],"\tError: ", Ix[2]-v,  )
    
    print("\nFunc3: 2y^2*sqrt(2-y^2)")
    print("Trapezoidal", Iy[0], "\tError: ", Iy[0]-v, "\nSimpson's 1/3", 
          Iy[1], "\tError: ", Iy[1]-v, "\nSimpson's 3/8", Iy[2],"\tError: ", Iy[2]-v,  )


main()
