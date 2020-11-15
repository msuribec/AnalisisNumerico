import numpy as np
from linearSystems.directMethods import auxiliary

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

def doolittle(A,Scrolledtext1):
    # Creating two L and U matrices filled with 0s and the same size as A

    L = np.zeros_like(A).astype(float)
    U = np.zeros_like(A).astype(float)
    n = len(A)

    # for-loop in order to set the j,j-th entry of U to 1

    for k in range(n):
        Scrolledtext1.insert(tk.INSERT,'\nPHASE %d\n' % (k + 1))
        L[k, k] = 1

        U[k, k] = (A[k, k] - np.dot(L[k, :k], U[:k, k]))

        for i in range(k + 1, n):
            U[k, i] = (A[k, i] - np.dot(L[k, :k], U[:k, i]))

        for j in range(k + 1, n):
            L[j, k] = (A[j, k] - np.dot(L[j, :k], U[:k, k])) / U[k, k]
        Scrolledtext1.insert(tk.INSERT,'\nThe L matrix is\n')
        Scrolledtext1.insert(tk.INSERT,L)
        Scrolledtext1.insert(tk.INSERT,'\nThe U matrix is\n')
        Scrolledtext1.insert(tk.INSERT,U)
    # Returning the matrices L and U i.e. the A matrix decomposed using Doolittle's algorithm

    return (L, U)


def computing_final_solution(L,U,b,Scrolledtext1):
    y = auxiliary.forward_substitution(L, b)
    x = auxiliary.backward_substitution(U, y)
    Scrolledtext1.insert(tk.INSERT,'\nsolving Lz=b by forward substitution, we get\n')
    Scrolledtext1.insert(tk.INSERT,"y = " + str(y) + "\n")
    Scrolledtext1.insert(tk.INSERT,'\nSolving Ux=z by backward substitution, we get\n')
    Scrolledtext1.insert(tk.INSERT,"x = " + str(x) + "\n")
    return x

def solveDoolittle(mat,coef,Scrolledtext1):
    A=np.array(mat,dtype=float)
    b=np.array(coef,dtype=float)
    L, U = doolittle(A,Scrolledtext1)
    computing_final_solution(L,U,b,Scrolledtext1)

# if __name__ == "__main__":
#     A = [[4, -1, 0,3], [1, 15.5, 3,8], [0, -1.3,-4 ,1.1], [14, 5,-2 ,30]]
#     b = [1, 1, 1, 1]
#     solveDoolittle(A,b)
