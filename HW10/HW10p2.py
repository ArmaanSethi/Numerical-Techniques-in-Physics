#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def sawTooth(x):
    return 1-abs(x)

def a(k):
    if k == 0:
        return 1
    return ( 2 - 2*np.cos(np.pi*k) ) / ( np.pi**2 * k**2 )

x = np.arange(-1, 1, 1/60)
y = sawTooth(x)

z  = np.fft.fft(y, 120)

print("k\t A_k \t\t\t fft \t\t\t Ratio")
for i in range(30):
    print(i,"\t", 
          str.format('{0:.15f}',float(a(i))), "\t", 
          str.format('{0:.15f}', float(np.real(z[i]))), "\t", 
          np.real(z[i]) / a(i))
    
print('\nYou can see the error accumulating\n\n')
for i in range(100,120):
    print(i,"\t", 
          str.format('{0:.15f}',float(a(i))), "\t", 
          str.format('{0:.15f}', float(np.real(z[i]))), "\t", 
          np.real(z[i]) / a(i))

print('\n\n')