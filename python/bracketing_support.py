#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 14, 2020 09:11:34 PM EST  platform: Windows NT

import sys
import oneVariableEquations.bisection as bisection
import oneVariableEquations.reglaFalsa as regfalsi
from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
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

def set_Tk_var():
    global combobox
    combobox = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None




if __name__ == '__main__':
    import bracketing
    bracketing.vp_start_gui()


def runMethod(choiceInteg, fEntry, valueaEntry, valuebEntry,iterationsEntry,tolEntry, Scrolledtext1):

    Scrolledtext1.delete("1.0", 'end')
    k = choiceInteg.get()
    str = fEntry.get()
    f = getSympyFun(str)
    a = float(valueaEntry.get())
    b = float(valuebEntry.get())
    tol = float(tolEntry.get())
    iter_max = int(iterationsEntry.get())
    ops= ['bisection','regula falsi']
    x=sp.Symbol('x')
    if k == ops[0]:
        bisection.bisection(x, f, a, b, tol, iter_max,Scrolledtext1)
    elif k==ops[1]:
        regfalsi.reglaFalsa(x, f, a, b, tol, iter_max,Scrolledtext1)
    else:
        Scrolledtext1.insert(tk.INSERT, "Please pick a method")



def getSympyFun(str):
    x = sp.Symbol('x')
    expr = parse_expr(str, evaluate=False)
    return expr

