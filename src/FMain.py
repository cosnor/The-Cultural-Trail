import customtkinter as ctk
from src.FPart import FramePart
from src.Table import FrameTable
from src.FAdd import SuperficialFrame
from PIL import Image
from src.functions import *

class FrameMain(ctk.CTkFrame):
    def __init__(self, master, background_color, foreground_color):
        super().__init__(master)
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        #Definición del frame
        
        #MainPartBack
        self.mainPartBack = FramePart(self, 1260, 800, "#431A05", "transparent")
        self.mainPartBack.grid(row=0, column=1, sticky="nsew")
        self.mainPartBack.rowconfigure(0, weight=1)
        self.mainPartBack.columnconfigure(0, weight=1)
        
        #MainPart
        self.mainPart = FrameTable(self.mainPartBack, 1108, 665, "#431A05", "#87400C")
        self.mainPart.rowconfigure(6, weight=1)
        self.mainPart.columnconfigure(5, weight=1)
        self.mainPart.configure(corner_radius=20, border_width=5, border_color="#87400C")
        self.mainPart.grid(row=0, column=0)
        
        
        #Back2
        self.back2 = FramePart(self, 1260, 800, "#431A05", "transparent")
        
        #NavBar
        self.navBar = FramePart(self, 280, 800, "#EE9D04", "transparent")
        self.navBar.grid(row=0, column=0, sticky="nsew")
        self.navBar.rowconfigure(2, weight=1)
        self.navBar.columnconfigure(0, weight=1)
        
        #NavBarLogo
        self.navBarLogo = FrameLogo(self.navBar, "#EE9D04", "transparent")
        self.navBarLogo.grid(row=0, column=0, sticky="nsew")
        
        #First Section Buttons
        self.firstSectionButtons = FramePart(self.navBar, 280, 100, "#EE9D04", "transparent")
        self.firstSectionButtons.grid(row=1, column=0, sticky="nsew")
        self.firstSectionButtons.rowconfigure(2, weight=1)
        self.firstSectionButtons.columnconfigure(0, weight=1)
        
        #Title
        self.titleButton= ButtonNavBar(self.firstSectionButtons, "The Cultural Trail", "#CD7601", "#CD7601", "#CD7601", None, ("Georgia", 22, "bold"))
        self.titleButton.grid(row=0, column=0, sticky="nsew")
        self.titleButton.configure(text_color="#FEFAE8")
        
        #Buttons
        self.button1 = ButtonNavBar(self.firstSectionButtons, "Tablero de Servicios", "#FEB611", "#FEB611", "#FFCF44", command= lambda: self.select_frame("tablero"))
        self.button1.grid(row=1, column=0, sticky="nsew")
        self.button2 = ButtonNavBar(self.firstSectionButtons, "Agregar Servicio", "#EE9D04", "#EE9D04", "#CD7601", command= lambda: self.select_frame("agregar"))
        self.button2.grid(row=2, column=0, sticky="nsew")
        self.button3 = ButtonNavBar(self.firstSectionButtons, "Editar Servicios", "#FEB611", "#FEB611", "#FFCF44", None)
        self.button3.grid(row=3, column=0, sticky="nsew")
        
        
    def select_frame(self, frame_name): 
        if frame_name == "tablero":
            self.back2.grid_forget()
            self.mainPartBack.grid(row=0, column=1, sticky="nsew")
        elif frame_name == "agregar":
            self.mainPartBack.grid_forget()
            self.back2.grid(row=0, column=1, sticky="nsew")
            
            
        else: 
            self.mainPartBack.grid(row=0, column=1, sticky="nsew")
            
class FrameLogo(ctk.CTkFrame):
    def __init__(self, master, background_color, foreground_color):
        super().__init__(master)
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        #Imagen
        self.logo = ctk.CTkImage(light_image=Image.open("assets/logo.png"),dark_image=Image.open("assets/logo.png"), size=(300, 300))
        #Label Imagen
        self.logo_button = ctk.CTkButton(self, image=self.logo, text="", fg_color="transparent", bg_color="#CD7601", hover=None)  # display image with a CTkLabel
        self.logo_button.grid(row=0, column=0, sticky="nsew")
        

class ButtonNavBar(ctk.CTkButton):
    def __init__(self, master, text, background_color, foreground_color, hover_color, command, font=("Helvetica", 16, "bold")):
        super().__init__(master)
        self.configure(text=text)
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        self.configure(hover_color=hover_color)
        self.configure(text_color="#431A05")
        self.configure(font=font)
        self.configure(width=280)
        self.configure(height=66)
        self.configure(corner_radius=0)
        self.configure(command=command)
        
        
