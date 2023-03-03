# Основное окно графическоего интерфейса
from tkinter import *

"""def start_gui():
    root = Tk()
    root.title("Draft GUI")
    root.geometry("500x300")

    app = Frame(root)
    app.grid()

    lbl = Label(app, text = "Тесты на сегодня")
    lbl.grid()

    bttn1 = Button(app, text = "Reflash")
    bttn1.grid()

    root.mainloop()

start_gui()"""
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.ceate_widgets()
    
    def create_widgets(self):
        pass