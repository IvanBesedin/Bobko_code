from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook, Treeview
from tkinter.messagebox import showinfo

window = Tk()  # создаю окно
# window.state('zoomed')  # функция полного экрана
window.title('Принцип Шинона-Фано')

note_tab1_leng = ['Кодирование', 'coding', 'codificación']
main_frame = Frame(window)  # создаю рамку
notebook = Notebook(main_frame)
tab1 = Frame(notebook)  # это первая вкладка для закодирования
tab2 = Frame(notebook)  # это вторая вкладка для декодирования
notebook.add(tab1, text='Кодирование')
notebook.add(tab2, text='Декодирование')
dialog_tab1 = Label(tab1, text='Введите текст для кодирования', font=('Arial', 18))  # диалоговый текст обращения к пользователю в первой вкладке
dialog_tab1.grid(row=2, column=1)
def configurassions(x):
    notebook.tab(tab1, text=note_tab1_leng[x])
def leng_rus():
    global a
    a = 0
    configurassions(a)
dialog_button_tab1 = Button(tab1, text='Закодировать', font=('Arial', 18), command=leng_rus)  # создаем кнопку
dialog_button_tab1.grid(row=3, column=3)
notebook.pack(expand=1, fill=BOTH, side=TOP)
main_frame.pack(side=LEFT, padx=25, ipady=340)
window.mainloop()
