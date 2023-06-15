# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()
root.title("Переключение языков")

# Словарь с переводами слов на разные языки
translations = {
    "русский": {"Привет": "Привет", "Как дела?": "Как дела?", "Пока": "Пока"},
    "английский": {"Привет": "Hello", "Как дела?": "How are you?", "Пока": "Goodbye"},
    "испанский": {"Привет": "Hola", "Как дела?": "Cómo estás?", "Пока": "Hasta luego"}
}


# Функция для переключения языков
def switch_language(lang):
    for key, value in translations[lang].items():
        labels[key].config(text=value)


# Создание изображений и кнопок выбора языка
russian_img = PhotoImage(file="ru.jpeg")
russian_button = Button(root, image=russian_img, command=lambda: switch_language("русский"), )
russian_button.pack(side=LEFT)

english_img = PhotoImage(file="flag-velikobritanii.png")
english_button = Button(root, image=english_img, command=lambda: switch_language("английский"))
english_button.pack(side=LEFT)

spanish_img = PhotoImage(file="spain.png")
spanish_button = Button(root, image=spanish_img, command=lambda: switch_language("испанский"))
spanish_button.pack(side=LEFT)

# Создание меток для слов на разных языках
labels = {}
for key, value in translations['русский'].items():
    labels[key] = Label(root, text=value)
    labels[key].pack()
# russian_img()
# english_img()
# spanish_img()

root.mainloop()
