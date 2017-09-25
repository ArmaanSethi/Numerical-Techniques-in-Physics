#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:34:25 2017

@author: Armaan Sethi
"""

import numpy as np
import matplotlib.pyplot as plt

def main_a():
    #set domain for plot
    x = np.arange(-5, 5, 0.01) 
    #add labels and legend
    plt.xlabel("x")
    plt.ylabel("tanh(x)")
    plt.title("Main_a")
    #plot it
    plt.grid(True, linestyle='--')
    plt.plot(x,np.tanh(x))

def plotfunc(a):
    x = np.arange(-5, 5, 0.01)
    plt.plot(x, np.tanh(a*x))
    
def main_b():
    #declare different a's
    a1 = 0.5
    a2 = 1.3
    a3 = 2.2
    #plot the a's
    plotfunc(a1)
    plotfunc(a2)
    plotfunc(a3)
    #create a legend
    plt.grid(True, linestyle='--')
    plt.legend((str(a1), str(a2),str(a3)), loc= 0)
    plt.title("Main_b")

main_a()
#seperate the plots
plt.figure()
main_b()