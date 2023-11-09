from typing import Optional, Tuple, Union
import customtkinter as ctk

class SuperficialFrame(ctk.CTkFrame): 
    def __init__(self, master):
        super().__init__(master)
        self.configure(width= 830, height= 665)
        self.configure(bg_color="#87400C")
        
        