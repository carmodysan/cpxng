from PIL import Image, ImageTk
import tkinter as Tk


class TopToolBar():
    def __init__(self, root):
        self.frame_top_tb = Tk.Frame(root, bg='#34383c')  # Police : #6f7176

        self.img = Image.open("ressources/sign-out-alt.png").resize((32, 32))
        eimg = ImageTk.PhotoImage(self.img)

        label = Tk.Label(self.frame_top_tb, image=eimg, bg='#34383c')
        label.image = eimg
        label.pack(side=Tk.LEFT, padx=10, pady=11)

        self.frame_top_tb.pack(side=Tk.TOP, anchor=Tk.NW, fill=Tk.X)
