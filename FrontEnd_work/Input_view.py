from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook, Treeview

# from work_eugeny import co

compress = None


def co(a):  # это тестовые функции, нужны, чтобы определить какую функцию куда импортировать
    return str(a) + 'hello'


def coco(b):
    return str(b) + 'goodbye'


window = Tk()  # создаю окно
window.state('zoomed')  # функция полного экрана
window.title('Принцип Шинона-Фано')

a = 'Введите текст для раскодирования'
b = 'Введите текст для кодирования'

main_frame = Frame(window)  # создаю рамку
notebook = Notebook(main_frame)
tab1 = Frame(notebook)  # это первая вкладка для закодирования
tab2 = Frame(notebook)  # это вторая вкладка для декодирования

notebook.add(tab1, text='Кодирование')
notebook.add(tab2, text='Декодирование')
dialog_tab1 = Label(tab1, text=b, font=('Arial', 18))  # диалоговый текст обращения к пользователю в первой вкладке
dialog_tab1.grid(row=1, column=1)

input_text_tab1 = ScrolledText(tab1, width=40, height=4, fg='blue',
                               font=('Arial', 18))  # пользователь в первой вкладке вводит сюда свой текст
input_text_tab1.grid(row=2, column=1)

out_text_tab1 = ScrolledText(tab1, font=('Arial', 18), width=40,
                             height=4)  # в первой вкладке пользователь получит результат в этом окне
out_text_tab1.grid(row=2, column=4)
out_text_tab1.configure(state='disabled')  # отключаем, чтобы невозможно было ей пользоваться


def compression():
    '''
    Функция compression активируется при нажатии на кнопку в первой вкладке
    сначала выводимый текст делаем активным, чтобы в него можно было поместить итоговый результат
    потом получаем значение, которое ввел пользователь в переменную compress,
    причем compress глобальная переменная и её, вроде можно импортировать
    функция со() - это тестовая функция, вместо неё должна быть функция, которая выводит закодированное значение
    в виде строки.
    :return:
    '''
    global compress
    out_text_tab1.configure(state='normal')
    out_text_tab1.delete('1.0', END)
    compress = input_text_tab1.get('1.0', END)
    out_text_tab1.insert('1.0', co(compress))
    out_text_tab1.configure(state='disabled')


dialog_button_tab1 = Button(tab1, text='Закодировать', font=('Arial', 18), command=compression)  # создаем кнопку
dialog_button_tab1.grid(row=2, column=3)


def data_table_tab1():
    sentence = input_text_tab1.get(1.0, END)
    data = list(sentence)
    count = 0
    for record in table_tab1.get_children():
        table_tab1.delete(record)
    for record in data:
        table_tab1.insert(parent='', index=END, text='', values=(record[0]))
        count += 1


table_tab1 = Treeview(tab1, columns=('first', 'second'), show='headings')
table_tab1.heading('first', text='Буквы')
table_tab1.heading('second', text='Символы')
table_tab1.grid(row=10, column=3)

btn_table_tab1 = Button(tab1, text='Отобразить в таблице', command=data_table_tab1, font=('Arial', 18))
btn_table_tab1.grid(row=10, column=1)

# создаем все элементы во второй вкладке
dialog_tab2 = Label(tab2, text=a, font=('Arial', 18))  # Это вывод текста для пользователя
dialog_tab2.grid(row=1, column=1)

input_text_tab2 = ScrolledText(tab2, width=40, height=4, fg='blue', font=('Arial', 18))
input_text_tab2.grid(row=2, column=1)

out_text_tab2 = ScrolledText(tab2, font=('Arial', 18), width=40, height=4)
out_text_tab2.grid(row=2, column=5)
out_text_tab2.configure(state='disabled')


def decompression():
    '''
    аналог функции compression()
    но менять нужно функцию сосо(), на функцию декодирования
    :return:
    '''
    global decompress
    out_text_tab2.configure(state='normal')
    out_text_tab2.delete('1.0', END)
    decompress = input_text_tab2.get('1.0', END)

    out_text_tab2.insert('1.0', coco(decompress))
    out_text_tab2.configure(state='disabled')


# def spin_entry():
#     try:
#         flag = 0
#         val = int(spin_tab2.get())
#         for i in range(val):
#             k = i
#             ent = Entry(tab2, font=('Arial', 11))
#             ent.grid(row=4 + k, column=2 + flag)
#             ent_2 = Entry(tab2, font=('Arial', 11))
#             ent_2.grid(row=4+k, column=3)
#     except TypeError:
#         print('error')


dialog_button_tab2 = Button(tab2, text='Раскодировать', font=('Arial', 18), command=decompression)
dialog_button_tab2.grid(row=3, column=1)


# дальше идет не совсем мой код

def mousewheel(evt):
    text_widget_1.yview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows
    text_widget_2.yview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows


def yview(*args):
    text_widget_1.yview(*args)
    text_widget_2.yview(*args)


scrollbar = Scrollbar(tab2, orient=VERTICAL, command=yview)
scrollbar.grid(row=4, column=4, sticky=N + S)

text_widget_1 = Text(tab2, width=10, height=20, yscrollcommand=scrollbar.set, font="consolas 14")
text_widget_1.bind_class("Text", '<MouseWheel>', mousewheel)
text_widget_1.grid(row=4, column=2)

text_widget_2 = Text(tab2, width=10, height=20, yscrollcommand=scrollbar.set, font="consolas 14")
text_widget_2.bind_class("Text", '<MouseWheel>', mousewheel)
text_widget_2.grid(row=4, column=3, padx=2)

notebook.pack(expand=1, fill=BOTH, side=TOP)
main_frame.pack(side=LEFT, padx=25, ipady=340)
window.mainloop()
