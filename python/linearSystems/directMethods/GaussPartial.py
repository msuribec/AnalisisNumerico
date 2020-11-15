
import linearSystems.directMethods.auxiliary as auxiliary
import copy
import numpy as np

from fractions import Fraction


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


def gauss(A,b,Scrolledtext1):
    np.set_printoptions(suppress=True)
    A = copy.deepcopy(A)
    b = copy.deepcopy(b)
    n = len(A)
    p = len(b[0])
    det = 1
    Ab= auxiliary.augmentedForm(A, b)
    Scrolledtext1.insert(tk.INSERT,'The augmented matrix is: \n')
    Scrolledtext1.insert(tk.INSERT,np.array(Ab))
    Scrolledtext1.insert(tk.INSERT,'\n')
    for k in range(n - 1):
        Scrolledtext1.insert(tk.INSERT,'PHASE %d' %(k+1))
        r = k
        # pivoting
        for j in range(k + 1, n):
            if abs(A[j][k]) > abs(A[r][k]):
                r = j
        if r != k:
            A[k], A[r] = A[r], A[k] #swaping rows
            b[k], b[r] = b[r], b[k] #swaping rows
            det = -det
        Scrolledtext1.insert(tk.INSERT,'The multipliers for this phase are\n')
        for j in range(k + 1, n): # multipliers
            t = A[j][k] / A[k][k]
            Scrolledtext1.insert(tk.INSERT,"m(% d, % d)\n" %(k, j))
            for r in range(k + 1, n):
                A[j][r] -= t * A[k][r]
            for r in range(p):
                b[j][r] -= t * b[k][r]
        np.set_printoptions()
        Scrolledtext1.insert(tk.INSERT,'The matrix at this phase is:\n')
        Scrolledtext1.insert(tk.INSERT,np.triu(np.array(A)))
        Scrolledtext1.insert(tk.INSERT,'\n')


    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = A[i][j]
            for k in range(p):
                b[i][k] -= t * b[j][k]
        t = 1 / A[i][i]
        det *= A[i][i]
        for j in range(p):
            b[i][j] *= t
    Scrolledtext1.insert(tk.INSERT,'The final solution (in orde from x1 to xn) is:\n')
    Scrolledtext1.insert(tk.INSERT,np.array(b))
    return det, b


def zeromat(p, q):
    return [[0] * q for i in range(p)]

def mapmat(f, a):
    return [list(map(f, v)) for v in a]

def ratmat(a):
    return mapmat(Fraction, a)

def solveGaussPartial(A,coef,Scrolledtext1):
    b=auxiliary.from_vector(coef)
    det, c = gauss(A, b,Scrolledtext1)

# if __name__ == '__main__':
#     A = [[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 5], [-12, 13, -8, -4]]
#     b = [-12, 13, 31, -32]
#     solveGaussPartial(A,b)
#
