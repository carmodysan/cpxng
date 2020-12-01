import tkinter as Tk


class DownloadView():
    def __init__(self):
        print('Download view initialized')

    def load_content(self, main_frame):
        content = Tk.Label(main_frame, text="My super download !")
        content.pack(side=Tk.TOP, fill=Tk.BOTH, expand=Tk.YES)
        content2 = Tk.Label(main_frame, text="Fichier n°1")
        content2.pack(side=Tk.TOP, fill=Tk.BOTH, expand=Tk.YES)
