import tkinter as tk
from tkinter import messagebox

# variables del juego
player = "X"
game_over = False

# FUNCION PARA VERIFICAR SI HAY UN GANADOR
def check_winner():
    # revisa filas y columnas
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    # revisa diagonales
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

# FUNCION PARA DESHABILITAR TODOS LOS BOTONES CUANDO HAYA GANADOR
def disable_all():
    for r in range(3):
        for c in range(3):
            buttons[r][c]["state"] = "disabled"

# FUNCION QUE SE EJECUTA CUANDO SE PRESIONA UN BOTON
def button_click(row, col):
    global player, game_over
    # ve y verifica que el button este vacio
    if buttons[row][col]["text"] == "" and not game_over:
        # escribe X o O
        buttons[row][col]["text"] = player
        # cambia el color del boton
        buttons[row][col]["bg"] = "#36D7B7" if player == "X" else "#F4D03F"  # ✅ colores corregidos
        buttons[row][col]["state"] = "disabled"  # deshabilita boton para que no se pueda volver a presionar

        if check_winner():  # verifica ganador
            messagebox.showinfo("Tic Tac Toe", f"¡Jugador {player} gana!")
            game_over = True
            disable_all()  # deshabilita todos los botones
            turn_label.config(text=f"Ganó {player}")  # actualiza etiqueta de turno/ganador
        # cuando se llene la pantalla todos los botones de las col y filas esten llenos
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Tic Tac Toe", "¡Es un empate!")
            game_over = True
            turn_label.config(text="Empate")
        else:
            # si no hay ganador ni empate, cambia el turno
            player = "O" if player == "X" else "X"
            turn_label.config(text=f"Turno: {player}")  # actualiza etiqueta de turno

# FUNCION PARA REINICIAR EL JUEGO
def reset_game():
    global player, game_over
    player = "X"
    game_over = False
    turn_label.config(text=f"Turno: {player}")
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col]["bg"] = "SystemButtonFace"  # restablece el color del boton al predeterminado
            buttons[row][col]["state"] = "normal"  # vuelve a habilitar los botones

# CREACION DE LA VENTANA PRINCIPAL
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x360")  # un poco más de espacio para el label
root.configure(bg="#AED6F1")

# crea un marco para contener los botones
frame = tk.Frame(root, bg="#AED6F1")
frame.place(relx=0.5, rely=0.55, anchor="center")  # centrado con un poco más de espacio arriba para el label

# crea los botones del juego
buttons = [[tk.Button(frame, text="", font=("Arial", 24), width=3, height=1,
                      command=lambda r=row, c=col: button_click(r, c)) for col in range(3)] for row in range(3)]

# crea una cuadrícula de botones separados por 10 pixeles
for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

# label para mostrar el turno
turn_label = tk.Label(root, text="Turno: X", font=("Arial", 12), bg="#AED6F1")
turn_label.place(relx=0.5, rely=0.1, anchor="center")

# cada vez que se presiona el boton, se reinicia el juego
reset_button = tk.Button(root, text="Reiniciar Juego", font=("Arial", 14),
                         command=reset_game, bg="#546E7A", fg="white")
reset_button.place(relx=0.5, rely=0.92, anchor="center")

root.mainloop()  # inicia el bucle principal de la ventana
