"""class juego:

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
    return random.opcion(["Piedra", "Papel", "Tijera"])"""

import tkinter as tk
import random

#ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijeras :)")
ventana.geometry("350x650")
ventana.config(bg="#A1A1A1")

# Contadores globales
puntuacion_jugador = 0
puntuacion_pc = 0

#func.pricipal
def jugar(eleccion_jugador):
    opciones = ["Piedra", "Papel", "Tijeras"]
    eleccion_pc = random.choice(opciones)
    
    label_pc.config(text=f"La computadora eligió: {eleccion_pc}")

    if eleccion_jugador == eleccion_pc:
        resultado = "Empate 🤝"
        color="#8A530B"
    elif (eleccion_jugador == "Piedra" and eleccion_pc == "Tijeras") or \
         (eleccion_jugador == "Tijeras" and eleccion_pc == "Papel") or \
         (eleccion_jugador == "Papel" and eleccion_pc == "Piedra"):
        resultado = "¡Ganaste! 🎉"
        color="#197003"
    else:
        resultado = "Perdiste :("
         color = "#C90303"
        puntuacion_pc += 1
        ganador = "Computadora"

    label_resultado.config(text=resultado, fg=color)
    actualizar_marcador()

    agregar_historial(eleccion_jugador, eleccion_pc, ganador)


#etiquetas
titulo = tk.Label(ventana, text="Elige tu jugada:", font=("Times New Roman", 16,), bg="black", fg="white")
titulo.pack(pady=10)

#botones
boton_piedra = tk.Button(ventana, text="🧱 Piedra", width=20, command=lambda: jugar("Piedra"), font=("Courier",12, "italic"))
boton_piedra.pack(pady=5)

boton_papel = tk.Button(ventana, text="📄 Papel", width=20, command=lambda: jugar("Papel"), font=("Courier",12, "italic"))
boton_papel.pack(pady=5)

boton_tijeras = tk.Button(ventana, text="✂️ Tijeras", width=20, command=lambda: jugar("Tijeras"), font=("Courier",12, "italic"))
boton_tijeras.pack(pady=5)

#etiquetas resultados
label_pc = tk.Label(ventana, text="", font=("Comic Sans MS", 12, "bold"), bg="#A1A1A1")
label_pc.pack(pady=10)

label_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#A1A1A1")
label_resultado.pack(pady=10)

# historial
label_historial = tk.Label(ventana, text="Historial de partidas:", font=("Arial", 12, "bold"), bg="#A1A1A1")
label_historial.pack(pady=5)

historial = tk.Listbox(ventana, width=45, height=10)
historial.pack(pady=5)

# botón reiniciar
boton_reiniciar = tk.Button(ventana, text="🔄 Reiniciar juego", font=("Arial", 12, "bold"), bg="black", fg="white", command=reiniciar)
boton_reiniciar.pack(pady=10)


ventana.mainloop()






