class Vuelo:
    def __init__(self, origen, destino, fecha, avion):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.avion = avion
    
    def get_pais_origen(self):
        return self.origen
    
    def get_pais_destino(self):
        return self.destino
    
    def get_fecha(self):
        return self.fecha
    
    def get_avion(self):
        return self.avion
    
    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha})"