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
    iters = 0
    found_root = 0
   # max_iters = np.log(abs(xhi-xlo)/xtol)/np.log(2.0)#check this
    if((np.sign(f(xlo))) == (np.sign(f(xhi)))):
        print("Bisection cannot find the root, returning infinity instead")
        return(np.Infinity, np.Infinity)
    
    while((iters < nmax) and (found_root == 0)):
        midpoint = (xlo + xhi)/2
        #print(iters, midpoint)
        if(np.sign(f(midpoint)) == np.sign(f(xlo))):
            xlo = midpoint
        else:
            xhi = midpoint
        if((abs(f(xlo)) - xtol) <= 0.0):
            root = xlo
            found_root = 1
        if((abs(f(xhi)) - xtol) <= 0.0):
            root = xhi
            found_root = 1
        iters+=1
        
        #OUTPUT HERE TO SEE ITERATIONS AND EACH XLO
        #print(iters, xlo)

    return (root, iters)

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
    try:
        (root,iters) = rf_bisect(f, -1.0, 1.0, 1e-6, 25) 
        #plot
        x = np.arange(-1, 1, 0.01) 
        #add labels and legend
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("plot of: " + f.__name__)
        #plot it
        plt.grid(True, linestyle='--')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        #function
        plt.plot(x,f(x))
        
        print('\nRoot of ' + f.__name__ + ":   " + str(root))
        print('# iterations: ' + str(iters))
        print(f.__name__ + 'evaluated at root is: ' + str(f(root)))
        plt.figure()
    except Exception as e:
        print("yo we hit an error", e)
    



main(f1)
main(f2)
main(f3)
main(f4)

    