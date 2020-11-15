#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 14, 2020 07:16:19 PM EST  platform: Windows NT

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

import directsys_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    directsys_support.set_Tk_var()
    top = Toplevel1(root)
    directsys_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    directsys_support.set_Tk_var()
    top = Toplevel1(w)
    directsys_support.init(w, top, *args, **kwargs)
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
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("600x450+647+251")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Integration")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.choiceInteg = ttk.Combobox(top)
        self.choiceInteg.place(relx=0.35, rely=0.089, relheight=0.058
                               , relwidth=0.495)
        self.value_list = ['GaussianElimination', 'GaussPartialPivot', 'GaussTotal pivot', 'LUFact',
                           'LUPartialPivoting', 'Cholesky', 'Crout', 'Doolittle', ]
        self.choiceInteg.configure(values=self.value_list)
        self.choiceInteg.configure(textvariable=directsys_support.combobox)
        self.choiceInteg.configure(takefocus="")

        self.matrixEntry = tk.Entry(top)
        self.matrixEntry.place(relx=0.35, rely=0.2, height=24, relwidth=0.507)
        self.matrixEntry.configure(background="white")
        self.matrixEntry.configure(disabledforeground="#a3a3a3")
        self.matrixEntry.configure(font="TkFixedFont")
        self.matrixEntry.configure(foreground="#000000")
        self.matrixEntry.configure(highlightbackground="#d9d9d9")
        self.matrixEntry.configure(highlightcolor="black")
        self.matrixEntry.configure(insertbackground="black")
        self.matrixEntry.configure(selectbackground="blue")
        self.matrixEntry.configure(selectforeground="white")

        self.vectorEntry = tk.Entry(top)
        self.vectorEntry.place(relx=0.35, rely=0.311, height=24, relwidth=0.173)
        self.vectorEntry.configure(background="white")
        self.vectorEntry.configure(disabledforeground="#a3a3a3")
        self.vectorEntry.configure(font="TkFixedFont")
        self.vectorEntry.configure(foreground="#000000")
        self.vectorEntry.configure(highlightbackground="#d9d9d9")
        self.vectorEntry.configure(highlightcolor="black")
        self.vectorEntry.configure(insertbackground="black")
        self.vectorEntry.configure(selectbackground="blue")
        self.vectorEntry.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.217, rely=0.2, height=26, width=48)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Matrix''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.233, rely=0.311, height=26, width=47)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''vector''')

        self.runButton = tk.Button(top)
        self.runButton.place(relx=0.25, rely=0.622, height=43, width=96)
        self.runButton.configure(activebackground="#ececec")
        self.runButton.configure(activeforeground="#000000")
        self.runButton.configure(background="#70b6b0")
        self.runButton.configure(disabledforeground="#a3a3a3")
        self.runButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.runButton.configure(foreground="#ffffff")
        self.runButton.configure(highlightbackground="#d9d9d9")
        self.runButton.configure(highlightcolor="black")
        self.runButton.configure(pady="0")
        self.runButton.configure(relief="flat")
        self.runButton.configure(text='''R U N''')
        self.runButton.bind('<ButtonRelease-1>',
                            lambda e: directsys_support.runMethod(self.choiceInteg, self.matrixEntry,
                                                                  self.vectorEntry, self.Scrolledtext1))

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

        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(relx=0.467, rely=0.489, relheight=0.307
                                 , relwidth=0.382)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="blue")
        self.Scrolledtext1.configure(selectforeground="white")
        self.Scrolledtext1.configure(wrap="none")


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
