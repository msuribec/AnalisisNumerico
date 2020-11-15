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


def crout(A,Scrolledtext1):
    n=len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for k in range(0, n):
        Scrolledtext1.insert(tk.INSERT, '\nPHASE %d \n' % (k + 1))
        U[k, k] = 1
        for j in range(k, n):
            sum0 = sum([L[j, s] * U[s, k] for s in range(0, j)])
            L[j, k] = A[j, k] - sum0
        for j in range(k+1, n):
            sum1 = sum([L[k, s] * U[s, j] for s in range(0, k)])
            U[k, j] = (A[k, j] - sum1) / L[k, k]
        Scrolledtext1.insert(tk.INSERT,'\nThe L matrix is\n')
        Scrolledtext1.insert(tk.INSERT,L)
        Scrolledtext1.insert(tk.INSERT,'\nThe U matrix is\n')
        Scrolledtext1.insert(tk.INSERT,U)

    return L, U

def computing_final_solution(L,U,b,Scrolledtext1):

    y = auxiliary.forward_substitution(L, b)
    x = auxiliary.backward_substitution(U, y)
    Scrolledtext1.insert(tk.INSERT,'\nsolving Lz=b by forward substitution, we get\n')
    Scrolledtext1.insert(tk.INSERT,"y = " + str(y) + "\n")
    Scrolledtext1.insert(tk.INSERT,'\nSolving Ux=z by backward substitution, we get\n')
    Scrolledtext1.insert(tk.INSERT,"x = " + str(x) + "\n")
    # Returning the solution vector x
    return x

def solveCrout(mat,coef,Scrolledtext1):
    A=np.array(mat,dtype=float)
    b=np.array(coef,dtype=float)
    L, U = crout(A,Scrolledtext1)
    computing_final_solution(L, U, b,Scrolledtext1)



# if __name__ == "__main__":
#     A = [[6, 6, 6], [4, 25, 6], [6, 9, 1]]
#     b = [1, 1, 1]
#     solveCrout(A,b)