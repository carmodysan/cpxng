import tkinter as Tk
from utils import log


class StatsView():
    def __init__(self):
        self.logger = log.Logger.Instance()

    def load_content(self, main_frame):
        content = Tk.Label(main_frame, text="My super stats !")
        content.pack(side=Tk.TOP, fill=Tk.BOTH, expand=Tk.YES)
        content = Tk.Label(main_frame, text="Nombre de cartes : 10000")
        content.pack(side=Tk.TOP, fill=Tk.BOTH, expand=Tk.YES)
        self.logger.appdebug('Stats view content loaded')
