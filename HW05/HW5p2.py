#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: armaan
"""
import numpy as np
import matplotlib.pyplot as plt

def f1(x,y):
    return (x**2)-(y**2)
def EC(x,y):
    return x**2-x+y**2+y

def sample(x, y, f):
    #print(my_ary)
    my_ary = np.zeros(shape=(len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            my_ary[j][i] = f(x[i],y[j])
    
    #print(my_ary)
    plt.figure()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f.__name__)
    plt.imshow(my_ary,  extent=([-1,1,1,-1]))
    plt.colorbar()
    #plt.figure()
    #plt.imshow(my_ary, interpolation = 'bilinear')
    return my_ary
 
def bilinear2D(xsamp,ysamp,xdata,ydata,zdata):
    new_array = np.zeros(shape = (len(ysamp),len(xsamp)))
    k = 0
    l = 0
    for i in range(len(xsamp)-1):
        l=0
        for j in range(len(ysamp)-1):
            if(xsamp[i] > xdata[k+1]):
                k+=1
            if(ysamp[j] > ydata[l+1]):
                l+=1

            y1 = zdata[k][l]
            y2 = zdata[k+1][l]
            y3 = zdata[k+1][l+1]
            y4 = zdata[k][l+1]
            
            t = (xsamp[i] - xdata[k])/(xdata[k+1]-xdata[k])
            u = (ysamp[j] - ydata[l])/(ydata[l+1]-ydata[l])
            new_array[i,j] = (1-t)*(1-u)*y1 + t*(1-u)*y2 + t*y3*u + (1-t)*u*y4
            
            
    plt.figure()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Interpolation')
    plt.imshow(new_array, extent=([-1,1,1,-1]))   
    plt.colorbar()         

def main():
    
    #Part A
    xdata = np.arange(-1,1.01,0.2)
    ydata = np.arange(-1,1.01,0.2)
    
    #my_ary = np.zeros(shape=(len(xdata),len(ydata)))
    A = sample(xdata, ydata, f1)
    EC_A = sample(xdata, ydata, EC)
    #Part B
    x_sample = np.arange(-1,1.000001,0.01)
    y_sample = np.arange(-1,1.000001,0.01)
    bilinear2D(x_sample,y_sample,xdata,ydata,A)
    bilinear2D(x_sample,y_sample,xdata,ydata,EC_A)
    
    

main()
