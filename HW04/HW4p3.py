# Homework 4, Problem 3
# Armaan Sethi

import numpy as np
import matplotlib.pyplot as plt

## module LUdecomp3
''' c,d,e = LUdecomp3(c,d,e).
    LU decomposition of tridiagonal matrix [a], where {c}, {d}
    and {e} are the diagonals of [a]. On output
    {c},{d} and {e} are the diagonals of the decomposed matrix.

    x = LUsolve3(c,d,e,b).
    Solution of [a]{x} {b}, where {c}, {d} and {e} are the
    vectors returned from LUdecomp3.
'''

def LUdecomp3(c,d,e):
    n = len(d)
    for k in range(1,n):
        lam = c[k-1]/d[k-1]
        d[k] = d[k] - lam*e[k-1]
        c[k-1] = lam
    return c,d,e

def LUsolve3(c,d,e,b):
    n = len(d)
    for k in range(1,n):
        b[k] = b[k] - c[k-1]*b[k-1]
    b[n-1] = b[n-1]/d[n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - e[k]*b[k+1])/d[k]
    return b   

## module cubicSpline
''' k = curvatures(xData,yData).
    Returns the curvatures of cubic spline at its knots.

    y = evalSpline(xData,yData,k,x).
    Evaluates cubic spline at x. The curvatures k can be
    computed with the function 'curvatures'.
'''   
def curvatures(xData,yData):
    n = len(xData) - 1
    c = np.zeros(n)
    d = np.ones(n+1)
    e = np.zeros(n)
    k = np.zeros(n+1)
    c[0:n-1] = xData[0:n-1] - xData[1:n]
    d[1:n] = 2.0*(xData[0:n-1] - xData[2:n+1])
    e[1:n] = xData[1:n] - xData[2:n+1]
    k[1:n] =6.0*(yData[0:n-1] - yData[1:n]) \
                 /(xData[0:n-1] - xData[1:n]) \
             -6.0*(yData[1:n] - yData[2:n+1])   \
                 /(xData[1:n] - xData[2:n+1])
    LUdecomp3(c,d,e)
    LUsolve3(c,d,e,k)
    return k

def evalSpline(xData,yData,k,x):
    
    def findSegment(xData,x):
        iLeft = 0
        iRight = len(xData)- 1
        while 1:
            if (iRight-iLeft) <= 1: return iLeft
            i =int((iLeft + iRight)/2)
            if x < xData[i]: iRight = i
            else: iLeft = i
    
    i = findSegment(xData,x)
    h = xData[i] - xData[i+1]
    y = ((x - xData[i+1])**3/h - (x - xData[i+1])*h)*k[i]/6.0 \
      - ((x - xData[i])**3/h - (x - xData[i])*h)*k[i+1]/6.0   \
      + (yData[i]*(x - xData[i+1])                            \
       - yData[i+1]*(x - xData[i]))/h
    return y

## EDIT BELOW HERE
    
def f(x):
    return abs(np.sin(x))

def main():
    #Initial "Data" range
    x = np.arange(-10,10,0.1)
    #Initial "Data" points
    y = f(x)    
    #Plot Initial Data (-10,10)
    plt.figure(figsize=(8,8))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Part B')
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.scatter(x,f(x))
    
    #Calculate Spline
    k = curvatures(x, y)
    v = np.arange(-10,10,0.002)
    y_spline = []
    for i in v:
        y_spline.append(evalSpline(x,y,k,i))
    
    #Plot Initial Data, Spline, Correct Values (-0.5,0.5)
    plt.figure(figsize=(10,10))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Part C')
    plt.grid(True, linestyle='--')
    plt.xlim(-0.5,0.5)
#    plt.ylim(-0.1,0.5)
    plt.scatter(x,f(x), color = 'm')
    plt.scatter(v, y_spline, color = 'c',s=3)
    plt.scatter(v,f(v), color = 'y', s=2)
    plt.legend(('Part B "Data"' , 'Interpolation' , 'Correct Values'), loc='best')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

main()