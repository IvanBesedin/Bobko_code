from tkinter import *
from tkinter import ttk


def codify():
    sentence = t.get(1.0, END)
    t_out.delete(1.0, END)
    t_out.insert(1.0, sentence)


def data_t():
    sentence = t.get(1.0, END)
    data = list(sentence)
    count = 0
    for record in table.get_children():
        table.delete(record)
    for record in data:
        table.insert(parent='', index=END, text='', values=(record[0]))
        count += 1
    table.grid(row=10, column=0)


win = Tk()
win.title("Кодировщик по методу Шенона фано")

t = Text(win, width=20, height=6)
t.grid(column=0, row=1, sticky='we')
t_out = Text(win, width=20, height=6)
t_out.grid(column=3, row=1, sticky='we')

btn1 = Button(win, text='Закодировать', command=codify).grid(row=1, column=1)
btn2 = Button(win, text='Таблица', command=data_t).grid(row=2, column=1)
btn3 = Button(win, text='Раскодировать').grid(row=1, column=2)

lbl_in = Label(text='Вход').grid(row=0, column=0, sticky='we')
lbl_out = Label(text='Выход').grid(row=0, column=3, sticky='we')

table = ttk.Treeview(win, columns=('first', 'second'), show='headings')
table.heading('first', text='Буквы')
table.heading('second', text='Символы')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_columnconfigure(3, minsize=200)

win.mainloop()
