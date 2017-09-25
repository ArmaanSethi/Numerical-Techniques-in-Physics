# Template File for Homework 3, Problem 3
# PHYS 331
# Amy Oldenburg

## module newtonRaphson
''' root = newtonRaphson(f,df,a,b,tol).
    Finds a root of f(x) = 0 by combining the Newton-Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).   
'''    
import numpy as np
import matplotlib.pyplot as plt


def newtonRaphson(f,df,a,b,tol): # DO NOT MODIFY
    from numpy import sign
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)                    
    for i in range(30):
        fx = f(x)
        if fx == 0.0: return x
      # Tighten the brackets on the root 
        if sign(fa) != sign(fx): b = x  
        else: a = x
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
      # If the result is outside the brackets, use bisection  
        if (b - x)*(x - a) < 0.0:  
            dx = 0.5*(b - a)                      
            x = a + dx
      # Check for convergence     
        if abs(dx) < tol*max(abs(b),1.0): return x
    print('Too many iterations in Newton-Raphson')
    
## ADD your code below this line
    
def f(x): 
    return np.cosh(x) * np.cos(x) + 1 
def df(x):
    return np.sinh(x) * np.cos(x) - np.cosh(x) * np.sin(x) 

def plot(f):
    x = np.arange(-1,  10, 0.01) 
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f.__name__)
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    #only relavent when plotting derivative
    if(f.__name__ == "df"):
        plt.axhline(y=1, color='b')
    plt.axvline(x=0, color='k')
    plt.ylim(-2,2)#plot it once without this line to get an idea of how the functions look, then use this to better examine roots and df < 1
    plt.plot(x,f(x))

def main():
    #Length
    L = 0.9 #meters
    #width
    b = .025 #meters
    #height
    h = .0025 #meters
    #Intertia
    I = b*h**3/12
    #E
    E = 200*10**9 #Pa
    #density
    d = 7850 #kg/m^3
    #Volume
    V = L*b*h #m^3
    #mass
    m = V * d#kg
    #plot things to understand where to find roots
    plot(f)
    plt.figure()
    plot(df)
    
    
    #find roots
    firstRoot = newtonRaphson( f, df, 1.5, 2.5, 1e-12 )
    secondRoot = newtonRaphson( f, df, 4.0, 5.0, 1e-12)
    print("First Root:\t", firstRoot)
    print("Second Root:\t", secondRoot)
    denominator = ( ( 2 * np.pi )**2 * m * L**3 ) / ( E * I ) # all constanst now beta^4 = C f^2 
    f_1 = np.sqrt( ( firstRoot**4 ) / denominator ) 
    f_2 = np.sqrt( ( secondRoot**4 ) / denominator ) 
    print("f_1 :\t", f_1)
    print("f_2 :\t", f_2)

    
main()