# Armaan Sethi

#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ain" and an nx1 column matrix "bin"
# it performs Gauss elimination and outputs the eliminated new matrices
# "A" is also nxn upper triangular, and "b" as an nx1 column matrix
def GaussElimin(Ain,bin):
    n=len(bin)
    A = Ain.copy() # make copies so as not to write over originals
    b = bin.copy()
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):

            c = A[j,i]/A[i,i] # multiplicative factor to zero point
            A[j,i] = 0.0 # we know this element goes to zero
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n] # do subtraction of two rows
            b[j] = b[j]-c*b[i] # do substraction of b's as well
    return (A,b)  # return modified A and b

#---Do not modify above this line--#
    
def triSolve(M, b, upperOrLower):
    n = M.shape[0]
    s = np.zeros([n], dtype=float)

    if(upperOrLower):
        #Upper
        for i in range(n):
            subtract = 0
            for j in range(i):
                subtract += s[n-j-1] * M[n-i-1][n-j-1]            
            s[n-1-i] = (b[n-1-i] - subtract)/M[n-1-i][n-1-i]
    else:
        #Lower
        for i in range(n):
            subtract = 0
            for j in range(0, i):
                subtract += s[j] * M[i][j]
            s[i] = (b[i]-subtract)/M[i][i]
    return s

def main():
    a1 = np.array([[4.,-2.,1.],[-3.,-1.,4.],[1.,-1.,3.]])
    b1 = np.array([15., 8., 13.])
    
    a2 = np.array([[2.,2.,3.,2.],[0.,2.,0.,1.],[4.,-3.,0.,1.],[6.,1.,-6.,5.]])
    b2 = np.array([-2.,0.,-7.,6.])
    
    print('\na1\n', a1)
    print('b1\n', b1)
    print('\nSolution in order to compare\n', np.linalg.solve(a1,b1))#Solution in order to compare
    (a1, b1) = GaussElimin(a1,b1)
    print('solve', triSolve(a1,b1,1))
    
    
    print('\n\na2\n', a2)
    print('b2\n', b2)
    print('\nSolution in order to compare\n', np.linalg.solve(a2,b2))#Solution in order to compare
    (a2, b2) = GaussElimin(a2,b2)
    print('solve', triSolve(a2,b2,1))
    

main()