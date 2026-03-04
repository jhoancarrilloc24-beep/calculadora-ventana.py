class Usuario:
    
    def __init__(self, ID, nombre):
        self.ID = ID
        self.nombre = nombre   
        
    def get_ID(self):
        return self.ID
     
    def set_ID(self, nueva_ID):
        self.ID = nueva_ID
        
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
         
    def tomar_datos(self):
        print(f"ID: {self.get_ID()}")
        print(f"nombre: {self.get_nombre()}")