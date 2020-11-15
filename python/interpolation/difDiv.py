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

from numpy import *



def divDiffNewton(x, y):
    n = len(x)
    A = zeros((n, n + 1))
    A[:, 0] = x[:]
    A[:, 1] = y[:]
    # Fill in Divided differences
    for j in range(2, n + 1):
        for i in range(j - 1, n):
            A[i, j] = (A[i, j - 1] - A[i - 1, j - 1]) / (A[i, 0] - A[i - j + 1, 0])
    # Copy diagonal elements into array for returning
    p = zeros(n)
    for k in range(0, n):
        p[k] = A[k, k + 1]
    return A,p

def interpolate_newton(x,y):
    xpt = array(x)
    ypt = array(y)
    A, p = divDiffNewton(xpt, ypt)
    set_printoptions(suppress=True)
    str=array_str(A,precision=5)
    return str

def interpolate_newtonGUI(x,y,Scrolledtext1):
    xpt = array(x)
    ypt = array(y)
    A, p = divDiffNewton(xpt, ypt)
    set_printoptions(suppress=True)
    Scrolledtext1.insert(tk.INSERT, 'The divided differences table is:\n')
    str=array_str(A,precision=5)
    Scrolledtext1.insert(tk.INSERT, str)





# if __name__ == "__main__":
#     x = [1, 1.2, 1.4, 1.6, 1.8, 2]
#     y = [0.6747, 0.8491, 1.1214, 1.4921, 1.9607, 2.5258]
#     str=interpolate_newton(x,y)
#     print(str)
