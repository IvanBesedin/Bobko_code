from shennonFanoCompression import shennon_fano_compression
result = shennon_fano_compression()
x = result.dictionary
tabl = []

for cod, letters in x.items():
    tabl.append([letters, cod])

print(tabl)



from tkinter import *
from tkinter import ttk
def codify(path = "data_set\\message.txt"):
    sentence = t.get(1.0,END)
    text_file = open(path, 'w')
    text_file.write(sentence)
    text_file.close()

def data_t():

    data = tabl
    for record in table.get_children():
        table.delete(record)
    count=0
    for record in data:
        table.insert(parent='', index=END, iid=count, text='', values=(record[0], record[1]))
        count+=1
    table.grid(row=	3, column=3, sticky='we')




win = Tk()
win.title("Кодировщик по методу Шенона фано")
#win.iconbitmap()
#photo = PhotoImage(file=)

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
table.heading('second', text='Симболы')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=200)
win.grid_columnconfigure(3, minsize=200)


win.mainloop()