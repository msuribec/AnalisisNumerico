import numpy as np
from math import sqrt
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


def chol(A,Scrolledtext1):

    n = len(A)

    # Create zero matrix for L
    L = np.eye(n)
    U = np.eye(n)
    i=0
    for i in range(n-1):
        Scrolledtext1.insert(tk.INSERT,'\nPHASE %d\n'%(i+1))
        sum1 = 0
        for k in range(i):
            sum1 = sum1 + L[i][k] * U[k][i]

        L[i][i]=np.sqrt(A[i][i]-sum1)
        U[i][i] = L[i][i]
        for j in range(i+1,n):
            sum2=0
            for k in range(0,i):
                sum2 = sum2 + L[j][k]* U[k][i]


            L[j][i] = (A[j][i] - sum2)/ U[i][i]

        for j in range(i+1,n):
            sum3=0
            for k in range(0,i):

                sum3 += sum3 + L[i][k]*U[k][j]

            U[i][j] = (A[i][j] - sum3) / L[i][i]
        Scrolledtext1.insert(tk.INSERT,'\nThe L matrix at this iteration is\n')
        Scrolledtext1.insert(tk.INSERT,L)
        Scrolledtext1.insert(tk.INSERT,'\nThe U matrix at this iteration is\n')
        Scrolledtext1.insert(tk.INSERT, U)
    Scrolledtext1.insert(tk.INSERT,'\nPHASE %d:\n' % (i + 2))

    productS = 0
    for k  in range(0,n - 1):
        productS = productS + L[n - 1][k]* U[k][n - 1]

    L[n - 1][n - 1] = np.sqrt(A[n - 1][n - 1] - productS)
    U[n - 1][n - 1] = L[n - 1][n - 1]

    Scrolledtext1.insert(tk.INSERT,'\nThe L matrix at this iteration is:\n')
    Scrolledtext1.insert(tk.INSERT, L)
    Scrolledtext1.insert(tk.INSERT,'\nThe U matrix at this iteration is\n')
    Scrolledtext1.insert(tk.INSERT, U)

    return L,U


def computing_final_solution(L,U,b,Scrolledtext1):

    y = auxiliary.forward_substitution(L, b)
    x = auxiliary.backward_substitution(U, y)
    Scrolledtext1.insert(tk.INSERT,'\nsolving Lz=b by forward substitution, we get\n')
    Scrolledtext1.insert(tk.INSERT,"\ny = " + str(y) + "\n")
    Scrolledtext1.insert(tk.INSERT,'\nSolving Ux=z by backward substitution, we get\n')
    Scrolledtext1.insert(tk.INSERT,"x = " + str(x) + "\n")
    return x

def solveChol(mat,coef,Scrolledtext1):
    A=np.array(mat,dtype=float)
    b=np.array(coef,dtype=float)
    L, U = chol(A,Scrolledtext1)
    computing_final_solution(L, U, b,Scrolledtext1)



# if __name__ == "__main__":
#     A = [[20, -1, 3,4], [6, 23, 4,3], [7,21, 46, 9],[-3,-9,12,38]]
#     b = [1, 1, 1,1]
#     solveChol(np.array(A),np.array(b))