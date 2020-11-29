import tkinter as Tk

from models import mainmodel
from views import mainview


class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model = mainmodel.Model()
        self.view = mainview.View(self.root)
        self.view.sidepanel.label_quit.bind("<Button-1>", self.quit)
        self.view.sidepanel.label_quit.bind("<Enter>", self.mouse_enter_quit)
        self.view.sidepanel.label_quit.bind("<Leave>", self.mouse_leave_quit)

    def run(self):
        self.root.title("Cartes CPx")
        self.root.deiconify()
        self.root.mainloop()

    def quit(self, event):
        self.root.destroy()

    def mouse_enter_quit(self, event):
        self.view.sidepanel.label_quit.configure(image=self.view.sidepanel.eimg_quit_active, cursor='hand2')
        self.view.sidepanel.label_quit.image = self.view.sidepanel.eimg_quit_active

    def mouse_leave_quit(self, event):
        self.view.sidepanel.label_quit.configure(image=self.view.sidepanel.eimg_quit, cursor='arrow')
        self.view.sidepanel.label_quit.image = self.view.sidepanel.eimg_quit
