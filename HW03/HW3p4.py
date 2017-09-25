# Template File for Homework 3, Problem 4
# PHYS 331
# Amy Oldenburg

import numpy as np
import matplotlib.pyplot as plt
## module newtonRaphson

# has been modified to strip bisection aspects of the code
# is generally UNSAFE, but can be used for specific case of Problem 4
def newtonRaphsonMOD(f,df,a,b): # YES YOU MAY MODIFY!
    from numpy import sign
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)         
    error_list = []           
    for i in range(10):
        fx = f(x)
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        previous_x = x
        x = x + dx
        error_list.append(abs(x-previous_x))

    return (error_list, x)

    

#f(x)=(x-10)(x+25)(x2+45) 
def f(x):
    return (x-10)*(x+25)*(x**2+45)
def df(x):
    return 675 - 410*x + 45*x**2 + 4*x**3

def plot(f):
    x = np.arange(-1,  16, 0.01) 
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f.__name__)
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    #only relavent when plotting derivative
    if(f.__name__ == "df"):
        plt.axhline(y=1, color='b')
    plt.axvline(x=0, color='k')
    #plt.ylim(-2,2)#plot it once without this line to get an idea of how the functions look, then use this to better examine roots and df < 1
    plt.plot(x,f(x))

def main():
    plot(f)
    plt.figure()
    plot(df)
    plt.figure()
    (errors, root) = newtonRaphsonMOD(f,df,0,15)
    print("errors:\t", errors)
    print("root:\t", root)
    
    iterations = range(1, len(errors)+1)
    #plot
    plt.scatter(iterations, errors)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.xlabel("Iterations")
    plt.ylabel("Error")
    plt.title("Error vs Iterations")

main()