# Añade esta importación con las demás
from Pasajero import Pasajero
from Avion import Avion
from Vuelo import Vuelo
from Clase import Clase
from Azar import Azar
from Maleta import Maleta
import random
import sys

class Aerolinea:
    def __init__(self):
        self.vuelos = []
        self.aviones = []
        self.inicializado = False
    
    def mostrar_menu(self):
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Inicializar sistema")
            print("2. Reservar asiento")
            print("3. Mostrar mapa de asientos")
            print("4. Listar pasajeros")
            print("5. Mostrar pasajeros menores")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.inicializar_sistema()
            elif opcion == "2":
                self.reservar_asiento()
            elif opcion == "3":
                self.mostrar_mapa()
            elif opcion == "4":
                self.listar_pasajeros()
            elif opcion == "5":
                self.mostrar_menores()
            elif opcion == "6":
                print("\nGracias por usar el sistema. ¡Hasta pronto!")
                sys.exit()
            else:
                print("Opción no válida. Intente nuevamente.")
    
    def inicializar_sistema(self):
        if self.inicializado:
            print("El sistema ya fue inicializado")
            return
        
        # Crear aviones
        avion1 = Avion("Boeing 737-800", 16, 48)  # 4 filas business, 12 turista
        avion2 = Avion("Airbus A320", 12, 60)     # 3 filas business, 15 turista
        
        self.aviones.extend([avion1, avion2])
        
        # Crear vuelos
        self.vuelos.append(Vuelo("Madrid", "Barcelona", "20/07/2024", avion1))
        self.vuelos.append(Vuelo("Madrid", "París", "21/07/2024", avion2))
        
        # Hacer algunas reservas automáticas
        for vuelo in self.vuelos:
            for _ in range(3):  # 3 reservas business
                self._hacer_reserva_automatica(vuelo, Clase.BUSINESS)
            for _ in range(5):  # 5 reservas turista
                self._hacer_reserva_automatica(vuelo, Clase.TURISTA)
        
        self.inicializado = True
        print("\nSistema inicializado correctamente con 2 vuelos")
    
    def _hacer_reserva_automatica(self, vuelo, clase):
        avion = vuelo.get_avion()
        filas = avion.get_numero_filas(clase)
        butacas = avion.get_butacas_por_fila()
        
        for _ in range(10):  # Intentos máximos
            fila = random.randint(1, filas)
            butaca = random.randint(1, butacas)
            if avion.get_pasajero(fila, butaca, clase) is None:
                pasajero = Azar.generar_pasajero()
                avion.reservar_asiento(fila, butaca, clase, pasajero)
                return True
        return False
    
    def seleccionar_vuelo(self):
        print("\nVuelos disponibles:")
        for i, vuelo in enumerate(self.vuelos, 1):
            print(f"{i}. {vuelo}")
        
        while True:
            try:
                opcion = int(input("Seleccione vuelo (número): ")) - 1
                if 0 <= opcion < len(self.vuelos):
                    return self.vuelos[opcion]
                print("Número de vuelo no válido")
            except ValueError:
                print("Ingrese un número válido")
    
    def reservar_asiento(self):
        if not self.inicializado:
            print("Primero debe inicializar el sistema (Opción 1)")
            return
        
        vuelo = self.seleccionar_vuelo()
        avion = vuelo.get_avion()
        
        print("\nTipos de clase:")
        print("1. Business")
        print("2. Turista")
        
        while True:
            clase_op = input("Seleccione clase (1-2): ")
            if clase_op in ("1", "2"):
                clase = Clase.BUSINESS if clase_op == "1" else Clase.TURISTA
                break
            print("Opción no válida")
        
        avion.mostrar_mapa_asientos()
        
        filas = avion.get_numero_filas(clase)
        butacas = avion.get_butacas_por_fila()
        
        print(f"\nSeleccione asiento (Business: 1-{filas}, Butacas: 1-{butacas} -> A-D)")
        
        while True:
            try:
                fila = int(input(f"Fila (1-{filas}): "))
                butaca = int(input(f"Butaca (1-{butacas}): "))
                
                if 1 <= fila <= filas and 1 <= butaca <= butacas:
                    if avion.get_pasajero(fila, butaca, clase) is None:
                        pasajero = self.ingresar_datos_pasajero()
                        if pasajero:
                            avion.reservar_asiento(fila, butaca, clase, pasajero)
                            letra = chr(64 + butaca)
                            print(f"\n¡Reserva exitosa! Asiento: {fila}{letra} - {pasajero.get_nombre()}")
                            return
                        else:
                            print("Reserva cancelada")
                            return
                    else:
                        print("Asiento ya ocupado")
                else:
                    print("Ubicación no válida")
            except ValueError:
                print("Ingrese números válidos")
    
    def ingresar_datos_pasajero(self):
        print("\nIngrese datos del pasajero:")
        nombre = input("Nombre completo: ")
        pasaporte = input("Pasaporte: ")
        telefono = input("Teléfono: ")
        
        while True:
            try:
                edad = int(input("Edad: "))
                if 0 < edad < 120:
                    break
                print("Edad no válida")
            except ValueError:
                print("Ingrese un número válido")
        
        print("\nDatos de equipaje:")
        while True:
            try:
                peso = float(input("Peso (kg): "))
                ancho = int(input("Ancho (cm): "))
                alto = int(input("Alto (cm): "))
                fondo = int(input("Fondo (cm): "))
                break
            except ValueError:
                print("Ingrese valores numéricos válidos")
        
        maleta = Maleta(peso, ancho, alto, fondo)
        return Pasajero(nombre, pasaporte, telefono, edad, maleta)
    
    def mostrar_mapa(self):
        if not self.inicializado:
            print("Primero debe inicializar el sistema (Opción 1)")
            return
        
        vuelo = self.seleccionar_vuelo()
        vuelo.get_avion().mostrar_mapa_asientos()
    
    def listar_pasajeros(self):
        if not self.inicializado:
            print("Primero debe inicializar el sistema (Opción 1)")
            return
        
        vuelo = self.seleccionar_vuelo()
        avion = vuelo.get_avion()
        
        print(f"\nPasajeros del vuelo {vuelo}:")
        print("\nClase Business:")
        self._listar_pasajeros_clase(avion, Clase.BUSINESS)
        
        print("\nClase Turista:")
        self._listar_pasajeros_clase(avion, Clase.TURISTA)
    
    def _listar_pasajeros_clase(self, avion, clase):
        filas = avion.get_numero_filas(clase)
        butacas = avion.get_butacas_por_fila()
        
        for fila in range(1, filas + 1):
            for butaca in range(1, butacas + 1):
                pasajero = avion.get_pasajero(fila, butaca, clase)
                if pasajero:
                    letra = chr(64 + butaca)
                    print(f"Fila {fila}{letra}: {pasajero.get_nombre()} ({pasajero.get_edad()} años) - {pasajero.get_pasaporte()}")
    
    def mostrar_menores(self):
        if not self.inicializado:
            print("Primero debe inicializar el sistema (Opción 1)")
            return
        
        vuelo = self.seleccionar_vuelo()
        avion = vuelo.get_avion()
        
        print(f"\nPasajeros menores de edad en vuelo {vuelo}:")
        print("\nClase Business:")
        self._mostrar_menores_clase(avion, Clase.BUSINESS)
        
        print("\nClase Turista:")
        self._mostrar_menores_clase(avion, Clase.TURISTA)
    
    def _mostrar_menores_clase(self, avion, clase):
        filas = avion.get_numero_filas(clase)
        butacas = avion.get_butacas_por_fila()
        encontrados = False
        
        for fila in range(1, filas + 1):
            for butaca in range(1, butacas + 1):
                pasajero = avion.get_pasajero(fila, butaca, clase)
                if pasajero and pasajero.get_edad() < 18:
                    letra = chr(64 + butaca)
                    print(f"Fila {fila}{letra}: {pasajero.get_nombre()} ({pasajero.get_edad()} años)")
                    encontrados = True
        
        if not encontrados:
            print("No hay pasajeros menores en esta clase")

if __name__ == "__main__":
    import random
    sistema = Aerolinea()
    sistema.mostrar_menu()