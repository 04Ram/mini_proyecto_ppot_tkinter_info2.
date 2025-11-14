import tkinter as tk
import random

# ---------- FUNCIÓN: JUEGO CONTRA PC ----------
def ventana_vs_pc():
    menu.destroy()  # Cierra el menú principal
    
    ventana = tk.Tk()
    ventana.title("Piedra, Papel o Tijeras - Jugador vs PC")
    ventana.geometry("350x350")
    ventana.config(bg="#A1A1A1")

    def jugar(eleccion_jugador):
        opciones = ["Piedra", "Papel", "Tijeras"]
        eleccion_pc = random.choice(opciones)

        label_jugador.config(text=f"Tú elegiste: {eleccion_jugador}")
        label_pc.config(text=f"La computadora eligió: {eleccion_pc}")

        if eleccion_jugador == eleccion_pc:
            resultado = "Empate 🤝"
            color = "#8A530B"
        elif (eleccion_jugador == "Piedra" and eleccion_pc == "Tijeras") or \
             (eleccion_jugador == "Tijeras" and eleccion_pc == "Papel") or \
             (eleccion_jugador == "Papel" and eleccion_pc == "Piedra"):
            resultado = "¡Ganaste! 🎉"
            color = "#197003"
        else:
            resultado = "Perdiste 😢"
            color = "#C90303"

        label_resultado.config(text=resultado, fg=color)

    tk.Label(ventana, text="Modo: Jugador vs PC", font=("Arial", 10, "italic"), bg="#A1A1A1").pack(pady=5)
    tk.Label(ventana, text="Elige tu jugada:", font=("Times New Roman", 16), bg="black", fg="white").pack(pady=10)

    tk.Button(ventana, text="🧱 Piedra", width=20, command=lambda: jugar("Piedra"), font=("Courier",12, "italic")).pack(pady=5)
    tk.Button(ventana, text="📄 Papel", width=20, command=lambda: jugar("Papel"), font=("Courier",12, "italic")).pack(pady=5)
    tk.Button(ventana, text="✂ Tijeras", width=20, command=lambda: jugar("Tijeras"), font=("Courier",12, "italic")).pack(pady=5)
    tk.Button(ventana, text="⬅ Volver al menú", width=20, font=("Courier",12,"italic"), bg="gray", command=lambda:[ventana.destroy(), mostrar_menu()]).pack(pady=10)

    label_jugador = tk.Label(ventana, text="", font=("Comic Sans MS", 12, "bold"), bg="#A1A1A1")
    label_jugador.pack(pady=5)
    label_pc = tk.Label(ventana, text="", font=("Comic Sans MS", 12, "bold"), bg="#A1A1A1")
    label_pc.pack(pady=5)
    label_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#A1A1A1")
    label_resultado.pack(pady=10)

    tk.Button(ventana, text="⬅ Volver al menú", width=20, font=("Courier",12,"italic"), bg="gray", command=lambda:[ventana.destroy(), mostrar_menu()]).pack(pady=10)
    tk.Button(ventana, text="🚪 Salir", width=20, font=("Courier",12,"italic"), bg="red", fg="white", command=ventana.quit).pack(pady=5)

    ventana.mainloop()


# ---------- FUNCIÓN: JUEGO 2 JUGADORES ----------
def ventana_dos_jugadores():
    menu.destroy()

    ventana = tk.Tk()
    ventana.title("Piedra, Papel o Tijeras - 2 Jugadores")
    ventana.geometry("350x400")
    ventana.config(bg="#A1A1A1")

    turno = tk.StringVar(value="Jugador 1")
    jugada_j1 = tk.StringVar(value="")
    
    def jugar(eleccion):
        if turno.get() == "Jugador 1":
            jugada_j1.set(eleccion)
            turno.set("Jugador 2")
            label_turno.config(text="Turno de Jugador 2")
        else:
            jugada_j2 = eleccion
            mostrar_resultado(jugada_j1.get(), jugada_j2)

    def mostrar_resultado(j1, j2):
        label_elecciones.config(text=f"Jugador 1: {j1} | Jugador 2: {j2}")

        if j1 == j2:
            resultado = "Empate 🤝"
            color = "#8A530B"
        elif (j1 == "Piedra" and j2 == "Tijeras") or \
             (j1 == "Tijeras" and j2 == "Papel") or \
             (j1 == "Papel" and j2 == "Piedra"):
            resultado = "¡Jugador 1 Gana! 🎉"
            color = "#197003"
        else:
            resultado = "¡Jugador 2 Gana! 🎉"
            color = "#C90303"

        label_resultado.config(text=resultado, fg=color)
        turno.set("Jugador 1")
        label_turno.config(text="Turno de Jugador 1")

    tk.Label(ventana, text="Modo: 2 Jugadores", font=("Arial", 10, "italic"), bg="#A1A1A1").pack(pady=5)
    label_turno = tk.Label(ventana, text="Turno de Jugador 1", font=("Times New Roman", 16), bg="black", fg="white")
    label_turno.pack(pady=10)

    for texto in ["🧱 Piedra", "📄 Papel", "✂ Tijeras"]:
        opcion = texto.split()[1]
        tk.Button(ventana, text=texto, width=20, command=lambda o=opcion: jugar(o), font=("Courier",12,"italic")).pack(pady=5)

    label_elecciones = tk.Label(ventana, text="", font=("Comic Sans MS", 12, "bold"), bg="#A1A1A1")
    label_elecciones.pack(pady=10)
    label_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#A1A1A1")
    label_resultado.pack(pady=10)

    tk.Button(ventana, text="⬅ Volver al menú", width=20, font=("Courier",12,"italic"), bg="gray", command=lambda:[ventana.destroy(), mostrar_menu()]).pack(pady=10)
    tk.Button(ventana, text="🚪 Salir", width=20, font=("Courier",12,"italic"), bg="red", fg="white", command=ventana.quit).pack(pady=5)

    ventana.mainloop()


# ---------- MENÚ PRINCIPAL ----------
def mostrar_menu():
    global menu
    menu = tk.Tk()
    menu.title("Menú Principal - Piedra, Papel o Tijeras")
    menu.geometry("350x300")
    menu.config(bg="#A1A1A1")

    tk.Label(menu, text="🎮 Elige el modo de juego 🎮", font=("Times New Roman", 16, "bold"), bg="black", fg="white").pack(pady=20)

    tk.Button(menu, text="🧠 Jugador vs PC", width=25, font=("Courier",12,"italic"), command=ventana_vs_pc).pack(pady=10)
    tk.Button(menu, text="👥 2 Jugadores", width=25, font=("Courier",12,"italic"), command=ventana_dos_jugadores).pack(pady=10)
    tk.Button(menu, text="🚪 Salir", width=25, font=("Courier",12,"italic"), bg="red", fg="white", command=menu.quit).pack(pady=20)

    menu.mainloop()


# ---------- INICIO ----------
mostrar_menu()
