import tkinter as Tk
from tkinter import messagebox

from db import mariadb


# Classe définissant le menu de l'application
class Menu():
    def __init__(self, root):
        self.menu = Tk.Menu(root)
        root.config(menu=self.menu)

        # File Menu
        self.file_menu = Tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Fichier", menu=self.file_menu)
        self.file_menu.add_command(
            label="Quitter le logiciel", command=lambda: self.menu_quit(root))
        self.file_menu.add_command(
            label="Connexion", command=self.menu_connect)

        # About Menu
        self.about_menu = Tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="A propos", menu=self.about_menu)
        self.about_menu.add_command(label="About", command=self.menu_about)

    def menu_quit(self, root):
        db = mariadb.MariaDB.Instance()
        db.close_connection()
        root.destroy()

    def menu_about(self):
        messagebox.showinfo("Ceci est un essai :", "Le")

    def menu_connect(self):
        db = mariadb.MariaDB.Instance()
        db.query_refer("SELECT * FROM essai")
        db.query_cartes("SELECT * FROM essai")
