import tkinter as Tk

from models import mainmodel
from views import mainview


class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model = mainmodel.Model()
        self.view = mainview.View(self.root)

    def run(self):
        self.root.title("Cartes CPx")
        self.root.deiconify()
        self.root.mainloop()
