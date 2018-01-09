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

def Fcoupled(x, y):
    F = np.zeros( (2,), dtype=float ) 
    F[0] = y[1]
    F[1] = -(2*x + 3)*y[1]-6*x*y[0] + x
    return F

def FcoupledAnalytical(x, y):
    F = np.zeros( (2,), dtype=float ) 
    F[0] = y[1]
    F[1] = -(2*x + 3)*y[1]-6*x*y[0] + x
    return F

def anayltical(x):
    return (3.5)*np.e**(-x**2) + (0.5)

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
    y0 = np.asarray( [ 1., 1. ], dtype=float ) 
    h = [1.0, 0.1, 0.01, 0.001] 
    freq = 100 
    """Set figure to large so I can easily compare different h values"""
    plt.figure(figsize = (10,10))
    
    """Euler"""
    for _h in h:
        X1, Y1 = integrate(Fcoupled, x0, y0, xStop, _h)
        printSoln(X1,Y1,freq)
        plot(X1, Y1)
        
        
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')    
    plt.title("Euler Integration of y''(x)+(2x+3)y'(x)+6xy = x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(("h=1", "h=0.1", "h=0.01", "h = 0.001"))
    plt.show()
    
    """Runge Kuta"""
    plt.figure(figsize=(10,10))
    X1, Y1 = RK4integrate(FcoupledAnalytical, x0, y0, xStop, 0.001)
    
    analytical_x = np.linspace(0,4)
    plt.plot(analytical_x, anayltical(analytical_x))
    plot(X1, Y1)
    
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')    
    plt.title("Runge Kuta of y''(x)+(2x+3)y'(x)+6xy = x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(("Analytical Solution", "Runge Kuta"))
    plt.show()

    plt.show()
    
main()

