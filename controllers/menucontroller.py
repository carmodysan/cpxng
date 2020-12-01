class MenuController():
    def __init__(self, view, root, model):
        self.view = view
        self.root = root
        self.model = model

        # Quit module
        self.view.sidepanel.label_quit.bind("<Button-1>", self.quit)
        self.view.sidepanel.label_quit.bind("<Enter>", self.mouse_enter_quit)
        self.view.sidepanel.label_quit.bind("<Leave>", self.mouse_leave_quit)

        # About module
        self.view.sidepanel.label_about.bind("<Button-1>", self.about)
        self.view.sidepanel.label_about.bind("<Enter>", self.mouse_enter_about)
        self.view.sidepanel.label_about.bind("<Leave>", self.mouse_leave_about)

        # Download module
        self.view.sidepanel.label_dl.bind("<Button-1>", self.dl)
        self.view.sidepanel.label_dl.bind("<Enter>", self.mouse_enter_dl)
        self.view.sidepanel.label_dl.bind("<Leave>", self.mouse_leave_dl)

    # Quit module controller
    def quit(self, event):
        self.root.destroy()

    def mouse_enter_quit(self, event):
        self.view.sidepanel.label_quit.configure(image=self.view.sidepanel.image_quit_active, cursor='hand2')
        self.view.sidepanel.label_quit.image = self.view.sidepanel.image_quit_active

    def mouse_leave_quit(self, event):
        self.view.sidepanel.label_quit.configure(image=self.view.sidepanel.image_quit, cursor='arrow')
        self.view.sidepanel.label_quit.image = self.view.sidepanel.image_quit

    # About module controller
    def about(self, event):
        self.view.display_about(self.root)

    def mouse_enter_about(self, event):
        self.view.sidepanel.label_about.configure(image=self.view.sidepanel.image_about_active, cursor='hand2')
        self.view.sidepanel.label_about.image = self.view.sidepanel.image_about_active

    def mouse_leave_about(self, event):
        self.view.sidepanel.label_about.configure(image=self.view.sidepanel.image_about, cursor='arrow')
        self.view.sidepanel.label_about.image = self.view.sidepanel.image_about

    # Download module controller
    def dl(self, event):
        self.model.select_test()
        self.view.display_download(self.root)

    def mouse_enter_dl(self, event):
        self.view.sidepanel.label_dl.configure(image=self.view.sidepanel.image_dl_active, cursor='hand2')
        self.view.sidepanel.label_dl.image = self.view.sidepanel.image_dl_active

    def mouse_leave_dl(self, event):
        self.view.sidepanel.label_dl.configure(image=self.view.sidepanel.image_dl, cursor='arrow')
        self.view.sidepanel.label_dl.image = self.view.sidepanel.image_dl
