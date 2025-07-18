from Clase import Clase
from Asiento import Asiento

class Avion:
    ASIENTOS_POR_FILA = 4
    
    def __init__(self, modelo, num_business, num_turista):
        self.modelo = modelo
        self.asientos_business = self._crear_asientos(num_business, Clase.BUSINESS)
        self.asientos_turista = self._crear_asientos(num_turista, Clase.TURISTA)
    
    def _crear_asientos(self, cantidad, clase):
        filas = cantidad // self.ASIENTOS_POR_FILA
        return [[None for _ in range(self.ASIENTOS_POR_FILA)] for _ in range(filas)]
    
    def reservar_asiento(self, fila, butaca, clase, pasajero):
        if clase == Clase.BUSINESS:
            matriz = self.asientos_business
        else:
            matriz = self.asientos_turista
        
        if 1 <= fila <= len(matriz) and 1 <= butaca <= self.ASIENTOS_POR_FILA:
            if matriz[fila-1][butaca-1] is None:
                asiento = Asiento(fila, butaca, pasajero)
                matriz[fila-1][butaca-1] = asiento
                return asiento
        return None
    
    def get_pasajero(self, fila, butaca, clase):
        if clase == Clase.BUSINESS:
            matriz = self.asientos_business
        else:
            matriz = self.asientos_turista
        
        if 1 <= fila <= len(matriz) and 1 <= butaca <= self.ASIENTOS_POR_FILA:
            asiento = matriz[fila-1][butaca-1]
            return asiento.get_pasajero() if asiento else None
        return None
    
    def get_numero_filas(self, clase):
        return len(self.asientos_business) if clase == Clase.BUSINESS else len(self.asientos_turista)
    
    def get_butacas_por_fila(self):
        return self.ASIENTOS_POR_FILA
    
    def mostrar_mapa_asientos(self):
        print(f"\nMapa de asientos - Avión {self.modelo}")
        print("Business (Primeras filas):")
        self._mostrar_clase(self.asientos_business)
        print("\nTurista (Últimas filas):")
        self._mostrar_clase(self.asientos_turista)
    
    def _mostrar_clase(self, asientos):
        for i, fila in enumerate(asientos, 1):
            print(f"Fila {i}:", end=" ")
            print(" ".join("■" if a else "□" for a in fila))