import customtkinter as ctk

class FramePart(ctk.CTkFrame):
    def __init__(self, master, width, height, background_color, foreground_color):
        super().__init__(master)
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        self.configure(width=width)
        self.configure(height=height)
        
class FramePanPart(ctk.CTkScrollableFrame): 
    def __init__(self, master, width, height, background_color, foreground_color):
        super().__init__(master)
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        self.configure(width=width)
        self.configure(height=height)
        self.configure(corner_radius=10, border_width=0, border_color="#87400C", scrollbar_button_color="#FFE588", scrollbar_button_hover_color = "#FFE588")