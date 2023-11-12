import customtkinter as ctk
from src.FPart import FramePart, FramePanPart
from PIL import Image
from src.functions import *

# Registro de Ocupación Actual de los paneles
class Ocupation:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.actual_row = 0
        self.actual_column = -1
        self.limit_column = 2
        self.limit_row = 7

    # Actualiza la posición del panel
    def update_position(self):
        if self.actual_column == self.limit_column:
            self.actual_column = 0
            self.actual_row += 1
        else:
            self.actual_column += 1

        return [self.actual_row, self.actual_column]

# Frames Paneles de Servicios
class FranePanel(ctk.CTkScrollableFrame):
    def __init__(self, master, name, img, type, description, date, place):
        super().__init__(master)

        self.configure(bg_color="#87400C")
        self.configure(fg_color="#FFE588")
        self.configure(width=320)
        self.configure(height=620)
        self.configure(corner_radius=10, border_width=0, border_color="#87400C")
        self.configure(scrollbar_button_color="#FFE588", scrollbar_button_hover_color = "#FFE588")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        #Atributos del panel
        self.name = name
        self.img = img
        self.type = type
        self.description = description
        self.date = date
        self.Place = place
        self.number = None #Número de panel que ocupa en la lista de páneles
        self.position = None #Posición del panel en la tabla de servicios (fila, columna)

        #Label Imagen
        self.img_type = ctk.CTkButton(self, image=self.img, text="", fg_color="transparent", bg_color="#FFE588", hover=None, height=324, width=280, corner_radius= 10)  # display image with a CTkLabel
        self.img_type.grid(row=0, column=0)
        
        #Lower Frame
        self.lower_frame = FramePart(self, 360, 326, "#FFE588", "#FFE588")
        self.lower_frame.grid(row=1, column=0)
        self.lower_frame.rowconfigure(5, weight=1)
        self.lower_frame.columnconfigure(0, weight=1)
        
        #Lower Frame B
        self.lower_frameB = FramePart(self, 360, 326, "#FFE588", "#FFE588")
        self.lower_frameB.rowconfigure(5, weight=1)
        self.lower_frameB.columnconfigure(0, weight=1)
        
        self.lnameB = ctk.CTkButton(self.lower_frameB, text=self.name, bg_color="#FFE588", fg_color="#FFCF44", hover=None, border_width=2, border_color= "#431A05",text_color="#431A05", font=("Georgia", 15), width=300, height=38, corner_radius=10)
        self.lnameB.grid(row=0, column=0)
        self.tbDesc = ctk.CTkTextbox(master=self.lower_frameB, width=321, height=160, corner_radius=18, border_width=5, border_color="#FFE588", bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18), scrollbar_button_hover_color="#87400C", scrollbar_button_color="#87400A")
        self.tbDesc.grid(row=1, column=0, columnspan=4, ipadx= 5)
        self.tbDesc.insert(0.0, self.description)
        self.tbDesc.configure(state="disabled")
        self.bseeMoreB = ctk.CTkButton(self.lower_frameB, text="Ver Menos", bg_color="#FFE588", fg_color="#EE9D04", hover_color="#87400C", border_width=2, border_color= "#87400C",text_color="#431A05", font=("Georgia", 16), width=294, height=70, corner_radius=10, command= lambda: self.see_more("main"))
        self.bseeMoreB.grid(row=5, column=0, pady= 20, rowspan=1)
        
        
        #Labels
        self.lname = ctk.CTkButton(self.lower_frame, text=self.name, bg_color="#FFE588", fg_color="#FFCF44", hover=None, border_width=2, border_color= "#431A05",text_color="#431A05", font=("Georgia", 15), width=300, height=38, corner_radius=10)
        self.lname.grid(row=0, column=0)
        self.ltype = ctk.CTkButton(self.lower_frame, text=f"Tipo: {self.type}", bg_color="#FFE588", fg_color="transparent", hover=None,text_color="#431A05", font=("Georgia", 14), height=54)
        self.ltype.grid(row=1, column=0)
        self.ldate = ctk.CTkButton(self.lower_frame, text=f"Fecha: {self.date}", bg_color="#FFE588", fg_color="transparent", hover=None,text_color="#431A05", font=("Georgia", 14), height=54)
        self.ldate.grid(row=2, column=0)
        self.lplace = ctk.CTkButton(self.lower_frame, text=f"Lugar: {self.Place}", bg_color="#FFE588", fg_color="transparent", hover=None,text_color="#431A05", font=("Georgia", 14), height=54)
        self.lplace.grid(row=3, column=0)
        
        #Button
        self.bseeMore = ctk.CTkButton(self.lower_frame, text="Ver Más", bg_color="#FFE588", fg_color="#EE9D04", hover_color="#87400C", border_width=2, border_color= "#431A05",text_color="#431A05", font=("Georgia", 16), width=294, height=70, corner_radius=10, command= lambda: self.see_more("back"))
        self.bseeMore.grid(row=5, column=0, pady= 20)
        


    # Asigna el número de panel y su posición en la tabla de servicios
    def set_number(self, number, position):
        self.number = number
        self.position = position
    
    def see_more(self, side):
        if side == "main":
            self.lower_frameB.grid_forget()
            self.lower_frame.grid(row=1, column=0)
        elif side == "back":
            self.lower_frame.grid_forget()
            self.lower_frameB.grid(row=1, column=0)
    
    def update_info(self): 
        self.lname.configure(text=self.name)
        self.ldate.configure(text=f"Fecha: {self.date}")
        self.lplace.configure(text=f"Lugar: {self.Place}")
        self.tbDesc.configure(state="normal")
        self.tbDesc.delete(0.0, "end")
        self.tbDesc.insert(0.0, self.description)
        self.tbDesc.configure(state="disabled")
    

# Frame Tabla de Servicios
class FrameTable(ctk.CTkScrollableFrame):
    def __init__(self, master, width, height, background_color, foreground_color):
        super().__init__(master)

        # Atributos de la tabla
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        self.configure(width=width)
        self.configure(height=height)
        self.configure(scrollbar_button_color="#CD7601", scrollbar_button_hover_color = "#EE9D04")
        self.table_occupation = Ocupation()
        self.panels = []
        self.frame2= None



    def create_panel(self, name, img, type, description, date, place):
        
        if type == "Cultural":
            img = ctk.CTkImage(light_image=Image.open("assets/danza.png"), size=(220, 220))
        elif type == "Abastecimiento":
            img = ctk.CTkImage(light_image=Image.open("assets/manzana.png"), size=(220, 220))
        elif type == "Regulación":
            img = ctk.CTkImage(light_image=Image.open("assets/arbolito.png"), size=(220, 220))

        self.panel = FranePanel(self, filter(name), img, filter(type), filter(description), filter(date), filter(place))
        self.panels.append(self.panel)
        self.list_position = self.table_occupation.update_position()
        
        self.panel.grid(row=self.list_position[0], column=self.list_position[1], sticky="nsew", padx=10, pady=10)
        self.panel.set_number(len(self.panels), self.list_position)
        self.frame2.comboEliminar.configure(values= [panel.name for panel in self.panels])
        self.frame2.comboEditar.configure(values= [panel.name for panel in self.panels])
        self.frame2.panels = self.panels
        

    def return_panel(self, number):
        return self.panels[number]
    
    def remove_panel(self, panel):
        panel.grid_forget()
        self.panels.remove(panel)
        
    #!Ya se elimina, falta ubicar bien los índices después de la eliminación: Hacer condicional para no meter dos iguales
    def update_panels(self): 
        for panel in self.panels:
            panel.grid_forget()
            
        self.table_occupation = Ocupation()
        for panel in self.panels:
            self.list_position = self.table_occupation.update_position()
            panel.grid(row=self.list_position[0], column=self.list_position[1], sticky="nsew", padx=10, pady=10)
            panel.set_number(self.panels.index(panel) + 1, self.list_position)
    
    def update_bind(self): 
        self.frame2.panels = self.panels
            
    
    