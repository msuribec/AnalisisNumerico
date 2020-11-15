"""
Implementation of the Gaussian Elimination Algorithm for finding the row-reduced echelon form of a given matrix.
No pivoting is done.
Requires Python 3 due to the different behaviour of the division operation in earlier versions of Python.
Released under the Public Domain (if you want it - you probably don't)
"""

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


import numpy as np
import linearSystems.directMethods.auxiliary as auxiliary


def gaussElim(mat,Scrolledtext1):
    """
	Changes mat into Reduced Row-Echelon Form.
	"""
    # at the end of this for loop, the matrix is in Row-Echelon format.
    Scrolledtext1.insert(tk.INSERT,'The augmented matrix is:\n')
    np.set_printoptions(suppress=True)
    Scrolledtext1.insert(tk.INSERT,np.array(mat))
    for k in range(min(len(mat), len(mat[0]))):
        # every iteration, ignore one more row and column
        for row in range(k, len(mat)):
            zero_row = mat[row][k] == 0
            if zero_row:
                continue
            # swap current row with first row
            mat[k], mat[row] = mat[row], mat[k]

            if row != len(mat) - 1:  # printing phase number
                Scrolledtext1.insert(tk.INSERT,"\nPhase: %d \n" % (k + 1))
                Scrolledtext1.insert(tk.INSERT,'\nThe multipliers for this phase are:\n')
            Abkk = mat[k][k]
            for i in range(k + 1, len(mat)):
                Abik = mat[i][k]
                M = Abik / Abkk
                Scrolledtext1.insert(tk.INSERT,'M(%g %g): %g\n' % (i + 1, k + 1, M))
                for j in range(k, len(mat[0])):
                    mat[i][j] += mat[k][j] * (-1*M)
                    
            Scrolledtext1.insert(tk.INSERT,'\nThe matrix at this phase is:\n')
            Scrolledtext1.insert(tk.INSERT,np.array(mat))
            break

    Scrolledtext1.insert(tk.INSERT,'\nThe Final Upper triangular matrix is:\n')
    Scrolledtext1.insert(tk.INSERT,np.array(mat, dtype=float))
    Ab = np.array(mat, dtype=float)
    x = auxiliary.back(Ab, len(mat))
    Scrolledtext1.insert(tk.INSERT,'\nThe final solution (in order, from x1 to xn) is:\n')
    Scrolledtext1.insert(tk.INSERT,x)
    return mat, x


def solveGaussSimple(mat, coef,Scrolledtext1):
    b = auxiliary.from_vector(coef)
    Ab = auxiliary.augmentedForm(mat, b)
    mat, x = gaussElim(Ab,Scrolledtext1)
    return x



