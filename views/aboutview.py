import tkinter as Tk


class AboutView():
    def __init__(self):
        print('About view initialized')

    def load_content(self, main_frame):
        content = Tk.Label(main_frame, text="Cartes CPx NG")
        content.pack(side=Tk.TOP, fill=Tk.BOTH, expand=Tk.YES)
        content2 = Tk.Label(main_frame, text="Logiciel de suivi des cartes CPx")
        content2.pack(side=Tk.TOP, fill=Tk.BOTH, expand=Tk.YES)
        content2 = Tk.Label(main_frame, text="Version : 0.1.a")
        content2.pack(side=Tk.TOP, fill=Tk.BOTH, expand=Tk.YES)
