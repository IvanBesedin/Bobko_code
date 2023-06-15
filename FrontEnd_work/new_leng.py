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

rus_image_start = PhotoImage(file=r'C:\Users\Zero\PycharmProjects\Bobko_code\buttons\75_pixels.png')
rus_image = rus_image_start.subsample(x=2, y=2)

ang_image_start = PhotoImage(file=r'C:\Users\Zero\PycharmProjects\Bobko_code\buttons\Английский флаг.png')
ang_image = ang_image_start.subsample(x=2, y=2)

spa_image_start = PhotoImage(file=r'C:\Users\Zero\PycharmProjects\Bobko_code\buttons\Испанский флаг.png')
spa_image = spa_image_start.subsample(x=2, y=2)
dialog_tab1 = Label(tab1, text='Введите текст для кодирования', font=('Arial', 18))  # диалоговый текст обращения к пользователю в первой вкладке
dialog_tab1.grid(row=2, column=0)
def configurassions(x):
    notebook.tab(tab1, text=note_tab1_leng[x])
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
button_rus_tab1 = Button(tab1, image=rus_image, command=leng_rus)  # создаем кнопку
button_rus_tab1.grid(row=1, column=1)

button_ang_tab1 = Button(tab1, image=ang_image, command=leng_ang)  # создаем кнопку
button_ang_tab1.grid(row=1, column=2)

button_spa_tab1 = Button(tab1, image=spa_image, command=leng_spa)  # создаем кнопку
button_spa_tab1.grid(row=1, column=3)

notebook.pack(expand=1, fill=BOTH, side=TOP)
main_frame.pack(side=LEFT, padx=25, ipady=340)
window.mainloop()
