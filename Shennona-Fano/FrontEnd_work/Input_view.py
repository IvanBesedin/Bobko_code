from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook
# from work_eugeny import co

compress = None


def co(a):
    return str(a) + 'hello'


def coco(b):
    return str(b) + 'goodbye'


window = Tk()
window.state('zoomed')
window.title('I expecting more')

a = 'Введите текст для раскодирования'
b = 'Введите текст для кодирования'

main_frame = Frame(window)
notebook = Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text='Кодирование')
notebook.add(tab2, text='Декодирование')
dialog_tab1 = Label(tab1, text=b,
                    font=('Arial', 18))
dialog_tab1.grid(row=1, column=1)

input_text_tab1 = ScrolledText(tab1, width=45, height=4, fg='blue', font=('Arial', 18))
input_text_tab1.grid(row=2, column=1)

out_text_tab1 = ScrolledText(tab1, font=('Arial', 18), width=45, height=4)
out_text_tab1.grid(row=2, column=4)
out_text_tab1.configure(state='disabled')


def compression():
    global compress
    out_text_tab1.configure(state='normal')
    out_text_tab1.delete('1.0', END)
    compress = input_text_tab1.get('1.0', END)
    out_text_tab1.insert('1.0', co(compress))
    out_text_tab1.configure(state='disabled')


dialog_button = Button(tab1, text='Закодировать', font=('Arial', 18), command=compression)
dialog_button.grid(row=2, column=3)

main_frame.pack(side=LEFT, padx=10, ipady=340)

dialog_tab2 = Label(tab2, text=a, font=('Arial', 18))  # Это вывод текста
dialog_tab2.grid(row=1, column=1)

input_text_tab2 = ScrolledText(tab2, width=45, height=4, fg='blue', font=('Arial', 18))
input_text_tab2.grid(row=2, column=1)

out_text_tab2 = ScrolledText(tab2, font=('Arial', 18), width=45, height=4)
out_text_tab2.grid(row=2, column=4)
out_text_tab2.configure(state='disabled')


def decompression():
    global decompress
    out_text_tab2.configure(state='normal')
    out_text_tab2.delete('1.0', END)
    decompress = input_text_tab2.get('1.0', END)
    out_text_tab2.insert('1.0', coco(decompress))
    out_text_tab2.configure(state='disabled')


dialog_button_tab2 = Button(tab2, text='Раскодировать', font=('Arial', 18), command=decompression)
dialog_button_tab2.grid(row=2, column=3)

notebook.pack(expand=1, fill=BOTH, side=TOP)

window.mainloop()
