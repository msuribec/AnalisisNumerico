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

def interpolate_newtonGUI(x,y,Scrolledtext1):
    xpt = array(x)
    ypt = array(y)
    A, p = divDiffNewton(xpt, ypt)
    set_printoptions(suppress=True)
    Scrolledtext1.insert(tk.INSERT, 'The divided differences table is:\n')

    Scrolledtext1.insert(tk.INSERT,'\n'.join(['     '.join(['{:4}'.format(item) for item in row])
                     for row in A]))
    Scrolledtext1.insert(tk.INSERT, '\nThe polynomial is:\n')
    i=0
    grado = len(xpt)-1
    for line in A:
        if i==0:
            Scrolledtext1.insert(tk.INSERT, line[i + 1])
            Scrolledtext1.insert(tk.INSERT, ' + \n')
        elif i==grado:
            Scrolledtext1.insert(tk.INSERT, line[i + 1])

            for j in range(0, i):

                Scrolledtext1.insert(tk.INSERT, '   (x - %.15f) ' % xpt[j])
        else:
            Scrolledtext1.insert(tk.INSERT, line[i + 1])
            for j in range(0,i):
                Scrolledtext1.insert(tk.INSERT, '   (x - %.15f) '%xpt[j])
            Scrolledtext1.insert(tk.INSERT, '+ \n')
        i=i+1






# if __name__ == "__main__":
#     x = [1, 1.2, 1.4, 1.6, 1.8, 2]
#     y = [0.6747, 0.8491, 1.1214, 1.4921, 1.9607, 2.5258]
#     str=interpolate_newton(x,y)
#     print(str)
