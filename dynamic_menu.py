#encoding: utf-8

from tkinter import *

def f1():
    """save open file. зберігає відкриває файл"""
    pass

def f2():
    """edit text редагує текст"""
    pass

def keyRelease(event=None):
    menubar.delete(0, END)
    text=Entry1.get()
    F=set()
    for fn in [f1, f2, f3]:
        if fn.__doc__.find(text)!=-1:
            F.add(fn)
    mnu(F)

def mnu(F=set()):
    empty=len(F)==0
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=f1)
    filemenu.add_command(label="Reload",command=f1)
    if f1 in F or empty: menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="New",command=f2) # меню відповідає функція f2
    editmenu.add_command(label="Copy",command=f2)
    editmenu.add_separator()
    editmenu.add_command(label="Delete",command=f2)
    if f2 in F or empty: menubar.add_cascade(label="Edit", menu=editmenu)
    root.config(menu=menubar)


root = Tk()
root.title('Dymanic menu app')
root.resizable(width=TRUE, height=FALSE)
root.geometry("200x200+0+0")
menubar = Menu(root)
mnu()
s=StringVar()
Entry1 = Entry(root,textvariable=s,width=40)
Entry1.bind("<KeyRelease>", keyRelease)
Entry1.pack(side=TOP, fill=X)
root.mainloop()
