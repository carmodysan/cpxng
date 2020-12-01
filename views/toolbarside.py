import tkinter as Tk
from PIL import Image, ImageTk


class SideToolBar():
    def __init__(self, root):
        self.frame_side_panel = Tk.Frame(root, bd=1, bg='#91c46b')

        # Quit module
        self.image_quit = self.create_photoimage('ressources/sign-out-alt.png')
        self.image_quit_active = self.create_photoimage('ressources/sign-out-alt-active.png')

        self.label_quit = Tk.Label(self.frame_side_panel, image=self.image_quit, bg='#91c46b')
        self.label_quit.image = self.image_quit
        self.label_quit.pack(side=Tk.TOP, padx=10, pady=10)

        # About Module
        self.image_about = self.create_photoimage('ressources/about.png')
        self.image_about_active = self.create_photoimage('ressources/about-active.png')

        self.label_about = Tk.Label(self.frame_side_panel, image=self.image_about, bg='#91c46b')
        self.label_about.image = self.image_quit
        self.label_about.pack(side=Tk.TOP, padx=10, pady=10)

        # Download Module
        self.image_dl = self.create_photoimage('ressources/file-download.png')
        self.image_dl_active = self.create_photoimage('ressources/file-download-active.png')

        self.label_dl = Tk.Label(self.frame_side_panel, image=self.image_dl, bg='#91c46b')
        self.label_dl.image = self.image_dl
        self.label_dl.pack(side=Tk.TOP, padx=10, pady=10)

        self.frame_side_panel.pack(side=Tk.TOP, fill=Tk.Y, expand=Tk.YES)

    # Create et return PhotoImage object of the image path passed in arguments
    def create_photoimage(self, image):
        img = Image.open(image).resize((32, 32))
        return ImageTk.PhotoImage(img)
