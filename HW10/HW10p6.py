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
        Y.append(Y)
        
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
def Fcoupled(x,y): 
    F = np.zeros( (2,), dtype=float ) 
    F[0] = y[1]
    F[1] = -g/L*np.sin(y[0])
    return F


#Global Variables
L = 1 #m
g = 9.8 #m/s**2

def main():
    x0 = 0.0 
    xStop = 10.0 
    y0 = np.asarray( [ 1., 0. ], dtype=float ) 
    h = 0.05 
    freq = 5 
    
    X,Y = RK4integrate(Fcoupled,x0,y0,xStop,h) 
    printSoln(X,Y,freq)
    
    plt.figure()
    plt.plot(X, Y[:,0])
    plt.xlabel('time (t)')
    plt.ylabel('theta(rads)')
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')    
    
    plt.show() 
    
main()


