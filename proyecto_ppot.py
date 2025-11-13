class juego:

    def papel(self, papel):
        return "hola soy papel"

-------------------------
import random
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Piedra, Papel o Tijera")

Puntuacion_usuario = 0
Puntuacion_computadora = 0
Eleccion_usuario = ""
Eleccion_computadora = ""

def elije_una_opcion(opcion):
    opciones = ["Piedra", "Papel", "Tijera"]
    return opciones[opcion]

def aleatorio_computadora():
    return random.opcion(["Piedra", "Papel", "Tijera"])



