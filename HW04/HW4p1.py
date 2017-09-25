#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:50:30 2017

@author: armaan
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    #z = x+iy
    #(xi+y)**3-1
    Re = (x**3) - 3*x*(y**2) - 1
    Im = -y**3 + 3*x**2*y
    return np.array([Re, Im], dtype = float)

def Jinv(x,y):
    #First Jacob
    jacob = np.zeros((2,2), dtype = float)
    
    jacob[0][0] = 3*x**2 - 3*y**2
    jacob[0][1] = 6*x*y
    jacob[1][0] = -6*x*y
    jacob[1][1]= -3*y**2 + 3*x**2
    
    #Then inverse
    det_inv = 1/(jacob[0][0]*jacob[1][1]-jacob[0][1]*jacob[1][0])
    
    jacob_inv = np.zeros((2,2), dtype = float)
    
    jacob_inv[0][0] = jacob[1][1]*det_inv
    jacob_inv[1][1] = jacob[0][0]*det_inv
    jacob_inv[1][0] = -det_inv*jacob[1][0]
    jacob_inv[0][1] = -det_inv*jacob[0][1]
#    jacob_inv_func = np.linalg.inv(jacob) # use np.linalg.inv because they take care of edge cases such as 0 determinants etc.
    return jacob_inv

def rf_newton2d(f_system,Jinv_system,x0,y0,tol,maxiter):
    f = f_system(x0,y0)
    Jinv = Jinv_system(x0,y0)
    iters = 0
    while(iters < maxiter):
        f = f_system(x0,y0)     
        Jinv = Jinv_system(x0,y0)
        dx = -1*f[0] * Jinv[0][0] + -1*f[1] * Jinv[1][0]
        dy = -1*f[0] * Jinv[0][1] + -1*f[1] * Jinv[1][1]
        if(np.sqrt(dx**2+dy**2) < tol):
            return (np.array([x0,y0]), iters)
        x0+=dx
        y0+=dy
        iters+=1
    
    return (np.array([x0,y0]), iters)

#Extra Credjt Function
def color_plot(tol = 0.01):
    #domain
    x = np.arange(-1,1+tol,tol)
    y = np.arange(-1,1+tol,tol)
    
    root1_x = []
    root1_y = []
    root2_x = []
    root2_y = []
    root3_x = []
    root3_y = []
    root4_x = []
    root4_y = []
    
    for i in range(len(x)): 
        for j in range(len(y)):
            (cur_root, num_iter) = rf_newton2d(f, Jinv,x[i],y[j],10**-3, 30)
            if((abs(cur_root[0] - (1.0)) < tol) and (abs(cur_root[1] - (0.0)) < tol)):
                #print('converges to Root 1', x[i],y[j])
                root1_x.append(x[i])
                root1_y.append(y[j])
            elif((abs(cur_root[0] - (-0.5)) < tol) and (abs(cur_root[1] - (0.8660254)) < tol)):
                #print('converges to Rpotn2', x[i],y[j])
                root2_x.append(x[i])
                root2_y.append(y[j])
            elif((abs(cur_root[0] - (-0.5)) < tol) and (abs(cur_root[1] - (-0.8660254)) < tol)):
                #print('converges to Root 3', x[i],y[j])
                root3_x.append(x[i])
                root3_y.append(y[j])
            else:
                #print('converges to no roots', x[i],y[j])
                root4_x.append(x[i])
                root4_y.append(y[i])
                
    #PLOT
    plt.figure(figsize=(10,10))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Fractal 3 Color Image')
    plt.ylim(-1,1)#plot it once without this line to get an idea of how the functions look, then use this to better examine roots and df < 1
    plt.xlim(-1,1)
    plt.scatter(root1_x, root1_y, color='c', s = 4)
    plt.scatter(root2_x, root2_y, color='m', s = 4)
    plt.scatter(root3_x, root3_y, color='y', s = 4)
    plt.scatter(root4_x, root4_y, color='w', s = 4)
    plt.legend(('1 + 0i' , '0 - 0.5i', '0 + 0.5i', 'Does not converge to a root'), loc=2)

def main():
    print("Root 1 ([x, iy], iterations):\t", rf_newton2d(f,  Jinv, 1.01, 0.01, 10**-3, 30))
    print("Root 2 ([x, iy], iterations):\t", rf_newton2d(f,  Jinv, -0.51, 0.866, 10**-3, 30))
    print("Root 3 ([x, iy], iterations):\t", rf_newton2d(f,  Jinv, -0.51, -0.866, 10**-3, 30))
    color_plot()
    
main()
