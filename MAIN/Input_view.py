from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook, Treeview
from tkinter.messagebox import showinfo
import os
import shennonFanoCompression as shc
import shennonFanoDecompression as shd

compress = None
decompress = None
de_word = None
de_digital = None
a = 0



def co(text):  # это тестовые функции, нужны, чтобы определить какую функцию куда импортировать
    codded = shc.shennon_fano_compression(str(text)).code
    return codded


def coco(code, code_numbers, code_symbols):
    input_dictionary = dict(zip(code_numbers, code_symbols))
    uncodded = shd.shennon_fano_decompression(code, input_dictionary)
    return uncodded


window = Tk()  # создаю окно
window.state('zoomed')  # функция полного экрана
window.title('Принцип Шинона-Фано')

main_frame = Frame(window)  # создаю рамку
notebook = Notebook(main_frame)
tab1 = Frame(notebook)  # это первая вкладка для закодирования
tab2 = Frame(notebook)  # это вторая вкладка для декодирования

notebook.add(tab1, text='Кодирование')
notebook.add(tab2, text='Декодирование')
dialog_tab1 = Label(tab1, text='Введите текст',
                    font=('Arial', 18))  # диалоговый текст обращения к пользователю в первой вкладке
dialog_tab1.grid(row=2, column=1)

input_text_tab1 = ScrolledText(tab1, width=40, height=4, fg='blue',
                               font=('Arial', 18))  # пользователь в первой вкладке вводит сюда свой текст
input_text_tab1.grid(row=3, column=1)

out_text_tab1 = ScrolledText(tab1, font=('Arial', 18), width=36,
                             height=4)  # в первой вкладке пользователь получит результат в этом окне
out_text_tab1.grid(row=3, column=5)
plus = 47
# out_text_tab1.place(x=943, y=33 + plus)
# out_tab1_scroll.place(x=980, y=180, width=525)
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
    compress = input_text_tab1.get('1.0', END)[0:-1]
    out_text_tab1.insert('1.0', co(compress))
    out_text_tab1.configure(state='disabled')
    # sentence = input_text_tab1.get(1.0, END)
    data = zip(shc.shennon_fano_compression(compress).values,
               shc.shennon_fano_compression(compress).keys)
    count = 0
    for record in table_tab1.get_children():
        table_tab1.delete(record)
    for record in data:
        table_tab1.insert(parent='', index=END, text='', values=(record))
        count += 1


dialog_button_tab1 = Button(tab1, text='Закодировать', font=('Arial', 18), command=compression)  # создаем кнопку
dialog_button_tab1.grid(row=3, column=3)


def open_help():
    if a == 0:
        text = "Метод Шеннона-Фано – это алгоритм сжатия данных, который основывается " \
               "на распределении частоты встречаемости символов в сообщении. Алгоритм Шеннона-Фано разделяет " \
               "символы на две части, соответственно их частоте встречаемости, и далее рекурсивно продолжает " \
               "деление на подгруппы до тех пор, пока не будет получен код для каждого символа в сообщении. " \
               "Код Шеннона-Фано получается из частоты встречаемости символов, которая используется для " \
               "определения места символов в двоичном дереве. В конечном итоге, более часто встречающиеся " \
               "символы имеют более короткие коды, что является причиной сжатия сообщения."
    elif a == 1:
        text = "The Shannon-Fano method is an algorithm used to compress data that allows to obtain " \
               "the frequency distribution or repetition of characters found in a written message." \
               "The algorithm is divided into 2 parts, these 2 parts are divided by frequency (repetition) " \
               "of occurrence and continue to be divided into subgroups until the code of each character " \
               "found in the message is received. The Shannon-Fano code is based on the frequency (repetition)" \
               "of these characters and their occurrence found in the message, from which a" \
               "specific position in that binary tree is determined. The most common or recurring " \
               "characters found in the message are represented with smaller codes."

    elif a == 2:
        text = 'El método Shannon-Fano es un algoritmo utilizado para comprimir datos que permite obtener ' \
               'la distribución de frecuencia o repetición de caracteres encontrados en un mensaje escrito. ' \
               'El algoritmo se divide en 2 partes, estas 2 partes se dividen por frecuencia (repetición) ' \
               'de ocurrencia y continúan dividiéndose en subgrupos hasta que se recibe el código de cada ' \
               'carácter encontrado en el mensaje. El código Shannon-Fano se basa en la frecuencia (repetición) ' \
               'de estos caracteres y su ocurrencia, a partir de la cual se determina una posición específica ' \
               'en ese árbol binario. Los caracteres más comunes o recurrentes que se encuentran ' \
               'en el mensaje tienen códigos más pequeños.'
    else:
        text = "Ты как прогу сломал?"
    showinfo(title="Справка", message=text)


xge = 1170
yge = 300
widh = 180
table_tab1 = Treeview(tab1, columns=('first', 'second'), show='headings')
table_tab1.heading('first', text='Буквы')
table_tab1.heading('second', text='Символы')
table_tab1.column("first", width=widh)
table_tab1.column("second", width=widh)

table_tab1.grid(row=10, column=3)

# создаем все элементы во второй вкладке
dialog_tab2 = Label(tab2, text='Введите бинарный код',
                    font=('Arial', 18))  # Это вывод текста для пользователя
dialog_tab2.grid(row=2, column=1)

input_text_tab2 = ScrolledText(tab2, width=40, height=4, fg='blue', font=('Arial', 18))
input_text_tab2.grid(row=3, column=1)

plus = 43
# out_tab2_scroll = Scrollbar(tab2, orient=HORIZONTAL)

out_text_tab2 = ScrolledText(tab2, font=('Arial', 18), width=36, height=4)
out_text_tab2.place(x=989, y=33 + plus)  # разместил второй вывод по координатам
out_text_tab2.configure(state='disabled')


# out_tab2_scroll.place(x=939, y=180, width=525)


def decompression():
    '''
    аналог функции compression()
    но менять нужно функцию сосо(), на функцию декодирования
    добавление: переменные de_word и de_digital содержат тблицу значений в виде списка
    как их ввел пользователь
    :return:
    '''
    global decompress, de_word, de_digital
    out_text_tab2.configure(state='normal')
    out_text_tab2.delete('1.0', END)
    decompress = input_text_tab2.get('1.0', END)

    de_word = (text_widget_1.get(1.0, END)).split()
    de_digital = text_widget_2.get(1.0, END).split()

    print(de_word)
    print(de_digital)

    out_text_tab2.insert('1.0', coco(decompress, de_digital, de_word))
    out_text_tab2.configure(state='disabled')


dialog_button_tab2 = Button(tab2, text='Раскодировать', font=('Arial', 18), command=decompression)
dialog_button_tab2.place(x=770, y=89 + plus, anchor=CENTER)


# дальше идет не совсем мой код

def mousewheel(evt):
    text_widget_1.yview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows
    text_widget_2.yview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows


def yview(*args):
    text_widget_1.yview(*args)
    text_widget_2.yview(*args)


yg = 200 + plus
scrollbar = Scrollbar(tab2, orient=VERTICAL, command=yview)
scrollbar.place(x=875, y=yg, height=340)  # размещение строки прокрутки

text_widget_1 = Text(tab2, width=10, height=20, yscrollcommand=scrollbar.set, font=('Arial', 11))
text_widget_1.bind_class("Text", '<MouseWheel>', mousewheel)

text_widget_1.place(x=675, y=yg)  # левый текст
text_widget_2 = Text(tab2, width=10, height=20, yscrollcommand=scrollbar.set, font=('Arial', 11))
text_widget_2.bind_class("Text", '<MouseWheel>', mousewheel)
text_widget_2.place(x=775, y=yg)  # размещение правого текста
# вернулись к моему

# работа с картинками и переводом
rus_image_start = PhotoImage(file=r'{}'.format(os.path.abspath("флаг_России.png")))
rus_image = rus_image_start.subsample(x=2, y=2)

ang_image_start = PhotoImage(file=r'{}'.format(os.path.abspath("Английский флаг.png")))
ang_image = ang_image_start.subsample(x=2, y=2)

spa_image_start = PhotoImage(file=r'{}'.format(os.path.abspath("Испанский флаг.png")))
spa_image = spa_image_start.subsample(x=2, y=2)

note_tab1_leng = ['Кодирование', 'Coding', 'Codificación']
note_tab2_leng = ['Декодирование', 'Decoding', 'Decodificación']
dialog_text = ['Введите текст', 'Introduce Text', 'Introducir Texto']
dialog_text_tab2 = ['Введите бинарный код', 'Enter the binary code', 'Introducir codigo binario']
text_button_codify = ['Закодировать', 'Codify', 'Codificar']
text_button_decode = ['Раскодировать', 'Decrypt', 'Descifrar']
# table_text_first = []
#  теперь работа со сменой языка
def configurassions(x):
    notebook.tab(tab1, text=note_tab1_leng[x])
    notebook.tab(tab2, text=note_tab2_leng[x])
    dialog_tab1.configure(text=dialog_text[x])
    dialog_tab2.configure(text=dialog_text_tab2[x])
    dialog_button_tab1.configure(text=text_button_codify[x])
    dialog_button_tab2.configure(text=text_button_decode[x])
    # table_tab1.configure('first', )
def leng_rus():
    global a
    a = 0
    configurassions(a)


def leng_ang():
    global a
    a = 1
    configurassions(a)


def leng_spa():
    global a
    a = 2
    configurassions(a)


button_rus_tab1 = Button(tab1, image=rus_image, command=leng_rus)  # создаем кнопку русского в 1
button_rus_tab1.grid(row=1, column=2)
button_rus_tab2 = Button(tab2, image=rus_image, command=leng_rus)  # создаем кнопку русского в 2
button_rus_tab2.grid(row=1, column=2)

button_ang_tab1 = Button(tab1, image=ang_image, command=leng_ang)  # создаем кнопку английского в 1
button_ang_tab1.grid(row=1, column=3)
button_ang_tab2 = Button(tab2, image=ang_image, command=leng_ang)  # создаем кнопку английского в 2
button_ang_tab2.place(x=743, y=0)

button_spa_tab1 = Button(tab1, image=spa_image, command=leng_spa)  # создаем кнопку испанского в 1
button_spa_tab1.grid(row=1, column=4)
button_spa_tab2 = Button(tab2, image=spa_image, command=leng_spa)  # создаем кнопку испанского в 2
button_spa_tab2.place(x=946, y=0)

quest_mark_start = PhotoImage(
    file=r'{}'.format(os.path.abspath("информационная иконка тёмная.png")))  # картинка вопроса
quest_mark = quest_mark_start.subsample(x=2, y=2)
help_button_tab2 = Button(tab2, image=quest_mark, command=open_help, font=('Arial', 18))
help_button_tab2.grid(row=1, column=1)

help_button_tab1 = Button(tab1, image=quest_mark, command=open_help, font=('Arial', 18))
help_button_tab1.grid(row=1, column=1)  # размещение кнопки справка

notebook.pack(expand=1, fill=BOTH, side=TOP)
main_frame.pack(side=LEFT, padx=25, ipady=340)
window.mainloop()
