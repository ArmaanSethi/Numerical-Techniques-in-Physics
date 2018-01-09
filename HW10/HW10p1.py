import numpy as np
import matplotlib.pyplot as plt

def sawTooth(x):
    return 1-abs(x)

def a(k):
    if k == 0:
        return 1
    return ( 2 - 2*np.cos(np.pi*k) ) / ( np.pi**2 * k**2 )

def f(x, k):
    func = 0
    for i in range(1, len(k)):
        func+= k[i]*np.cos(i*x)
    return k[0]/2 + func
        
    
def funcSawtooth(kmax):
    kvalues = np.zeros(kmax)
    for i in range(kmax):
        kvalues[i] = a(i)
        
    x = np.linspace(-1,1,120)
    y = np.zeros((len(x), 1))
    
    for i in x:
        sums = []
        for k in range(1, kmax+1):
            term = a(k)*np.cos(k*np.pi*i)
            sums.append(term)
            
        place = np.where(x==i)
        y[place] = a(0)/2 + sum(sums)
            
    plt.figure()
    plt.title("funcsawtooth() Kmax = " + str(kmax))
    plt.plot(x, sawTooth(x))
    plt.plot(x, y)
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')    
    plt.legend(("Original Function", "Transformation"))
    return kvalues

def ModFuncSawtooth(kmax):
    kvalues = np.zeros(kmax)
    for i in range(kmax):
        kvalues[i] = a(i)
        
    x = np.linspace(-3,3,120)
    y = np.zeros((len(x), 1))
    
    for i in x:
        sums = []
        for k in range(1, kmax+1):
            term = a(k)*np.cos(k*np.pi*i)
            sums.append(term)
            
        place = np.where(x==i)
        y[place] = a(0)/2 + sum(sums)
            
    plt.figure()
    plt.title("ModFuncSawtooth() Kmax = " + str(kmax))
    plt.plot(x, y)
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')    
    plt.legend(("Transformation",))
    return kvalues

print("Ak Values Used: \n", funcSawtooth(1))
print("Ak Values Used: \n", funcSawtooth(2))
print("Ak Values Used: \n", funcSawtooth(3))
print("Ak Values Used: \n", funcSawtooth(30))

print("Ak Values Used: \n", ModFuncSawtooth(1))
print("Ak Values Used: \n", ModFuncSawtooth(3))
print("Ak Values Used: \n", ModFuncSawtooth(30))

