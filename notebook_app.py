from tkinter import * 
from tkinter import ttk
from random import *
from math import *

from news_generator import generate_random_news

def func_sqrt():
    user_input = entry.get()
    print(sqrt(float(user_input)))

def func_random_gen():
    num = randint(0, 1000000000)
    result_label.config(text=str(num))

def func_random_news_gen():
    result_label2.config(text=str(generate_random_news))


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


entry = Entry(frame1, width=50)
entry.pack(pady=10)

result_label = Label(frame2, text="")
result_label.pack(pady=10)

result_label2 = Label(frame4, text="")
result_label2.pack(pady=10)

Btn1 = Button(frame1, text="Solve", command=func_sqrt)
Btn1.pack()

Btn2 = Button(frame2, text="Find", command=func_random_gen)
Btn2.pack()

Btn2 = Button(frame4, text="Find", command=func_random_news_gen)
Btn2.pack()




root.mainloop()