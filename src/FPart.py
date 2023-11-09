import customtkinter as ctk

class FramePart(ctk.CTkFrame):
    def __init__(self, master, width, height, background_color, foreground_color):
        super().__init__(master)
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        self.configure(width=width)
        self.configure(height=height)