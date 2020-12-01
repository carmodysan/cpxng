from PIL import Image, ImageTk
import tkinter as Tk
from sys import platform

from views import statusbar, toolbarside, toolbartop
from views import aboutview, statsview, downloadview


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
        self.statusbar = statusbar.StatusBar(master)
        self.statusbar.observe('update_connect_db', self.statusbar.update_connect_db)

        # The left frame contains logo and possible actions
        self.left_frame = Tk.Frame(master)
        self.logo = Logo(self.left_frame)
        self.sidepanel = toolbarside.SideToolBar(self.left_frame)
        self.left_frame.pack(side=Tk.LEFT, fill=Tk.Y, anchor=Tk.NW)

        # The top frame contains the toolbar
        self.top_toolbar = toolbartop.TopToolBar(master)

        self.stats_view = statsview.StatsView()
        self.about_view = aboutview.AboutView()
        self.download_view = downloadview.DownloadView()

        self.main_frame = None
        self.display_stats(master)

    def display_stats(self, master):
        if self.main_frame is not None:
            self.main_frame.destroy()
            print('destroy previous frame')

        # The main frame contains the content
        self.main_frame = Tk.Frame(master)
        self.stats_view.load_content(self.main_frame)
        self.main_frame.pack(side=Tk.TOP, fill=Tk.BOTH, anchor=Tk.CENTER)

    def display_about(self, root):
        if self.main_frame is not None:
            self.main_frame.destroy()
            print('destroy previous frame')

        self.main_frame = Tk.Frame(root)
        self.about_view.load_content(self.main_frame)
        self.main_frame.pack(side=Tk.TOP, fill=Tk.BOTH, anchor=Tk.CENTER)

    def display_download(self, master):
        # The main frame contains the content
        if self.main_frame is not None:
            self.main_frame.destroy()
            print('destroy previous frame')

        self.main_frame = Tk.Frame(master)
        self.download_view.load_content(self.main_frame)
        self.main_frame.pack(side=Tk.TOP, fill=Tk.BOTH, anchor=Tk.CENTER)


class Logo():
    def __init__(self, root):
        self.frame_logo = Tk.Frame(root, bd=1, bg='#1d2226')

        self.img_logo = Image.open("ressources/logo.png").resize((32, 32))
        self.eimg_logo = ImageTk.PhotoImage(self.img_logo)

        #1d2226 for black logo <i class="fas fa-sign-out-alt"></i>
        label = Tk.Label(self.frame_logo, image=self.eimg_logo, bg='#1d2226')
        label.pack(side=Tk.LEFT, padx=10, pady=10)

        self.frame_logo.pack(side=Tk.TOP, anchor=Tk.NW)
