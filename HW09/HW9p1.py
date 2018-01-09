#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:49:44 2017

@author: armaan
"""
import numpy as np
import matplotlib.pyplot as plt

def SimpsonIntegrate(f, a, b, n):
    #Make sure n is not divisible by 6
    while n%6 == 0:
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

def func1(x):
    if x == 0:
        return 1
    else:
        return np.log(1+x)/x
    
def main():

    x_list = []
    n_list = [10, 30, 100, 300, 1000, 3000, 10**4, 3*10**4, 10**5]
    for n in n_list:
        x_list.append( SimpsonIntegrate(func1, 0, 1, n) )
    
    error_list_i1 = []
    error_list_i2 = []
    error_list_i3 = []
    error_list_i1_a = []
    error_list_i2_a = []
    error_list_i3_a = []
    for i in range(1, len(x_list)):
        error_list_i1.append( abs(x_list[i][0]-x_list[i-1][0]) )
        error_list_i2.append( abs(x_list[i][1]-x_list[i-1][1]) )
        error_list_i3.append( abs(x_list[i][2]-x_list[i-1][2]) )
    for i in range(len(x_list)):
        error_list_i1_a.append( abs(x_list[i][0] - np.pi**2/12) )
        error_list_i2_a.append( abs(x_list[i][1] - np.pi**2/12) )
        error_list_i3_a.append( abs(x_list[i][2] - np.pi**2/12) )
        
        
    """PLOT STUFF"""
    x = np.linspace(0,1, num = 200)
    y = []
    for x_val in x:
        y.append(func1(x_val))
        
        
    plt.figure(figsize = (8,8))
    plt.scatter(x, y, s= 3)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Integrand Over Range of Limits")
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    
    
    plt.figure(figsize = (8,8))
    
    plt.plot(range(1, len(error_list_i1)+1), error_list_i1)
    plt.plot(range(1, len(error_list_i2)+1), error_list_i2)
    plt.plot(range(1, len(error_list_i3)+1), error_list_i3)
    plt.xlabel("i")
    plt.ylabel("Error")
    plt.title("Error vs Iterations of Method")
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(("Trapezoidal","Simpson's 1/3","Simpson's 3/8"))
        
    
    plt.figure(figsize = (8,8))
    
    plt.loglog(n_list[:len(n_list)-1], error_list_i1)
    plt.loglog(n_list[:len(n_list)-1], error_list_i2)
    plt.loglog(n_list[:len(n_list)-1], error_list_i3)
    plt.xlabel("n")
    plt.ylabel("Error")
    plt.title("Error vs N LogLog Plot")
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(("Trapezoidal","Simpson's 1/3","Simpson's 3/8"))
    
    
    plt.figure(figsize = (8,8))

    plt.loglog(n_list[:len(n_list)], error_list_i1_a)
    plt.loglog(n_list[:len(n_list)], error_list_i2_a)
    plt.loglog(n_list[:len(n_list)], error_list_i3_a)
    plt.xlabel("n")
    plt.ylabel("Error")
    plt.title("Accuracy: Error vs N using Real Value")
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(("Trapezoidal","Simpson's 1/3","Simpson's 3/8"))
    
main()