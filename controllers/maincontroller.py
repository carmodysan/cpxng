import tkinter as Tk

from models import mainmodel
from views import mainview
from controllers import menucontroller
from utils import log


class Controller():
    def __init__(self):
        self.logger = log.Logger.Instance()
        self.logger.appinfo('Initialising Controller...')

        self.root = Tk.Tk()
        self.model = mainmodel.Model()
        self.view = mainview.View(self.root)
        self.menu_controller = menucontroller.MenuController(self.view, self.root, self.model)

        self.logger.appinfo('Controller initialised')

    def run(self):
        self.root.title('Cartes CPx NG')
        self.root.deiconify()

        self.logger.appinfo('Entering in the main loop of app')
        self.root.mainloop()
