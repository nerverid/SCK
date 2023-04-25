 # Основное окно графическоего интерфейса
from tkinter import *
import tkinter as tk
import listuieditor

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.lbl = Label(self, text = "Test for today")
        self.lbl.grid(row = 0, column = 0, columnspan = 2, sticky=W)

        #self.test_ent = Entry(self)
        #self.test_ent.grid(row = 1, rowspan = 10, column = 0, sticky = W)
        self.test_txt = Text(self, width = 35, height = 10, wrap = WORD)
        self.test_txt.grid(row = 1, rowspan = 10, column = 0, sticky = W)

        self.curr_lbl = Label(self, text = "Current list")
        self.curr_lbl.grid(row = 0, column = 3, columnspan = 2, sticky= E)

        #self.curr_ent = Entry(self)
        #self.curr_ent.grid(row = 1, rowspan = 10, column = 3, sticky = W)
        self.curr_txt = Text(self, width = 35, height = 10, wrap = WORD)
        self.curr_txt.grid(row = 1, rowspan = 10, column = 3, sticky = W)


        self.bttn1 = Button(self, text ="Tests")
        #text1_1 = "The hitchhiker guide to the galaxy, Adam Douglas, p. 23\n Jeeves and Vooster, Woodhouse, p. 145"
        #text2_1 = "English1,\n Haskel\n Python middle"
        self.bttn1["command"] = self.test_work()
        self.bttn1.grid(row = 12, column = 0)

        self.lists_bttn = Button(self, text ="Lists")
        #text1_1 = "The hitchhiker guide to the galaxy, Adam Douglas, p. 23\n Jeeves and Vooster, Woodhouse, p. 145"
        #text2_1 = "English1,\n Haskel\n Python middle"
        self.lists_bttn["command"] = self.list_work()
        self.lists_bttn.grid(row = 12, column = 3)
    
    def update_count(self):
        self.lbl["text"] = "Button is pressed"

    def refresh_text(self, text1 = "Списков нет", text2 = "Тестов нет"):
        self.test_txt.delete(0.0, END)
        self.curr_txt.delete(0.0, END)
        self.test_txt.insert(0.0, text2)
        self.curr_txt.insert(0.0, text1)
    
    def test_work(self):
        pass

    def list_work(self):
        list_window = List_window(self.master)
        list_window.grab_set()
        list_window.focus()
        #listuieditor.start()

class List_window(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        #self.grid()
        self.wait_visibility()
        self.create_widget()

    def create_widget(self):
        self.list_txt = Text(self, width = 35, height = 10, wrap = WORD)
        self.list_txt.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()

"""root = Tk()
root.title("DraftGUI")
root.geometry("580x300")

app = Application(root)

root.mainloop()
"""
