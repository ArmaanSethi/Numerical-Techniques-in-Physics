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
    root = np.Infinity
    iters = 0
    # max_iters = np.log(abs(xhi-xlo)/xtol)/np.log(2.0)#check this
    
    if((np.sign(f(xlo))) == np.sign(f(xhi))):
        #print("Bisection cannot find the root")
        return(np.Infinity, np.Infinity)
    
    while((iters < nmax) and (root == np.Infinity)):
        midpoint = (xlo + xhi)/2.0
        if(np.sign(f(midpoint)) == np.sign(f(xlo))):
            xlo = midpoint
        else:
            xhi = midpoint
        if((abs(f(xlo)) - xtol) <= 0.0):
            root = xlo
        if((abs(f(xhi)) - xtol) <= 0.0):
            root = xhi
        iters+=1


    return (root, iters)

def bernoulli(h):
    Q = 1.2
    g = 9.81
    b = 1.8
    h0 = 0.6
    H = 0.075
    return ((Q*Q)/(2*g*b*b*h0*h0)) + h0 - ((Q*Q)/(2*g*b*b*h*h)) - h - H
    

def main(f):
# Example: Find the root of f2(x) and print the result.
    root = np.Infinity
    iters = 0
    answer_list = []
    x = np.arange(-10, 10, 0.1)

    tolerance = 1e-12
    
    for i in range(len(x)):
        (root,iters) = rf_bisect(bernoulli, x[i], x[i]+0.5, tolerance, 2500) 
        if(root != np.Infinity):
            if(len(answer_list)==0):
                answer_list.append((root, iters))
            elif((abs(root-answer_list[-1][0]) - tolerance*10) > 0):
                answer_list.append((root, iters))
                
    #plot
    h = np.arange(-1, 1, 0.01) 
    #add labels and legend
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("plot")
    #plot it
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    #function
    plt.ylim(-0.25,0.25)
    plt.plot(h, bernoulli(h))
    for i in range(len(answer_list)):
        if (answer_list[i][0] < 0):
            print ('root is not possible but...')
            #uncomment next line to not output physically impossible roots
            #continue
            
        print('Root of ' + f.__name__ + ":   " + str(answer_list[i][0]))
        print('# iterations: ' + str(answer_list[i][1]))
        print(f.__name__ + ' evaluated at root is: ' + str(f(answer_list[i][0])))
        print()

main(bernoulli)

    