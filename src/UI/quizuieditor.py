from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.submit_bttn = Button(self, text="Submit")
        self.submit_bttn.grid(row = 8, column = 3)

root = Tk()
root.title("Quiz editor")
root.geometry("500x300")

app = Application(root)

root.mainloop() 