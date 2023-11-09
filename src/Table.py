import customtkinter as ctk

class Ocupation: 
    def __init__(self): 
        self.rows = 0
        self.columns = 0
        self.actual_row = 0
        self.actual_column = 0
        self.limit_column = 3
        self.limit_row = 7
    
    def update_position(self):
        if self.actual_column == self.limit_column:
            self.actual_column = 0
            self.actual_row += 1
        else:
            self.actual_column += 1
        
        return [self.actual_row, self.actual_column]

class FranePanel(ctk.CTkFrame):
    def __init__(self, master, type, description, date, place, hour):
        super().__init__(master)
        
        self.configure(bg_color="#87400C")
        self.configure(fg_color="#FFE588")
        self.configure(width=360)
        self.configure(height=650)
        self.configure(corner_radius=20, border_width=5, border_color="#87400C")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.type = type
        self.description = description
        self.date = date
        self.place = place
        self.hour = hour
        
        
        

class FrameTable(ctk.CTkScrollableFrame):
    def __init__(self, master, width, height, background_color, foreground_color):
        super().__init__(master)

        # add widgets onto the frame...
        self.configure(bg_color=background_color)
        self.configure(fg_color=foreground_color)
        self.configure(width=width)
        self.configure(height=height)
        self.configure(scrollbar_button_color="#CD7601", scrollbar_button_hover_color = "#EE9D04")
        self.table_occupation = Ocupation()
        self.buttonjopo = ctk.CTkButton(self, text="Jopo", bg_color="#fff0af", fg_color="#3c5f49", hover_color="#2C4436", text_color="#fff0af", font=("Verdana", 16), width=153, height=43, corner_radius=10, command=lambda: self.create_panel("Jopo", "Jopo", "Jopo", "Jopo", "Jopo"))
        self.buttonjopo.grid(row=0, column=0, sticky="nsew")
        
        
    def create_panel(self, type, description, date, place, hour):
        self.panel = FranePanel(self, type, description, date, place, hour)
        self.list_position = self.table_occupation.update_position()
        self.panel.grid(row=self.list_position[0], column=self.list_position[1], sticky="nsew")
        

