# Template File for Homework 2, Problem 2
# PHYS 331
# Armaan Sethi
import numpy as np
import matplotlib.pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):
#Computes the value of the root for function f bracketed in the domain [xlo, xhi]. 
# PARAMETERS:
#   f     --  (function) The one-dimensional function to evaluate a root of.
#   xlo   --  (float) The lower limit of the bracket.
#   xhi   --  (float) The upper limit of the bracket.
#   xtol  --  (float) The tolerance the calculated root should achieve.
#   nmax  --  (int) The maximum number of iterations allowed.

# RETURNS: (tuple(float, int)) A root of f that meets the tolerance tol the number 
# of iteratons required to converge.
    
#----> Implement your solution for rf_bisect here <-------
    root = []
    iters = 0
    midpoints = []
    f_midpoints = []
    
    if((np.sign(f(xlo))) == np.sign(xhi)):
        print("Bisection cannot find the root")
        return(np.Infinity, np.Infinity)
    
    while((iters < nmax) and (root == [])):
        midpoint = (xlo + xhi)/2.0
        midpoints.append(midpoint)
        f_midpoints.append(f(midpoint))
        #print(iters, midpoint)
        if(np.sign(f(midpoint)) == np.sign(f(xlo))):
            xlo = midpoint
        else:
            xhi = midpoint
        if((abs(f(xlo)) - xtol) <= 0.0):
            root = xlo
        if((abs(f(xhi)) - xtol) <= 0.0):
            root = xhi
        iters+=1


    return (midpoints, f_midpoints)

# Functions f1, f2, f3, and f4 that may be used to test your implementation of rf_bisect.
def f1(x):
    return 3 * x + np.sin(x) - np.exp(x)

def f2(x):
    return x**3

def f3(x):
    return np.sin(1. / (x + 0.01))

def f4(x):
    return 1. / (x - 0.5)

def main(f):
# Example: Find the root of f2(x) and print the result.
    (midpoints,f_midpoints) = rf_bisect(f, -1., 1., 1e-12, 25) 
    #plot
    x = np.arange(-1, 1, 0.01) 
    #add labels and legend
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("midpoints shown on " + f.__name__)
    #plot it
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.ylim(-0.25,0.25)
    #function
    plt.scatter(midpoints, f_midpoints)

    plt.plot(x,f(x))
    plt.figure()
    
    #create list of errors
    error_list = []
    for v in f_midpoints:
        error_list.append(abs(v-f_midpoints[len(f_midpoints)-1]))
        
    #come up with domain for the error plot 
    a = range(1, len(midpoints)+1)
    print(a)
    #plot
    plt.scatter(a, error_list)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.xlabel("x")
    plt.ylabel("error")
    plt.title("error")
    plt.figure()

main(f1)
main(f2)
main(f3)
main(f4)

    