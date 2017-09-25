# Homework 4, Problem 2
# Armaan Sethi

import numpy as np
import math
import sys

## module error
''' err(string).
    Prints 'string' and terminates program.
'''    
def err(string):
    print(string)
    input('Press return to exit')
    sys.exit(0)

## module swap
''' swapRows(v,i,j).
    Swaps rows i and j of a vector or matrix [v].

    swapCols(v,i,j).
    Swaps columns of matrix [v].
'''
def swapRows(v,i,j):
    if len(v.shape) == 1:
        v[i],v[j] = v[j],v[i]
    else:
        v[[i,j],:] = v[[j,i],:]
        
def swapCols(v,i,j):
    v[:,[i,j]] = v[:,[j,i]]
    
## module gaussPivot
''' x = gaussPivot(a,b,tol=1.0e-12).
    Solves [a]{x} = {b} by Gauss elimination with
    scaled row pivoting
'''    
def gaussPivot(a,b,tol=1.0e-12):
    n = len(b)
    
  # Set up scale factors
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i,:]))
            
    for k in range(0,n-1):
        
      # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol: err('Matrix is singular')
        if p != k:
            swapRows(b,k,p)
            swapRows(s,k,p)
            swapRows(a,k,p)
            
      # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    if abs(a[n-1,n-1]) < tol: err('Matrix is singular')
                   
  # Back substitution
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

## module newtonRaphson2
''' soln = newtonRaphson2(f,x,tol=1.0e-9).
    Solves the simultaneous equations f(x) = 0 by
    the Newton-Raphson method using {x} as the initial
    guess. Note that {f} and {x} are vectors.
'''
def newtonRaphson2(f,x,tol=1.0e-9):
    
    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1 - f0)/h
        return jac,f0
    
    for i in range(30):
        jac,f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < tol:
            return x
        dx = gaussPivot(jac,-f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < tol*max(max(abs(x)),1.0): return x
    print('Too many iterations')

# EDIT BELOW HERE

def get_Rs():
    return np.asarray( [ 6870., 6728., 6615. ] )

def get_thetas():
    return np.asarray( [ -30., 0., 30. ] ) * ( np.pi / 180. )

def f(x): 
    thetas = get_thetas()
    Rs = get_Rs()
    f = np.empty((len(thetas)))
    for i in range(len(thetas)):
        f[i] = x[0] / ( 1. + x[1] * np.sin( thetas[i] + x[2] ) ) - Rs[i]
    return f 

def main():
    c0 = get_Rs()[1]
    #come up with good e0 guess
    e0 = -.001195
    a0 = 0
    x0 = np.array([c0,e0,a0])
    #print("Starting values of C,e,alpha= \t", x0)
    xN = newtonRaphson2( f, np.asarray(x0) )
    print("Final values of C,e,alpha= \t", xN)
    theta_min = ( np.pi / 2 - xN[2] ) % ( 2 * np.pi ) 
    print("Theta Min (radians,degrees)= \t", theta_min, "Radians,\t", theta_min * ( 180. / np.pi ), "Degrees" )
    #theta_max = ( 3 / 2 * np.pi - xN[2] ) % ( 2 * np.pi ) 
    #print("Theta Max (radians,degrees)= \t", theta_max, "Radians,\t", theta_max * ( 180. / np.pi ), "Degrees" )
    
    
main()
