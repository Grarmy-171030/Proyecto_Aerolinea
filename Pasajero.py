class Pasajero:
    def __init__(self, nombre, pasaporte, telefono, edad, maleta):
        self.nombre = nombre
        self.pasaporte = pasaporte
        self.telefono = telefono
        self.edad = edad
        self.maleta = maleta
    
    def get_nombre(self):
        return self.nombre
    
    def get_pasaporte(self):
        return self.pasaporte
    
    def get_telefono(self):
        return self.telefono
    
    def get_edad(self):
        return self.edad
    
    def get_maleta(self):
        return self.maleta