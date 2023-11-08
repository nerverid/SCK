#Создание редактирование списков
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.list_txt = Text(self, width = 35, height = 10, wrap = WORD)
        self.list_txt.grid()

def start():
    root = Tk()
    root.title("List editor")
    root.geometry("500x300")

    app = Application(root)
    root.mainloop()
