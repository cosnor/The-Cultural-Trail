import customtkinter as ctk
from src.functions import filter

class SuperficialEFrame(ctk.CTkScrollableFrame): 
    def __init__(self, master, brother_frame):
        super().__init__(master)
        self.configure(width= 830, height= 665)
        self.configure(bg_color="#431A05", fg_color="#FFE588", corner_radius=20, border_width=0, border_color="#FFE588")
        self.configure(scrollbar_button_color="#FFE588", scrollbar_button_hover_color = "#FFE588")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(6, weight=1)
        self.frame_to_bind = brother_frame
        self.panels = []
        
            
        #labels
        self.fix = ctk.CTkLabel(self, text="", bg_color="#FFE588", fg_color="#FFE588", width= 117, height= 1)
        self.fix.grid(row=1, column=0, columnspan=1)
        self.labelTitulo = ctk.CTkLabel(self, text="EDITA EL TABLERO", fg_color="#FFE588", bg_color="#FFE588", text_color="#2C4436", font=("Georgia", 32, "bold"), width=644, height=95)
        self.labelTitulo.grid(row=0, column=0, columnspan=7, pady= 20 )
        self.labelEliminar = ctk.CTkLabel(self, text="Eliminar Actividad", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelEliminar.grid(row=1, column=1, columnspan=2)
        self.labelEditar = ctk.CTkLabel(self, text="Editar Actividad", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelEditar.grid(row=3, column=1, columnspan=2)
        self.labelSeccion = ctk.CTkLabel(self, text="Editar Sección", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelSeccion.grid(row=4, column=1, columnspan=2)
        self.labelNuevo = ctk.CTkLabel(self, text="Nuevo Texto", fg_color="#FFE588", bg_color="#FFE588", text_color="#431A05", font=("Georgia", 20), width=236, height=95)
        self.labelNuevo.grid(row=5, column=1, columnspan=2)
        
        #Combo Boxes
        self.comboEliminar = ctk.CTkComboBox(self, width=321, height=49, border_width=5, corner_radius=18, border_color= "#FFCF44" ,bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18), values= [panel.name for panel in self.panels], button_color="#EE9D04", button_hover_color="#CD7601", dropdown_fg_color="#87400C", dropdown_text_color="#FFCF44", dropdown_font=("Georgia", 16), state="readonly", dropdown_hover_color="#2C4436", command= None)
        self.comboEliminar.set("Selecciona una actividad")
        self.comboEliminar.grid(row=1, column=3, columnspan=3, ipadx= 5, pady = 10 )
        self.comboEditar = ctk.CTkComboBox(self, width=321, height=49, border_width=5, corner_radius=18, border_color= "#FFCF44" ,bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18), values= [panel.name for panel in self.panels], button_color="#EE9D04", button_hover_color="#CD7601", dropdown_fg_color="#87400C", dropdown_text_color="#FFCF44", dropdown_font=("Georgia", 16), state="readonly", dropdown_hover_color="#2C4436", command=None)
        self.comboEditar.set("Selecciona una actividad")
        self.comboEditar.grid(row=3, column=3, columnspan=3, ipadx= 5 , pady = 10 )
        self.comboSeccion = ctk.CTkComboBox(self, width=321, height=49, border_width=5, corner_radius=18, border_color= "#FFCF44" ,bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18), values=["Nombre", "Tipo", "Fecha", "Lugar", "Descripción"], button_color="#EE9D04", button_hover_color="#CD7601", dropdown_fg_color="#87400C", dropdown_text_color="#FFCF44", dropdown_font=("Georgia", 16), state="readonly", dropdown_hover_color="#2C4436", command= None)
        self.comboSeccion.set("Selecciona una sección")
        self.comboSeccion.grid(row=4, column=3, columnspan=3, ipadx= 5, pady = 10 )
        
        
        #Text Fields
        self.tbNuevo = ctk.CTkTextbox(master=self, width=321, height=49, corner_radius=18, border_width=5, border_color="#FFE588", bg_color="#FFE588", fg_color="#FFCF44", text_color="#87400C", font=("Georgia", 18))
        self.tbNuevo.grid(row=5, column=3, columnspan=3, ipadx= 5)
        
        #Buttons
        self.bEliminar = ctk.CTkButton(self, text="Eliminar", bg_color="#FFE588", fg_color="#EE9D04", hover_color="#87400C", border_width=2, border_color= "#87400C",text_color="#431A05", font=("Georgia", 16), width=294, height=50, corner_radius=10, command = self.eliminar)
        self.bEliminar.grid(row=2, column=0, columnspan=7)
        self.bEditar = ctk.CTkButton(self, text="Editar", bg_color="#FFE588", fg_color="#EE9D04", hover_color="#87400C", border_width=2, border_color= "#87400C",text_color="#431A05", font=("Georgia", 16), width=294, height=50, corner_radius=10, command = self.modificar)
        self.bEditar.grid(row=6, column=0, columnspan=7, pady= 20)
        
    def eliminar(self):
        name = self.comboEliminar.get()
        print(f"hp: {name}")
        print(self.panels)
        for panel in self.panels:
            print(panel.name)
            if panel.name == name:
                self.panels.remove(panel)
                self.frame_to_bind.remove_panel(panel)
                print("Eliminado")
                self.comboEliminar.configure(values=[panel.name for panel in self.panels])
                self.comboEditar.configure(values=[panel.name for panel in self.panels])
            else:
                self.comboEliminar.set("No existe el panel")
                                
        self.comboEliminar.set("Selecciona una actividad")
        
    def modificar(self): 
        
        npanel = self.traductor (self.comboEditar.get())
        panel = self.frame_to_bind.return_panel(npanel)
        parametro = self.comboSeccion.get()
        texto = filter(self.tbNuevo.get(0.0, "end"))
        
        if parametro == "Nombre":
            panel.name = texto
        elif parametro == "Fecha":
            panel.date = texto
        elif parametro == "Lugar":
            panel.Place = texto
        elif parametro == "Descripción":
            panel.description = texto
        
        panel.update_info()
        self.frame_to_bind.update_bind()
        self.comboEditar.configure(values=[panel.name for panel in self.panels])
        self.comboEditar.set("Selecciona una actividad")
        self.tbNuevo.delete(0.0, "end")
        self.comboEliminar.configure(values=[panel.name for panel in self.panels])

            
    def traductor(self, panel_name): 
        values = self.comboEditar.cget("values")
        for index, value in enumerate(values): 
            if value == panel_name:
                return index