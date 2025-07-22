from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Gestion_Aerolinea import Aerolinea
from Clase import Clase
from Pasajero import Pasajero
from Maleta import Maleta


class VentanaAerolinea(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=600)
        self.master = master
        self.aerolinea = Aerolinea()
        self.sistema_inicializado = False
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Frame para botones
        frame_botones = Frame(self, bg="#bfdaff")
        frame_botones.place(x=0, y=0, width=100, height=600)

        # Botones principales
        Button(frame_botones, text="Inicializar", command=self.inicializar_sistema,
               bg="blue", fg="white").place(x=10, y=30, width=80, height=30)

        self.btnReservar = Button(frame_botones, text="Reservar", command=self.mostrar_reserva,
                                  bg="blue", fg="white", state=DISABLED)
        self.btnReservar.place(x=10, y=70, width=80, height=30)

        self.btnMapa = Button(frame_botones, text="Mapa", command=self.mostrar_mapa,
                              bg="blue", fg="white", state=DISABLED)
        self.btnMapa.place(x=10, y=110, width=80, height=30)

        self.btnListar = Button(frame_botones, text="Listar", command=self.listar_pasajeros,
                                bg="blue", fg="white", state=DISABLED)
        self.btnListar.place(x=10, y=150, width=80, height=30)

        self.btnMenores = Button(frame_botones, text="Menores", command=self.mostrar_menores,
                                 bg="blue", fg="white", state=DISABLED)
        self.btnMenores.place(x=10, y=190, width=80, height=30)

        Button(frame_botones, text="Salir", command=self.salir,
               bg="red", fg="white").place(x=10, y=230, width=80, height=30)

        # Frame de datos principales
        frame_datos = Frame(self, bg="#d3dde3")
        frame_datos.place(x=100, y=0, width=700, height=600)

        # Lista de vuelos
        Label(frame_datos, text="Vuelos disponibles:", bg="#d3dde3").place(x=10, y=10)
        self.lista_vuelos = Listbox(frame_datos)
        self.lista_vuelos.place(x=10, y=30, width=680, height=100)

        # Frame para reservas
        self.frame_reserva = Frame(frame_datos, bg="#e3e3e3")
        self.frame_reserva.place(x=10, y=140, width=680, height=200)

        # Campos del pasajero
        Label(self.frame_reserva, text="Nombre:").place(x=10, y=10)
        self.txtNombre = Entry(self.frame_reserva)
        self.txtNombre.place(x=80, y=10, width=200)

        Label(self.frame_reserva, text="Pasaporte:").place(x=10, y=40)
        self.txtPasaporte = Entry(self.frame_reserva)
        self.txtPasaporte.place(x=80, y=40, width=200)

        Label(self.frame_reserva, text="Edad:").place(x=10, y=70)
        self.txtEdad = Entry(self.frame_reserva)
        self.txtEdad.place(x=80, y=70, width=50)

        # Campos de equipaje
        Label(self.frame_reserva, text="Peso maleta (kg):").place(x=300, y=10)
        self.txtPeso = Entry(self.frame_reserva)
        self.txtPeso.place(x=400, y=10, width=50)

        Label(self.frame_reserva, text="Ancho (cm):").place(x=300, y=40)
        self.txtAncho = Entry(self.frame_reserva)
        self.txtAncho.place(x=400, y=40, width=50)

        Label(self.frame_reserva, text="Alto (cm):").place(x=300, y=70)
        self.txtAlto = Entry(self.frame_reserva)
        self.txtAlto.place(x=400, y=70, width=50)

        Label(self.frame_reserva, text="Fondo (cm):").place(x=300, y=100)
        self.txtFondo = Entry(self.frame_reserva)
        self.txtFondo.place(x=400, y=100, width=50)

        # Selección de asiento
        Label(self.frame_reserva, text="Clase:").place(x=10, y=100)
        self.clase_var = StringVar(value="TURISTA")
        OptionMenu(self.frame_reserva, self.clase_var, "BUSINESS", "TURISTA").place(x=80, y=100)

        Label(self.frame_reserva, text="Fila:").place(x=10, y=130)
        self.txtFila = Entry(self.frame_reserva)
        self.txtFila.place(x=50, y=130, width=50)

        Label(self.frame_reserva, text="Butaca:").place(x=120, y=130)
        self.txtButaca = Entry(self.frame_reserva)
        self.txtButaca.place(x=180, y=130, width=50)

        # Botones de acción
        Button(self.frame_reserva, text="Guardar", command=self.guardar_reserva,
               bg="green", fg="white").place(x=10, y=160, width=80)

        Button(self.frame_reserva, text="Limpiar", command=self.mostrar_reserva,
               bg="gray", fg="white").place(x=100, y=160, width=80)

        # Área de resultados
        self.text_resultados = Text(frame_datos, height=15, width=85)
        self.text_resultados.place(x=10, y=350)

        # Configurar tags para advertencias
        self.text_resultados.tag_config("warning", foreground="red")

    def inicializar_sistema(self):
        try:
            self.aerolinea.inicializar_sistema()
            self.sistema_inicializado = True
            self.btnReservar.config(state=NORMAL)
            self.btnMapa.config(state=NORMAL)
            self.btnListar.config(state=NORMAL)
            self.btnMenores.config(state=NORMAL)

            self.lista_vuelos.delete(0, END)
            for vuelo in self.aerolinea.vuelos:
                self.lista_vuelos.insert(END, f"{vuelo.origen} → {vuelo.destino} ({vuelo.avion.modelo})")

            messagebox.showinfo("Listo", "Sistema inicializado!")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo inicializar: {e}")

    def mostrar_reserva(self):
        # Limpiar campos de reserva
        self.txtNombre.delete(0, END)
        self.txtPasaporte.delete(0, END)
        self.txtEdad.delete(0, END)
        self.txtPeso.delete(0, END)
        self.txtAncho.delete(0, END)
        self.txtAlto.delete(0, END)
        self.txtFondo.delete(0, END)
        self.txtFila.delete(0, END)
        self.txtButaca.delete(0, END)
        self.clase_var.set("TURISTA")

    def guardar_reserva(self):
        if not self.sistema_inicializado:
            messagebox.showwarning("Error", "Primero inicialice el sistema")
            return

        seleccion = self.lista_vuelos.curselection()
        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un vuelo")
            return

        vuelo = self.aerolinea.vuelos[seleccion[0]]

        # Validar campos requeridos
        campos = [
            self.txtNombre.get(),
            self.txtPasaporte.get(),
            self.txtEdad.get(),
            self.txtPeso.get(),
            self.txtAncho.get(),
            self.txtAlto.get(),
            self.txtFondo.get(),
            self.txtFila.get(),
            self.txtButaca.get()
        ]

        if not all(campos):
            messagebox.showwarning("Error", "Complete todos los campos")
            return

        try:
            # Crear maleta con todos los parámetros
            maleta = Maleta(
                float(self.txtPeso.get()),
                int(self.txtAncho.get()),
                int(self.txtAlto.get()),
                int(self.txtFondo.get())
            )

            # Crear pasajero
            pasajero = Pasajero(
                self.txtNombre.get(),
                self.txtPasaporte.get(),
                "000000000",  # Teléfono por defecto
                int(self.txtEdad.get()),
                maleta
            )

            # Hacer reserva (la validación de asiento ocupado está en Gestion_Aerolinea)
            clase = Clase.BUSINESS if self.clase_var.get() == "BUSINESS" else Clase.TURISTA
            fila = int(self.txtFila.get())
            butaca = int(self.txtButaca.get())

            # Esta llamada ya maneja la verificación de asientos ocupados
            resultado = vuelo.avion.reservar_asiento(fila, butaca, clase, pasajero)

            if resultado:  # Si la reserva fue exitosa
                letra = chr(64 + butaca)
                self.text_resultados.insert(END, f"Reserva exitosa! Asiento: {fila}{letra}\n")

                # Mostrar advertencias de equipaje si aplican
                if maleta.excede_peso():
                    self.text_resultados.insert(END, "ADVERTENCIA: Equipaje excede peso máximo (23kg)\n", "warning")
                if maleta.excede_medidas():
                    self.text_resultados.insert(END, "ADVERTENCIA: Equipaje excede medidas (158cm)\n", "warning")

                self.mostrar_reserva()
            else:
                messagebox.showerror("Error", "No se pudo reservar: Asiento ocupado o inválido")

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

    def mostrar_mapa(self):
        if not self.sistema_inicializado:
            messagebox.showwarning("Error", "Primero inicialice el sistema")
            return

        seleccion = self.lista_vuelos.curselection()
        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un vuelo")
            return

        avion = self.aerolinea.vuelos[seleccion[0]].avion

        self.text_resultados.delete(1.0, END)
        self.text_resultados.insert(END, f"Mapa de asientos - {avion.modelo}\n\n")

        # Business Class
        self.text_resultados.insert(END, "Business Class:\n")
        for i, fila in enumerate(avion.asientos_business, 1):
            self.text_resultados.insert(END, f"Fila {i}: ")
            for asiento in fila:
                self.text_resultados.insert(END, "■ " if asiento else "□ ")
            self.text_resultados.insert(END, "\n")

        # Turista Class
        self.text_resultados.insert(END, "\nTurista Class:\n")
        for i, fila in enumerate(avion.asientos_turista, 1):
            self.text_resultados.insert(END, f"Fila {i}: ")
            for asiento in fila:
                self.text_resultados.insert(END, "■ " if asiento else "□ ")
            self.text_resultados.insert(END, "\n")

    def listar_pasajeros(self):
        if not self.sistema_inicializado:
            messagebox.showwarning("Error", "Primero inicialice el sistema")
            return

        seleccion = self.lista_vuelos.curselection()
        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un vuelo")
            return

        avion = self.aerolinea.vuelos[seleccion[0]].avion

        self.text_resultados.delete(1.0, END)
        self.text_resultados.insert(END, "Lista de pasajeros:\n\n")

        # Business Class
        self.text_resultados.insert(END, "Business Class:\n")
        for fila in range(1, avion.get_numero_filas(Clase.BUSINESS) + 1):
            for butaca in range(1, avion.get_butacas_por_fila() + 1):
                pasajero = avion.get_pasajero(fila, butaca, Clase.BUSINESS)
                if pasajero:
                    letra = chr(64 + butaca)
                    self.text_resultados.insert(END, f" {fila}{letra}: {pasajero.get_nombre()}\n")

        # Turista Class
        self.text_resultados.insert(END, "\nTurista Class:\n")
        for fila in range(1, avion.get_numero_filas(Clase.TURISTA) + 1):
            for butaca in range(1, avion.get_butacas_por_fila() + 1):
                pasajero = avion.get_pasajero(fila, butaca, Clase.TURISTA)
                if pasajero:
                    letra = chr(64 + butaca)
                    self.text_resultados.insert(END, f" {fila}{letra}: {pasajero.get_nombre()}\n")

    def mostrar_menores(self):
        if not self.sistema_inicializado:
            messagebox.showwarning("Error", "Primero inicialice el sistema")
            return

        seleccion = self.lista_vuelos.curselection()
        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un vuelo")
            return

        avion = self.aerolinea.vuelos[seleccion[0]].avion

        self.text_resultados.delete(1.0, END)
        self.text_resultados.insert(END, "Pasajeros menores de edad:\n\n")

        encontrados = False

        # Business Class
        for fila in range(1, avion.get_numero_filas(Clase.BUSINESS) + 1):
            for butaca in range(1, avion.get_butacas_por_fila() + 1):
                pasajero = avion.get_pasajero(fila, butaca, Clase.BUSINESS)
                if pasajero and pasajero.get_edad() < 18:
                    encontrados = True
                    letra = chr(64 + butaca)
                    self.text_resultados.insert(END,
                                                f" {fila}{letra}: {pasajero.get_nombre()} ({pasajero.get_edad()} años)\n")

        # Turista Class
        for fila in range(1, avion.get_numero_filas(Clase.TURISTA) + 1):
            for butaca in range(1, avion.get_butacas_por_fila() + 1):
                pasajero = avion.get_pasajero(fila, butaca, Clase.TURISTA)
                if pasajero and pasajero.get_edad() < 18:
                    encontrados = True
                    letra = chr(64 + butaca)
                    self.text_resultados.insert(END,
                                                f" {fila}{letra}: {pasajero.get_nombre()} ({pasajero.get_edad()} años)\n")

        if not encontrados:
            self.text_resultados.insert(END, "No hay menores en este vuelo")

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
            self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Sistema de Aerolínea")
    app = VentanaAerolinea(master=root)
    root.mainloop()