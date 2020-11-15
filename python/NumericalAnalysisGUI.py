#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 15, 2020 10:06:36 AM EST  platform: Windows NT

import sys
import interpol
import Integ
import openmethods
import bracketing
import directsys
import iterativeSys
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

import NumericalAnalysisGUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    NumericalAnalysisGUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    NumericalAnalysisGUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("614x408+520+259")
        top.minsize(160, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("Numerical Analysis")
        top.configure(relief="groove")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.integrationButton = tk.Button(top)
        self.integrationButton.place(relx=0.195, rely=0.123, height=43
                , width=416)
        self.integrationButton.configure(activebackground="#ececec")
        self.integrationButton.configure(activeforeground="#000000")
        self.integrationButton.configure(background="#5bc7e6")
        self.integrationButton.configure(disabledforeground="#a3a3a3")
        self.integrationButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.integrationButton.configure(foreground="#fdfdfd")
        self.integrationButton.configure(highlightbackground="#d9d9d9")
        self.integrationButton.configure(highlightcolor="black")
        self.integrationButton.configure(pady="0")
        self.integrationButton.configure(relief="flat")
        self.integrationButton.configure(text='''Integration''')
        self.integrationButton.bind('<ButtonRelease-1>',
                            lambda e: Integ.vp_start_gui())

        self.InterpolButton = tk.Button(top)
        self.InterpolButton.place(relx=0.195, rely=0.245, height=43, width=416)
        self.InterpolButton.configure(activebackground="#ececec")
        self.InterpolButton.configure(activeforeground="#000000")
        self.InterpolButton.configure(background="#73dbd3")
        self.InterpolButton.configure(cursor="fleur")
        self.InterpolButton.configure(disabledforeground="#a3a3a3")
        self.InterpolButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.InterpolButton.configure(foreground="#fdfdfd")
        self.InterpolButton.configure(highlightbackground="#d9d9d9")
        self.InterpolButton.configure(highlightcolor="black")
        self.InterpolButton.configure(pady="0")
        self.InterpolButton.configure(relief="flat")
        self.InterpolButton.configure(text='''Interpolation''')
        self.InterpolButton.bind('<ButtonRelease-1>',
                            lambda e: interpol.vp_start_gui())

        self.directButton = tk.Button(top)
        self.directButton.place(relx=0.195, rely=0.368, height=43, width=416)
        self.directButton.configure(activebackground="#ececec")
        self.directButton.configure(activeforeground="#000000")
        self.directButton.configure(background="#ec8cd1")
        self.directButton.configure(disabledforeground="#a3a3a3")
        self.directButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.directButton.configure(foreground="#fdfdfd")
        self.directButton.configure(highlightbackground="#d9d9d9")
        self.directButton.configure(highlightcolor="black")
        self.directButton.configure(pady="0")
        self.directButton.configure(relief="flat")
        self.directButton.configure(text='''Systems of equations with direct methods''')
        self.directButton.bind('<ButtonRelease-1>',
                            lambda e: directsys.vp_start_gui())

        self.iterativeButton = tk.Button(top)
        self.iterativeButton.place(relx=0.195, rely=0.49, height=43, width=416)
        self.iterativeButton.configure(activebackground="#ececec")
        self.iterativeButton.configure(activeforeground="#000000")
        self.iterativeButton.configure(background="#5b7cdd")
        self.iterativeButton.configure(disabledforeground="#a3a3a3")
        self.iterativeButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.iterativeButton.configure(foreground="#fdfdfd")
        self.iterativeButton.configure(highlightbackground="#d9d9d9")
        self.iterativeButton.configure(highlightcolor="black")
        self.iterativeButton.configure(pady="0")
        self.iterativeButton.configure(relief="flat")
        self.iterativeButton.configure(text='''Systems of equations with iterative methods''')
        self.iterativeButton.bind('<ButtonRelease-1>',
                            lambda e: iterativeSys.vp_start_gui())

        self.openButton = tk.Button(top)
        self.openButton.place(relx=0.195, rely=0.735, height=43, width=416)
        self.openButton.configure(activebackground="#ececec")
        self.openButton.configure(activeforeground="#000000")
        self.openButton.configure(background="#ff8080")
        self.openButton.configure(disabledforeground="#a3a3a3")
        self.openButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.openButton.configure(foreground="#fdfdfd")
        self.openButton.configure(highlightbackground="#d9d9d9")
        self.openButton.configure(highlightcolor="black")
        self.openButton.configure(pady="0")
        self.openButton.configure(relief="flat")
        self.openButton.configure(text='''Equations of one variable: Open methods''')
        self.openButton.bind('<ButtonRelease-1>',
                            lambda e: openmethods.vp_start_gui())

        self.bracketingButton = tk.Button(top)
        self.bracketingButton.place(relx=0.195, rely=0.613, height=43, width=416)

        self.bracketingButton.configure(activebackground="#ececec")
        self.bracketingButton.configure(activeforeground="#000000")
        self.bracketingButton.configure(background="#bfb5fb")
        self.bracketingButton.configure(disabledforeground="#a3a3a3")
        self.bracketingButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.bracketingButton.configure(foreground="#fdfdfd")
        self.bracketingButton.configure(highlightbackground="#d9d9d9")
        self.bracketingButton.configure(highlightcolor="black")
        self.bracketingButton.configure(pady="0")
        self.bracketingButton.configure(relief="flat")
        self.bracketingButton.configure(text='''Equations of one variable: Bracketing methods''')
        self.bracketingButton.bind('<ButtonRelease-1>',
                             lambda e: bracketing.vp_start_gui())


if __name__ == '__main__':
    vp_start_gui()






