from tkinter import * 
from tkinter import ttk
from random import *
from math import *

def func_sqrt():
    print(sqrt(4))

def func_random_gen():
    print(randint(0, 1000000000))


# root window
root = Tk()
root.geometry('600x550')
root.title('Your Helper')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create/add frames
frame1 = ttk.Frame(notebook, width=600, height=550)
frame2 = ttk.Frame(notebook, width=600, height=550)
frame3 = ttk.Frame(notebook, width=600, height=550)
frame4 = ttk.Frame(notebook, width=600, height=550)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

notebook.add(frame1, text='SQRT')
notebook.add(frame2, text='RANDOM')
notebook.add(frame3, text='AI HELP')
notebook.add(frame4, text='NEWS')



Btn1 = Button(frame1, text="Solve", command=func_sqrt)
Btn1.pack()

Btn2 = Button(frame2, text="Find", command=func_random_gen)
Btn2.pack()



root.mainloop()