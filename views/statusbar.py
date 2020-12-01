import tkinter as Tk

from utils import observer


# Classe définissant la barre d'état
class StatusBar(observer.Observer):
    def __init__(self, root):
        observer.Observer.__init__(self)
        self.status_bar = Tk.Label(root, text="Non connecté", bd=1, relief=Tk.SUNKEN, anchor=Tk.W)
        self.status_bar.pack(side=Tk.BOTTOM, fill=Tk.X)

    def update_connect_db(self, db):
        self.status_bar.config(text=db)
