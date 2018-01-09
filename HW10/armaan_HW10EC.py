"""
Armaan Sethi
Physics 331
HW10 Extra Credit
"""
import numpy as np
import matplotlib.pyplot as plt

"""From Textbook"""
def printSoln(X, Y, freq):
    def printHead(n):
        print("\nx        ", end=" ")
        for i in range(n):
            print ("      y[",i,"] ",end=" ")
        print()
        
    def printLine(x, y, n):
        print("{:13.4e}".format(x),end=" ")
        for i in range(n):
            print("{:13.4e}".format(y[i]),end=" ")   
        print()
    m = len(Y)
    try: n = len(Y[0])
    except TypeError: n = 1
    if freq == 0: freq = m
    printHead(n)
    for i in range(0, m, freq):
        printLine(X[i], Y[i], n)
    if i != m-1: printLine(X[m - 1], Y[m - 1], n)

def integrate(F, x, y, xStop, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while(x < xStop):
        h = min(h, xStop - x)
        y = y + h*F(x, y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

def RK4integrate(F, x, y, xStop, h):
    def run_kut4(F, x, y, h):
        K0 = h*F(x, y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h, xStop - x)
        y = y + run_kut4(F, x, y, h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

"""Start Code"""
def ImplicitEulerIntegrate(F, x, y, xStop, h, C):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    print("\n\nh")
    print(h)
    print('\nC\n')
    print(C)
    print('Ch\n')
    print(C*h)
    print('1+Ch')
    print((np.identity(2) +C*h))
    print('(1+Ch)^-1')
    dotter = np.linalg.inv((np.identity(2) +C*h))
    print(dotter)
    while(x < xStop):
        h = min(h, xStop - x)
        y = np.dot( dotter , y )
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

def Fcoupled(x, y):
    F = np.zeros( (2,), dtype=float ) 
    F[0] = 998*y[0] + 1998*y[1]
    F[1] = -999*y[0] - 1999*y[1]
    return F


def u(x):
    return 2*np.e**(-x)- np.e**((-1000)*x)
def v(x):
    return -1*np.e**((-1)*x) + np.e**((-1000)*x)


def plot(x, y):
#    plt.figure()
    plt.plot(x, y[:,0])
    plt.ylim(0,2)
    
def main():
    """Values"""
    x0 = 0.0 
    xStop = 4.0 
    y0 = np.asarray( [ 1., 0. ], dtype=float ) 
    #    h = [0.001, 0.002, 0.01, 0.1, 0.0019, 0.00199, 0.01999] 
    h = [0.001, 0.002, 0.01, 0.1, 0.0019, 0.00199]
    #h = [0.001]
    C = np.array([[-998., -1998.],[999., 1999.]])
    freq = 20
    """Set figure to large so I can easily compare different h values"""
    
    """Euler"""
    for _h in h:
        plt.figure(figsize = (15,15))
        X1, Y1 = integrate(Fcoupled, x0, y0, xStop, _h)
        plt.title("Euler Integration vs Analytical. h="+ str(_h) )
    #        printSoln(X1,Y1,freq)
        plt.scatter(X1, u(X1), s=4)
        plt.scatter(X1, v(X1), s=4)
        plt.scatter(X1, Y1[:,0], s=1)    
        plt.scatter(X1, Y1[:,1], s=1)    
        plt.grid(True, linestyle='--')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(("Analytical u", "Analytival v", "Euler u", "Euler v"))
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')    
        
    """Implicit Euler"""
    for _h in h:
        plt.figure(figsize = (15,15))
        X1, Y1 = ImplicitEulerIntegrate(Fcoupled, x0, y0, xStop, _h, C)
        plt.title("Implicit Euler Integration vs Analytical. h="+ str(_h) )
    #        printSoln(X1,Y1,freq)
        plt.scatter(X1, u(X1), s=4)
        plt.scatter(X1, v(X1), s=4)
        plt.scatter(X1, Y1[:,0], s=1)    
        plt.scatter(X1, Y1[:,1], s=1)    
        plt.grid(True, linestyle='--')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(("Analytical u", "Analytival v", "ImplicitEuler u", "ImplicitEuler v"))
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')    
    plt.show()

"""Explanation of findings"""
"""
Both the Euler and Implicit Euler are very accurate at h= 0.001, however, 
when you increase h above 0.001 the Euler integration begins to diverge.
This is because euler integration diverges when h > 2/c.  This is why in the Euler integration
when h = 0.002 graph, it almost seems as if there are 2 graphs of the Euler solution, when 
in reality it is just very instable and bouncing around the analytical solution at every 
other step. When h > 0.01, the Euler integration diverges to infinity (So the graphs do not work).
The Implicit Euler integration converges for all h values, so we do not have that problem.
One downside of Implicit Euler integration is that it is more computationally expensive 
since it requires a matrix inversion. It is also a slightly more complex algorithm. 
"""
main()

