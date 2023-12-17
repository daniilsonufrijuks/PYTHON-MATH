from tkinter import * 
from tkinter import ttk
from random import *
from math import *

from news_generator import generate_random_news
from equation_gen import quation_gen

def func_sqrt():
    user_input = entry.get()
    result_label3.config(text=str(sqrt(int(user_input))))

def func_random_gen():
    user_input1 = entry2.get()
    user_input2 = entry3.get()
    num = randint(int(user_input1), int(user_input2))
    result_label.config(text=str(num))

def func_random_news_gen():
    result_label2.config(text=str(generate_random_news()))

def equation_gen():
    result_label4.config(text=quation_gen())


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
notebook.add(frame3, text='EQUATION')
notebook.add(frame4, text='NEWS')


entry = Entry(frame1, width=50)
entry.pack(pady=10)


entry2 = Entry(frame2, width=20)
entry2.pack(pady=10)
entry3 = Entry(frame2, width=20)
entry3.pack(pady=20)

result_label = Label(frame2, text="")
result_label.pack(pady=40)

result_label2 = Label(frame4, text="")
result_label2.pack(pady=10)

result_label3 = Label(frame1, text="")
result_label3.pack(pady=10)

result_label4 = Label(frame3, text="")
result_label4.pack(pady=10)


Btn1 = Button(frame1, text="Solve", command=func_sqrt)
Btn1.pack()

Btn2 = Button(frame2, text="Find", command=func_random_gen)
Btn2.pack()

Btn3 = Button(frame4, text="Find", command=func_random_news_gen)
Btn3.pack()

Btn4 = Button(frame3, text="Find", command=equation_gen)
Btn4.pack()



root.mainloop()