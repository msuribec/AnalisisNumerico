#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 14, 2020 02:34:46 PM EST  platform: Windows NT

import sys

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

import Integ_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Integ_support.set_Tk_var()
    top = Toplevel1 (root)
    Integ_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    Integ_support.set_Tk_var()
    top = Toplevel1 (w)
    Integ_support.init(w, top, *args, **kwargs)
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+579+257")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("Integration")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.choiceInteg = ttk.Combobox(top)
        self.choiceInteg.place(relx=0.35, rely=0.089, relheight=0.058
                , relwidth=0.495)
        self.value_list = ['trapezoid','trapezoid generalized','simpson 1/3','simpson 1/3 generalized','simpson 3/8',]
        self.choiceInteg.configure(values=self.value_list)
        self.choiceInteg.configure(textvariable=Integ_support.combobox)
        self.choiceInteg.configure(takefocus="")

        self.functionEntry = tk.Entry(top)
        self.functionEntry.place(relx=0.35, rely=0.2, height=24, relwidth=0.507)
        self.functionEntry.configure(background="white")
        self.functionEntry.configure(disabledforeground="#a3a3a3")
        self.functionEntry.configure(font="TkFixedFont")
        self.functionEntry.configure(foreground="#000000")
        self.functionEntry.configure(highlightbackground="#d9d9d9")
        self.functionEntry.configure(highlightcolor="black")
        self.functionEntry.configure(insertbackground="black")
        self.functionEntry.configure(selectbackground="blue")
        self.functionEntry.configure(selectforeground="white")

        self.valueaEntry = tk.Entry(top)
        self.valueaEntry.place(relx=0.35, rely=0.311, height=24, relwidth=0.173)
        self.valueaEntry.configure(background="white")
        self.valueaEntry.configure(cursor="fleur")
        self.valueaEntry.configure(disabledforeground="#a3a3a3")
        self.valueaEntry.configure(font="TkFixedFont")
        self.valueaEntry.configure(foreground="#000000")
        self.valueaEntry.configure(highlightbackground="#d9d9d9")
        self.valueaEntry.configure(highlightcolor="black")
        self.valueaEntry.configure(insertbackground="black")
        self.valueaEntry.configure(selectbackground="blue")
        self.valueaEntry.configure(selectforeground="white")

        self.valuebEntry = tk.Entry(top)
        self.valuebEntry.place(relx=0.35, rely=0.422, height=24, relwidth=0.173)
        self.valuebEntry.configure(background="white")
        self.valuebEntry.configure(disabledforeground="#a3a3a3")
        self.valuebEntry.configure(font="TkFixedFont")
        self.valuebEntry.configure(foreground="#000000")
        self.valuebEntry.configure(highlightbackground="#d9d9d9")
        self.valuebEntry.configure(highlightcolor="black")
        self.valuebEntry.configure(insertbackground="black")
        self.valuebEntry.configure(selectbackground="blue")
        self.valuebEntry.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.217, rely=0.2, height=26, width=62)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Function''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.3, rely=0.311, height=26, width=14)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''a''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.3, rely=0.422, height=26, width=15)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''b''')

        self.resultMessage = tk.Message(top)
        self.resultMessage.place(relx=0.467, rely=0.578, relheight=0.222
                , relwidth=0.36)
        self.resultMessage.configure(background="#ffffff")
        self.resultMessage.configure(cursor="fleur")
        self.resultMessage.configure(foreground="#000000")
        self.resultMessage.configure(highlightbackground="#d9d9d9")
        self.resultMessage.configure(highlightcolor="black")
        self.resultMessage.configure(text='''Result''')
        self.resultMessage.configure(width=216)

        self.runButton = tk.Button(top)
        self.runButton.place(relx=0.25, rely=0.622, height=43, width=96)
        self.runButton.configure(activebackground="#ececec")
        self.runButton.configure(activeforeground="#000000")
        self.runButton.configure(background="#70b6b0")
        self.runButton.configure(cursor="fleur")
        self.runButton.configure(disabledforeground="#a3a3a3")
        self.runButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.runButton.configure(foreground="#ffffff")
        self.runButton.configure(highlightbackground="#d9d9d9")
        self.runButton.configure(highlightcolor="black")
        self.runButton.configure(pady="0")
        self.runButton.configure(relief="flat")
        self.runButton.configure(text='''R U N''')
        self.runButton.bind('<ButtonRelease-1>', lambda e: Integ_support.runMethod(self.choiceInteg, self.functionEntry,
                                                                                   self.valueaEntry, self.valuebEntry,
                                                                                   self.resultMessage,self.intervalsEntry))

        self.gobackButton = tk.Button(top)
        self.gobackButton.place(relx=0.383, rely=0.867, height=33, width=126)
        self.gobackButton.configure(activebackground="#ececec")
        self.gobackButton.configure(activeforeground="#000000")
        self.gobackButton.configure(background="#acd5d1")
        self.gobackButton.configure(disabledforeground="#a3a3a3")
        self.gobackButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.gobackButton.configure(foreground="#ffffff")
        self.gobackButton.configure(highlightbackground="#d9d9d9")
        self.gobackButton.configure(highlightcolor="black")
        self.gobackButton.configure(pady="0")
        self.gobackButton.configure(relief="flat")
        self.gobackButton.configure(text='''GO BACK''')

        self.intervalsEntry = tk.Entry(top)
        self.intervalsEntry.place(relx=0.35, rely=0.511, height=24
                , relwidth=0.173)
        self.intervalsEntry.configure(background="white")
        self.intervalsEntry.configure(disabledforeground="#a3a3a3")
        self.intervalsEntry.configure(font="TkFixedFont")
        self.intervalsEntry.configure(foreground="#000000")
        self.intervalsEntry.configure(insertbackground="black")
        self.intervalsEntry.configure(selectbackground="#007878d7d777")

        self.Label3_1 = tk.Label(top)
        self.Label3_1.place(relx=0.083, rely=0.511, height=26, width=145)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#ffffff")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Number of intervals N''')

if __name__ == '__main__':
    vp_start_gui()




