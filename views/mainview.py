from PIL import Image, ImageTk
import tkinter as Tk

import fontawesome as fa

from utils import observer
from views import menu


# Classe principale de la vue de l'application. Elle servira de point d'entrée
# à tous les objets de la vue.
class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        master.attributes('-zoomed', True)

        # Définit le menu principal
        self.menu = menu.Menu(master)

        self.logo = Logo(master)
        self.sidepanel = SidePanel(master)
        self.top_toolbar = TopToolBar(master)


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


class SidePanel():
    def __init__(self, root):
        self.frame_side_panel = Tk.Frame(root, bg='#91c46b') #Police : #517a3e

        self.img = Image.open("ressources/sign-out-alt.png").resize((32, 32))
        self.eimg = ImageTk.PhotoImage(self.img)

        self.label = Tk.Label(self.frame_side_panel, image=self.eimg, bg='#91c46b')
        self.label.image = self.eimg
        self.label.pack(side=Tk.TOP, padx=10, pady=10)

        self.frame_side_panel.pack(side=Tk.LEFT, fill=Tk.Y)

        #self.frame_side_panel.pack(side=Tk.LEFT, fill=Tk.Y, expand=1)
        #self.button_about = Tk.Button(self.frame_side_panel, text='?')
        #self.button_about.pack(side='top', fill=Tk.BOTH)
        #self.button_connect_db = Tk.Button(self.frame_side_panel, text='Connect')
        #self.button_connect_db.pack(side='top', fill=Tk.BOTH)

class TopToolBar():
    def __init__(self, root):
        self.frame_top_tb = Tk.Frame(root, bg='#34383c') #Police : #6f7176

        self.img = Image.open("ressources/exit.png")
        eimg = ImageTk.PhotoImage(self.img)

        exitButton = Tk.Button(self.frame_top_tb, image=eimg, relief=Tk.FLAT, width='40')
        exitButton.image = eimg
        exitButton.pack(side=Tk.LEFT, padx=2, pady=2)

        self.frame_top_tb.pack(side=Tk.TOP, fill=Tk.X)

class Logo():
    def __init__(self, root):
        self.frame_logo = Tk.Frame(root, bg='#1d2226')

        self.img_logo = Image.open("ressources/logo.png").resize((32, 32))
        self.eimg_logo = ImageTk.PhotoImage(self.img_logo)

        #1d2226 for black logo <i class="fas fa-sign-out-alt"></i>
        label = Tk.Label(self.frame_logo, image=self.eimg_logo, bg='#1d2226')
        label.pack(side=Tk.LEFT, padx=10, pady=10)

        self.frame_logo.pack(side=Tk.LEFT, fill=Tk.NONE, anchor=Tk.NW)
