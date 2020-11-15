"""
    LU factorization without pivoting

    In order to minimize space, the original coefficient matrix A is used to store the
    multipliers and (elements of L ) and the elements of U

    At the end of the method the
    U= upper(A)
    and L =lower(A)
"""
import numpy as np
import linearSystems.directMethods.auxiliary as auxiliary

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True
    


def luFactor(A,b,Scrolledtext1):

    n = A.shape[0]
    Scrolledtext1.insert(tk.INSERT,'\nOriginal Matrix: \n')
    Scrolledtext1.insert(tk.INSERT,A)
    for k in range(n-1):
        Scrolledtext1.insert(tk.INSERT,'\nPHASE: %d\n' %k)
        Scrolledtext1.insert(tk.INSERT,"\nAt this phase : \n")
        for i in range(k+1,n):
            A[i,k] = A[i,k]/A[k,k]      # " L[i,k] = A[i,k]/A[k,k] "
            Scrolledtext1.insert(tk.INSERT,'\nL(%d,%d) = %f \n'%(i,k,  A[i,k]))

            for j in range(k+1,n):
                A[i,j] -= A[i,k]*A[k,j] # " U[i,j] -= L[i,k]*A[k,j] "
                Scrolledtext1.insert(tk.INSERT,'\nU(%d,%d) = %f \n' % (i,j, A[i, j]))

    Scrolledtext1.insert(tk.INSERT,'\nThe final L matrix is\n:')
    Scrolledtext1.insert(tk.INSERT,np.tril(A))
    Scrolledtext1.insert(tk.INSERT,'\nThe final U matrix is\n:')
    Scrolledtext1.insert(tk.INSERT,np.triu(A))
    LU = A
    z = auxiliary.forwarsRows(LU, b)
    x = auxiliary.backwardsRows(LU, z)
    return x # (if you want)





def solveLUSimple(mat,coef,Scrolledtext1):
    aux=auxiliary.from_vector(coef)
    b=np.array(aux,dtype=float)
    A=np.array(mat,dtype=float)
    x = luFactor(A, b,Scrolledtext1)
    Scrolledtext1.insert(tk.INSERT,x)

# if __name__ == '__main__':
#     coef = [-12, 13, 31, -32]
#     mat = [[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 13], [-12, 13, -8, -4]]
#     # mat = [-7, 2, -3, 4, 5, -1, 14, -1, 1, 9, -7, 5, -12, 13, -8, -4]
#
#     solveLUSimple(mat,coef)

