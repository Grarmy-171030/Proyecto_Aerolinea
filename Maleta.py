class Maleta:
    def __init__(self, peso, ancho, alto, fondo):
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        self.fondo = fondo
        self.PESO_MAXIMO = 23
        self.MEDIDA_MAXIMA = 158

    def excede_peso(self):
        return self.peso > self.PESO_MAXIMO

    def excede_medidas(self):
        return (self.ancho + self.alto + self.fondo) > self.MEDIDA_MAXIMA