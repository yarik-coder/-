from tkinter import *
import os
def comp():
    os.startfile("1main.py")
    exit(0)
def notebook():
    os.startfile("main2.py")
    exit(0)

root = Tk()
root.title("выбор")
root.geometry("400x350")
bt_comp = Button(root, text="для компа", command=comp)
bt_comp.place(x=160, y=100)
bt_notebook = Button(root, text="для ноутбука", command=notebook)
bt_notebook.place(x=150, y=25)
root.mainloop()








































#сука если ты еще раз перепишищь этот код я узнаю кто ты и отпинаю за гаражами