from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext

root = Tk()
root.title("ШЕННОН ФАНО")
root.geometry('1400x900')
files = filedialog.askopenfilenames()
n = filedialog.asksaveasfilename()
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Зашифровать')
Labeltab1 = scrolledtext.ScrolledText(tab1, fg="white", bg="black", width=20, height=20)
Labeltab1.pack()
Labeltab2 = scrolledtext.ScrolledText(tab1, fg="white", bg="black", width=20, height=20, padx=10, pady=-10)
Labeltab2.pack()
tab2 = ttk.Frame(tab_control)
tab2 = Label(text="Окей бумер", fg="white", bg="black", width=200, height=20)
tab_control.add(tab2, text='Разшифровать')
tab_control.pack(expand=1, fill='both', padx=100)


root.mainloop()

