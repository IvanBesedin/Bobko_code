from tkinter import *

def change_language():
    languages = ['English', 'Russian', 'Spanish'] # языки
    selection = Listbox(root) # список для выбора языка
    selection.insert(END, *languages) # добавляем языки в список
    selection.place(relx=0.25, rely=0.25) # список по центру

root = Tk()

# изображение кнопки
img = PhotoImage(file='language.png')

# кнопка
btn = Button(root, image=img, command=change_language)

# кнопка в окне
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()