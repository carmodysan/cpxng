from PIL import Image, ImageTk
import tkinter as Tk
from sys import platform

from utils import observer
from views import menu


# Classe principale de la vue de l'application. Elle servira de point d'entrée
# à tous les objets de la vue.
class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)

        # Check operating system to maximize window correctly
        if platform == 'linux':
            master.attributes('-zoomed', True)  # For Linux
        elif platform == 'win32' or platform == 'cygwin':
            master.state('zoomed')  # For Windows

        # Définit la barre d'état
        self.statusbar = StatusBar(master)
        self.statusbar.observe(
            'update_connect_db', self.statusbar.update_connect_db)

        # The left frame contains logo and possible actions
        self.left_frame = Tk.Frame(master)
        self.logo = Logo(self.left_frame)
        self.sidepanel = SidePanel(self.left_frame)
        self.left_frame.pack(side=Tk.LEFT, fill=Tk.Y, anchor=Tk.NW)

        # The top frame contains the toolbar
        self.top_toolbar = TopToolBar(master)

        # The main frame contains the content
        self.main_frame = Tk.Frame(master)
        content = Tk.Label(self.main_frame, text="My super content !")
        content.pack(side=Tk.TOP, fill=Tk.BOTH, expand=Tk.YES)
        self.main_frame.pack(side=Tk.TOP, fill=Tk.BOTH, anchor=Tk.CENTER)


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
        self.frame_side_panel = Tk.Frame(root, bd=1, bg='#91c46b')

        # Quit module
        self.img_quit = Image.open("ressources/sign-out-alt.png").resize((32, 32))
        self.eimg_quit = ImageTk.PhotoImage(self.img_quit)
        self.img_quit_active = Image.open("ressources/sign-out-alt-active.png").resize((32, 32))
        self.eimg_quit_active = ImageTk.PhotoImage(self.img_quit_active)

        self.label_quit = Tk.Label(self.frame_side_panel, image=self.eimg_quit, bg='#91c46b')
        self.label_quit.image = self.eimg_quit
        self.label_quit.pack(side=Tk.TOP, padx=10, pady=10)

        self.frame_side_panel.pack(side=Tk.TOP, fill=Tk.Y, expand=Tk.YES)

        #self.frame_side_panel.pack(side=Tk.LEFT, fill=Tk.Y, expand=1)
        #self.button_about = Tk.Button(self.frame_side_panel, text='?')
        #self.button_about.pack(side='top', fill=Tk.BOTH)
        #self.button_connect_db = Tk.Button(self.frame_side_panel, text='Connect')
        #self.button_connect_db.pack(side='top', fill=Tk.BOTH)

class TopToolBar():
    def __init__(self, root):
        self.frame_top_tb = Tk.Frame(root, bg='#34383c') #Police : #6f7176

        self.img = Image.open("ressources/sign-out-alt.png").resize((32, 32))
        eimg = ImageTk.PhotoImage(self.img)

        label = Tk.Label(self.frame_top_tb, image=eimg, bg='#34383c')
        label.image = eimg
        label.pack(side=Tk.LEFT, padx=10, pady=11)

        self.frame_top_tb.pack(side=Tk.TOP, anchor=Tk.NW, fill=Tk.X)

class Logo():
    def __init__(self, root):
        self.frame_logo = Tk.Frame(root, bd=1, bg='#1d2226')

        self.img_logo = Image.open("ressources/logo.png").resize((32, 32))
        self.eimg_logo = ImageTk.PhotoImage(self.img_logo)

        #1d2226 for black logo <i class="fas fa-sign-out-alt"></i>
        label = Tk.Label(self.frame_logo, image=self.eimg_logo, bg='#1d2226')
        label.pack(side=Tk.LEFT, padx=10, pady=10)

        self.frame_logo.pack(side=Tk.TOP, anchor=Tk.NW)
