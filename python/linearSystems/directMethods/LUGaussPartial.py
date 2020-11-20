"""
    LU factorization with partial pivoting

    In order to minimize space, the original coefficient matrix A is used to store the
    multipliers and (elements of L ) and the elements of U

    At the end of the method the
    U= upper(A)
    and L =lower(A)

    marks is the array that stores row changes
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
    

def luFactorPartial(A,Scrolledtext1):

    n = A.shape[0]
    Scrolledtext1.insert(tk.INSERT,'\nOriginal Matrix: \n')
    Scrolledtext1.insert(tk.INSERT,A)
    marks = np.arange(0,n)
    for k in range(n-1):
        Scrolledtext1.insert(tk.INSERT,'\nPHASE: %d\n' % k)
        # pivoting
        maxrow = np.argmax(abs(A[k:n,k])) + k
        marks[[k,maxrow]] = marks[[maxrow,k]]
        A[[k,maxrow]] = A[[maxrow,k]]
        Scrolledtext1.insert(tk.INSERT, 'The matrix after pivoting:\n')
        Scrolledtext1.insert(tk.INSERT, A)
        # LU
        for i in range(k+1,n):
            A[i,k] = A[i,k]/A[k,k]
            Scrolledtext1.insert(tk.INSERT,'\n L(%d , %d) = %f \n' % (i, k, A[i, k]))
            for j in range(k+1,n):
                A[i,j] -= A[i,k]*A[k,j]
                Scrolledtext1.insert(tk.INSERT,'U(%d,%d) = %f \n' % (i, j, A[i, j]))

    Scrolledtext1.insert(tk.INSERT, '\nThe final matrix L is \n:')
    Scrolledtext1.insert(tk.INSERT, np.tril(A))
    Scrolledtext1.insert(tk.INSERT, '\nThe final matrix U is \n:')
    Scrolledtext1.insert(tk.INSERT, np.triu(A))

    return [A,marks]




def solveLUGaussPartial(mat,coef,Scrolledtext1):
    aux = auxiliary.from_vector(coef)
    b=np.array(aux,dtype=float)
    A=np.array(mat,dtype=float)
    LU, piv = luFactorPartial(A,Scrolledtext1)
    b = b[piv]
    y = auxiliary.ufsub(LU, b)

    x = auxiliary.bsub(LU, y)
    Scrolledtext1.insert(tk.INSERT, '\nThe solution vector is\n:')
    Scrolledtext1.insert(tk.INSERT, np.array(x))




# if __name__ == '__main__':
#     coef = [-12, 13, 31, -32]
#     mat = [[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 13], [-12, 13, -8, -4]]
#     solveLUGaussPartial(mat,coef)
#
