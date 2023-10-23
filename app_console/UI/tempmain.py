import tkinter as tk

class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.show_widgets()

    def show_widgets(self):
        self.frame = tk.Frame(self.master)
        self.master.title("SCK")
        
        self.lbl = tk.Label(self.frame, text = "Test for today")
        self.lbl.grid(row = 0, column = 0, columnspan = 2)
        self.lbl.pack()
        self.test_txt = tk.Text(self.frame, width = 35, height=10)
        #self.test_txt.grid(row = 1, rowspan = 10, column = 0)
        self.test_txt.pack()

        self.btn_lists = tk.Button(self.frame, text="Lists", command=self.open_list)
        #self.btn_lists.grid(row = 1, column = 2, columnspan = 1)
        self.btn_lists.pack()

        self.frame.pack()
        
    def open_list(self):
        global win_list
        win_list = ListEditUI
        win_list = tk.Toplevel(self.master)
        win_list.focus()

    def if_win_opened():
        pass
        
class QuizUI:
    def __init__(self):
        pass
    
    def show_widgets(self):
        pass

class ListEditUI(Application):
    if_opend = False
    def __init__(self):
        self.lbl = tk.Label(self.frame, text = "List for today")
        #self.lbl.grid(row = 0, column = 0, columnspan = 2)
        if_opend = True #Устанвливается если уже экземпляр уже запущен.
        # Лучше здесь использовать паттерн "Синглентон"
        self.lbl.pack()
    def show_widgets(self):
        #self.lbl = tk.Label(self.frame, text = "List for today")
        #self.lbl.grid(row = 0, column = 0, columnspan = 2)
        #self.lbl.pack()
        pass
    
    def exit_on_close():
        if_opend = False

root = tk.Tk()
app = Application(root)
root.mainloop()
