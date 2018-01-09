import numpy as np
import matplotlib.pyplot as plt


csv_input = np.loadtxt('HW10bridge.csv', delimiter = ',')
print(csv_input)
N = len(csv_input)
dt = 0.01 #seconds
t = N*dt
x = np.arange(0,t,dt)
z = np.fft.fft(csv_input)
freqs = np.fft.fftfreq(len(z))
plt.figure()
plt.xlabel("time(s)")
plt.plot(x, abs(z))

Nyquist = 50
DC = 0

"""ZOOM IN"""
for i in range(10):
    plt.figure()
    plt.xlabel("time(s)")
    plt.plot(x[i*N//10:(i+1)*N//10], abs(z[i*N//10:(i+1)*N//10]))
    plt.grid(True, linestyle='--')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')    




plt.figure()
plt.plot(abs(freqs))
plt.title("|Frequencies|")
plt.grid(True, linestyle='--')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')    
plt.xlabel("time intervals occured(0.01s)")
plt.ylabel("frequency")