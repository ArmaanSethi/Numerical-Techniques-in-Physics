# PHYS 331
# Armaan Sethi
import numpy as np
def calculateSum_16bit(delta):
    sum = np.float16(0.0)
    delta = np.float16(delta)  # Convert delta to a 16-bit floating point number.

    if delta == np.float16(0.0):  # If the 16-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 16 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

def calculateSum_32bit(delta):
    sum = np.float32(0.0)
    delta = np.float32(delta)  # Convert delta to a 32-bit floating point number.

    if delta == np.float32(0.0):  # If the 32-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 32 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

def calculateSum_64bit(delta):
    sum = np.float64(0.0)
    delta = np.float64(delta)  # Convert delta to a 64-bit floating point number.

    if delta == np.float64(0.0):  # If the 64-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 64 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

for i in range(8,500):
    print("I: ", i)
    print("16bit: ", calculateSum_16bit(10**-i))
    print("32bit: ", calculateSum_32bit(10**-i))
    print("64bit: ", calculateSum_64bit(10**-i))
    