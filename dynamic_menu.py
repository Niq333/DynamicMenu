#encoding: utf-8
"""Приклад 'динамічного меню' - користувач вводить текст і з'являються тільки ті пункти меню, які відповідають введеному тексту. Алгоритм шукає введений текст в документаціях функцій, що відповідають пунктам меню."""

from tkinter import * # імпортувати все з модуля tkinter (Python 3)

def f1():
    """save open file. зберігає відкриває файл""" # рядок документації функції
    f=open("somefile.txt", 'w')# відкрити файл
    # весь текст починаючи з другого рядка окрім останнього символу
    text=self.txt.get('1.0', Tkinter.END)[0:-1]
    f.write(text) #записати у файл
    f.close() #закрити файл

def f2():
    """edit text редагує текст"""
    Text1.delete("1.0", END)
    Text1.insert("1.0", "some text") # вставити

def f3():
    """help допомога"""
    from tkinter import messagebox
    messagebox.showinfo("About","Dynamic Menu Example")

def keyRelease(event=None):
    """Відпускання клавіші під час набору тексту в entry. Динамічно змінює меню відразу після натискання клавіш"""
    menubar.delete(0, END) # очистити меню
    text=Entry1.get()# отримати текст з поля
    #if len(text) in [0,1]: mnu(); return
    print(text) # тільки для відлагодження
    F=set() # множина функцій, що відповідають введеному тексту
    for fn in [f1, f2, f3]: # для кожної функції f1, f2, f3
        if fn.__doc__.find(text)!=-1: # шукає текст серед рядків документації
            F.add(fn) # і додає в множину F, якщо знаходить
        # Примітка: можна ще шукати за регулярним виразом
    mnu(F) # створити меню

def mnu(F=set()):
    """Створює меню з пунктами, які відповідають множині функцій F"""
    empty=len(F)==0 # True якщо множина пуста
    # створити меню і додати до смуги меню
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=f1) # меню відповідає функція f1
    filemenu.add_command(label="Reload",command=f1)
    # якщо функція f1 є у F, або F порожня, то створити меню File
    if f1 in F or empty: menubar.add_cascade(label="File", menu=filemenu)
    # створити меню і додати до смуги меню
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="New",command=f2) # меню відповідає функція f2
    editmenu.add_command(label="Copy",command=f2)
    editmenu.add_separator()
    editmenu.add_command(label="Delete",command=f2)
    if f2 in F or empty: menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=f3)
    if f3 in F or empty: menubar.add_cascade(label="Help", menu=helpmenu)
    # показати меню
    root.config(menu=menubar)


root = Tk() # головне вікно програми
root.title('Dymanic menu app') # надпис на вікні
root.resizable(width=TRUE, height=FALSE) # дозволити зміну розміру вікна по ширині
root.geometry("300x300+0+0") # розмір вікна
menubar = Menu(root)
mnu() # створити меню повністю
s=StringVar() # створити рядкову змінну
Entry1 = Entry(root,textvariable=s,width=50) # створити поле введення, пов'язати зі змінною s
Entry1.bind("<KeyRelease>", keyRelease) # пов'язати подію з функцією keyRelease
Entry1.bind("<Return>", keyRelease) # пов'язати подію з функцією keyRelease
Entry1.pack(side=TOP, fill=X) # розташувати на вікні зверху
s.set("") # установити рядковій змінній значення ""
Button1=Button(root, text="ok", command=f2) # створити кнопку, пов'язати з функцією f2
Button1.pack(side=TOP) # розташувати на вікні зверху
Text1=Text(root) # створити багаторядкове текстове поле
Text1.pack(side=TOP, fill=Y) # розташувати на вікні зверху
root.mainloop() # головний цикл програми (для обробки подій)
