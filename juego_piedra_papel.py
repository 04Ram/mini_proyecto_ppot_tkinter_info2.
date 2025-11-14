import tkinter as tk
import random

#ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijeras - Juego")
ventana.geometry("350x350")
ventana.config(bg="#A1A1A1")


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
        color="#C90303"
    label_resultado.config(text=resultado, fg=color)

modo_de_juegos = tk.Label(ventana, text="Modo de juego: Un jugador vs PC", font=("Arial", 10, "italic"), bg="#A1A1A1")
modo_de_juegos.pack(pady=5)

#etiquetas
titulo = tk.Label(ventana, text="Elige tu jugada:", font=("Times New Roman", 16,), bg="black", fg="white")
titulo.pack(pady=10)

#botones
boton_piedra = tk.Button(ventana, text="🧱 Piedra", width=20, command=lambda: jugar("Piedra"), font=("Courier",12, "italic"))
boton_piedra.pack(pady=5)

boton_papel = tk.Button(ventana, text="📄 Papel", width=20, command=lambda: jugar("Papel"), font=("Courier",12, "italic"))
boton_papel.pack(pady=5)

boton_tijeras = tk.Button(ventana, text="✂ Tijeras", width=20, command=lambda: jugar("Tijeras"), font=("Courier",12, "italic"))
boton_tijeras.pack(pady=5)
boton_salir = tk.Button(ventana, text="🚪Salir", width=20, command=ventana.quit, font=("Courier",12, "italic"),bg="red", fg="black")
boton_salir.pack(pady=5)

#etiquetas resultados
label_pc = tk.Label(ventana, text="", font=("Comic Sans MS", 12, "bold"), bg="#A1A1A1")
label_pc.pack(pady=10)

label_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#A1A1A1")
label_resultado.pack(pady=10)

ventana.mainloop()