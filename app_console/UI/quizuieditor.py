from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):

        self.menu_bttn = Button(self, text="Menu")
        self.menu_bttn.grid(row = 1, column = 5)

        self.question_txt = Text(self, width = 25, height = 5, wrap = WORD)
        self.question_txt.grid(row = 2, column = 3, columnspan = 2)

        self.quest1_chckbtn = Checkbutton(self)
        self.quest1_chckbtn.grid(row = 4, column = 2)

        self.ask1_txt = Text(self, width = 25, height = 2, wrap= WORD)
        self.ask1_txt.grid(row = 4, column = 4)

        self.quest2_chckbtn = Checkbutton(self)
        self.quest2_chckbtn.grid(row = 5, column = 2)

        self.ask2_txt = Text(self, width = 25, height = 2, wrap= WORD)
        self.ask2_txt.grid(row = 5, column = 4)

        self.quest3_chckbtn = Checkbutton(self)
        self.quest3_chckbtn.grid(row = 6, column = 2)

        self.ask3_txt = Text(self, width = 25, height = 2, wrap= WORD)
        self.ask3_txt.grid(row = 6, column = 4)

        self.quest4_chckbtn = Checkbutton(self)
        self.quest4_chckbtn.grid(row = 7, column = 2)

        self.ask4_txt = Text(self, width = 25, height = 2, wrap= WORD)
        self.ask4_txt.grid(row = 7, column = 4)

        self.submit_bttn = Button(self, text="Submit")
        self.submit_bttn.grid(row = 8, column = 3)

root = Tk()
root.title("Quiz editor")
root.geometry("500x300")

app = Application(root)

root.mainloop() 