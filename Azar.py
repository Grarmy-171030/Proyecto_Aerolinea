import random
from Pasajero import Pasajero
from Maleta import Maleta

class Azar:
    @staticmethod
    def generar_nombre():
        nombres = ["Ana", "Carlos", "David", "Elena", "Fernando", "Gabriela", 
                  "Héctor", "Irene", "Juan", "Laura", "Miguel", "Nuria"]
        apellidos = ["García", "Rodríguez", "González", "Fernández", "López", 
                    "Martínez", "Sánchez", "Pérez", "Gómez", "Ruiz"]
        return f"{random.choice(nombres)} {random.choice(apellidos)} {random.choice(apellidos)}"
    
    @staticmethod
    def generar_pasaporte():
        letras = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        numeros = ''.join(random.choices('0123456789', k=6))
        return f"{letras}{numeros}"
    
    @staticmethod
    def generar_telefono():
        return f"6{''.join(random.choices('0123456789', k=8))}"
    
    @staticmethod
    def generar_edad():
        return random.randint(1, 80)
    
    @staticmethod
    def generar_maleta():
        peso = round(random.uniform(5, 30), 2)
        ancho = random.randint(30, 60)
        alto = random.randint(40, 80)
        fondo = random.randint(20, 40)
        return Maleta(peso, ancho, alto, fondo)
    
    @staticmethod
    def generar_pasajero():
        return Pasajero(
            Azar.generar_nombre(),
            Azar.generar_pasaporte(),
            Azar.generar_telefono(),
            Azar.generar_edad(),
            Azar.generar_maleta()
        )