from typing import Optional, Tuple, Union
import customtkinter as ctk
from PIL import Image


class FrameInicial(ctk.CTkFrame):
    def __init__(self, master, background_color, foreground_color):
        super().__init__(master)
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        
        #Imágenes
        self.fondo = ctk.CTkImage(light_image=Image.open("assets/fondo.png"), size=(1540, 800))
        self.logo = ctk.CTkImage(light_image=Image.open("assets/logo.png"),dark_image=Image.open("assets/logo.png"), size=(300, 300))
        
        #Label Imágenes
        self.image_fondo = ctk.CTkLabel(self, image=self.fondo, text="")  # display image with a CTkLabel
        self.image_fondo.pack(fill="both", expand=True)
        self.logo_button = ctk.CTkButton(self, image=self.logo, text="", fg_color="transparent", bg_color="#fff0af", hover=None)  # display image with a CTkLabel
        self.logo_button.place(x=620, y=150)
        
        #Botones
        self.boton_entrar = ctk.CTkButton(self, text="Adentrarse", bg_color="#fff0af", fg_color="#3c5f49", hover_color="#2C4436", text_color="#fff0af", font=("Verdana", 16), width=153, height=43, corner_radius=10, command=lambda: self.master.select_frame_by_name("main"))
        self.boton_entrar.place(x=700, y=535)
        
        #Label Texto
        self.texto = ctk.CTkLabel(self, text="The Cultural Trail", bg_color="#fff0af", fg_color="transparent", text_color="#2C4436", font=("Georgia", 32, "bold"))
        self.texto.place(x=630, y=450)
        
class FrameMain(ctk.CTkFrame):
    def __init__(self, master, background_color, foreground_color):
        super().__init__(master)
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
    
        #Definición del frame
        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.x = self.winfo_screenwidth() // 2 - 1540 // 2
        self.y = self.winfo_screenheight() // 2 - 800 // 2
        self.posicionamiento = f"1540x800+{self.x - 10}+{self.y -35}"
        
        self.geometry(self.posicionamiento)
        self.resizable(False, False)        
        self.title("The Cultural Trail")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.frame_inicial = FrameInicial(self, "#fff0af", "transparent")
        self.frame_inicial.grid(row=0, column=0, sticky="nsew")
        
        self.frame_main = FrameMain(self, "#fff0af", "transparent")
    
    def select_frame_by_name(self, frame_name):
        
        if frame_name == "inicial":
            self.frame_inicial.grid(row=0, column=0, sticky="nsew")
        else: 
            self.frame_inicial.grid_forget()
        
        
app = App()
app.mainloop()