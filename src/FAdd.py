from typing import Optional, Tuple, Union
import customtkinter as ctk
from PIL import Image
from src.functions import *

class SuperficialFrame(ctk.CTkScrollableFrame): 
    def __init__(self, master, brother_frame):
        super().__init__(master)
        self.configure(width= 830, height= 665)
        self.configure(bg_color="#431A05", fg_color="#FFE588", corner_radius=20, border_width=0, border_color="#FFE588")
        self.configure(scrollbar_button_color="#FFE588", scrollbar_button_hover_color = "#FFE588")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(6, weight=1)
        self.frame_to_bind = brother_frame
        
        #labels
        self.labelTitulo = ctk.CTkLabel(self, text="AGREGA TU ACTIVIDAD AL TABLERO", fg_color="#FFE588", bg_color="#FFE588", text_color="#2C4436", font=("Georgia", 32, "bold"), width=644, height=36)
        self.labelTitulo.grid(row=0, column=0, columnspan=7, pady= 20 )
        self.labelNombre = ctk.CTkLabel(self, text="Nombre Actividad", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelNombre.grid(row=1, column=1, columnspan=2)
        self.labelNombre = ctk.CTkLabel(self, text="Tipo de Servicio", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelNombre.grid(row=2, column=1, columnspan=2)
        self.labelFecha = ctk.CTkLabel(self, text="Fecha y Hora", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelFecha.grid(row=3, column=1, columnspan=2)
        self.labelLugar = ctk.CTkLabel(self, text="Lugar", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelLugar.grid(row=4, column=1, columnspan=2)
        self.labelDesc = ctk.CTkLabel(self, text="Descripción", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelDesc.grid(row=5, column=1, columnspan=2)
        
        #Space Fix
        self.fix = ctk.CTkLabel(self, text= "", fg_color="#FFE588", bg_color="#FFE588", font=("Georgia", 20), width=117, height=95)
        self.fix.grid(row=1, column=0, columnspan=1)
        
        #Text Fields
        self.tbNombre = ctk.CTkTextbox(master=self, width=321, height=49, corner_radius=18, border_width=5, border_color="#FFE588", bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18))
        self.tbNombre.grid(row=1, column=3, columnspan=3, ipadx= 5)
        self.tbFecha = ctk.CTkTextbox(master=self, width=321, height=49, corner_radius=18, border_width=5, border_color="#FFE588", bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18))
        self.tbFecha.grid(row=3, column=3, columnspan=3, ipadx= 5)
        self.tbLugar = ctk.CTkTextbox(master=self, width=321, height=49, corner_radius=18, border_width=5, border_color="#FFE588", bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18))
        self.tbLugar.grid(row=4, column=3, columnspan=3, ipadx= 5)
        self.tbDesc = ctk.CTkTextbox(master=self, width=321, height=135, corner_radius=18, border_width=5, border_color="#FFE588", bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18), scrollbar_button_hover_color="#87400C", scrollbar_button_color="#87400A")
        self.tbDesc.grid(row=5, column=3, columnspan=3, ipadx= 5)
        
        #ImageViewer
        
        #Imágenes
        self.img_cultural = ctk.CTkImage(light_image=Image.open("assets/danza.png"), size=(80, 80))
        self.img_abastecimiento = ctk.CTkImage(light_image=Image.open("assets/manzana.png"), size=(80, 80))
        self.img_regulacion = ctk.CTkImage(light_image=Image.open("assets/arbolito.png"), size=(80, 80))
        
        self.img_actual = self.img_cultural
        
        #Label Imagen
        self.img__button = ctk.CTkButton(self, image=self.img_actual, text="", fg_color="transparent", bg_color="#FFE588", hover=None)  # display image with a CTkLabel
        self.img__button.grid(row=2, column=5)
        
        #Combo Box
        self.cbTipo = ctk.CTkComboBox(self, width=212, height=49, border_width=5, corner_radius=18, border_color= "#FFCF44" ,bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18), values=["Cultural", "Abastecimiento", "Regulación"], button_color="#EE9D04", button_hover_color="#CD7601", dropdown_fg_color="#87400C", dropdown_text_color="#FFCF44", dropdown_font=("Georgia", 16), state="readonly", dropdown_hover_color="#2C4436", command=self.combo_event)
        self.cbTipo.set("Cultural")
        self.cbTipo.grid(row=2, column=3, columnspan=2, ipadx= 5)
        
        #Buttons
        self.buttonAgregar = ctk.CTkButton(self, text="Agregar Servicio", bg_color="#FFE588", fg_color="#FFCF44", hover_color="#EE9D04", border_width=2, border_color= "#431A05",text_color="#431A05", font=("Georgia", 16), width=294, height=38, corner_radius=10, command= self.get_data)
        self.buttonAgregar.grid(row=6, column=2, columnspan=3, pady= 20)
        
    
    def combo_event(self, value):
        self.change_type(value)
        
    def change_type(self, type: str):
        if type == "Cultural":
            self.img_actual = self.img_cultural
            self.img__button.configure(image=self.img_actual)
        elif type == "Abastecimiento":
            self.img_actual = self.img_abastecimiento
            self.img__button.configure(image=self.img_actual)
        elif type == "Regulación":
            self.img_actual = self.img_regulacion
            self.img__button.configure(image=self.img_actual)
    
    def get_data(self):
        data = [self.tbNombre.get(0.0, "end"), self.img_actual, self.cbTipo.get(),  self.tbDesc.get(0.0, "end"), self.tbFecha.get(0.0, "end"), self.tbLugar.get(0.0, "end")]
        
        if (is_in_panel(filter(data[0]), self.frame_to_bind.panels)):
            print("Ya existe")
        else:
            self.tbNombre.delete(0.0, "end")
            self.tbDesc.delete(0.0, "end")
            self.tbFecha.delete(0.0, "end")
            self.tbLugar.delete(0.0, "end")
            self.send_data_to_panel(data)
        
    def send_data_to_panel(self, data):
        self.frame_to_bind.create_panel(*data)    