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

def GaussTotal(A, b,Scrolledtext1):
    copyA = A.astype(np.float32)
    copyb = b.astype(np.float32)
    Ab = np.concatenate((copyA, copyb), axis=1)
    n = A.shape[0]
    M = np.zeros_like(A)
    subm= np.zeros_like(A)
    Scrolledtext1.insert(tk.INSERT,'\nAugmented matrix is: \n')
    Scrolledtext1.insert(tk.INSERT, Ab)
    marks=np.arange(start=0, stop=n, step=1)
    for k in range(n - 1):
        Scrolledtext1.insert(tk.INSERT,'\nPhase: %g\n' % (k+1))
        # find maximum of absolute value of matrix
        a_abs = np.absolute(Ab[:, 0:n])
        subm = a_abs[k:n, k:n]
        Scrolledtext1.insert(tk.INSERT,"\nsubmatrix is:\n")
        Scrolledtext1.insert(tk.INSERT, Ab)
        max_abs = subm.max()

        i=k
        j=k

        for ind1 in range(len(subm)):
            for ind2 in range(len(subm)):
                if subm[ind2,ind1]==max_abs:
                    i=ind2
                    j=ind1
                    break
        i=i+k
        j=j+k
        if max_abs == 0:
            Scrolledtext1.insert(tk.INSERT,'\nSystem has no unique solution\n')

        Ab = auxiliary.swapCols(Ab, k, j)
        Ab = auxiliary.swapRows(Ab, k, i)
        b = auxiliary.swapRows(b, k, j)
        marks= auxiliary.swapRows(marks,k,j)
        Scrolledtext1.insert(tk.INSERT,'\nAfter row and column swap\n')
        Scrolledtext1.insert(tk.INSERT, Ab)

        Scrolledtext1.insert(tk.INSERT,'\nThe multipliers for this phase are\n')
        for r in range(k + 1, n, 1):
             M[r, k] = Ab[r, k] / Ab[k, k]
             Scrolledtext1.insert(tk.INSERT,'\nM(%d,%d) = %f \n' % (r, k, M[r, k]))
             Ab[r, k:n + 1] = Ab[r, k:n + 1] - M[r, k] * Ab[k, k:n + 1]
        Scrolledtext1.insert(tk.INSERT,'\nAfter the operations\n')
        Scrolledtext1.insert(tk.INSERT, Ab)


    Scrolledtext1.insert(tk.INSERT,'\nSolution is (in order from x1 to xn):\n')
    x= auxiliary.back(Ab,n)
    for i in range(0,n):
        for j in range(0,n):
            if marks[j]==i :
                k=j
        aux=x[k]
        x[k]=x[i]
        x[i]=aux
        aux = marks[k]
        marks[k] = marks[i]
        marks[i] = aux

    Scrolledtext1.insert(tk.INSERT,x)
    return A

def solveGaussT(mat,coef,Scrolledtext1):
    A, b = auxiliary.formatVector(mat, coef)
    GaussTotal(A,b,Scrolledtext1)


if __name__ == '__main__':
    mat = [[-1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0], [0, 0, 0, 0, 4, 1], [1, 1, -1, -1, 0, 0], [0, 0, 2, 1, -2, -1]]
    coef = [7,-1,-8,2,0,0]
    solveGaussT(mat,coef)

