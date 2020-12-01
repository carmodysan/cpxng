import tkinter as Tk

from models import mainmodel
from views import mainview
from controllers import menucontroller


class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model = mainmodel.Model()
        self.view = mainview.View(self.root)
        self.menu_controller = menucontroller.MenuController(self.view, self.root, self.model)

    def run(self):
        self.root.title("Cartes CPx")
        self.root.deiconify()
        self.root.mainloop()
