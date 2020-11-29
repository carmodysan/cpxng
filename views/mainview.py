import tkinter as Tk

from utils import observer
from views import menu


# Classe principale de la vue de l'application. Elle servira de point d'entrée
# à tous les objets de la vue.
class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)

        # Définit le menu principal
        self.menu = menu.Menu(master)
        # Définit la barre d'état
        self.statusbar = StatusBar(master)
        self.statusbar.observe(
            'update_connect_db', self.statusbar.update_connect_db)


# Classe définissant la barre d'état
class StatusBar(observer.Observer):
    def __init__(self, root):
        observer.Observer.__init__(self)
        self.status_bar = Tk.Label(
            root, text="Non connecté", bd=1, relief=Tk.SUNKEN, anchor=Tk.W)
        self.status_bar.pack(side=Tk.BOTTOM, fill=Tk.X)

    def update_connect_db(self, db):
        self.status_bar.config(text=db)
