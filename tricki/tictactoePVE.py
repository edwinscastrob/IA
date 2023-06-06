import random
from tkinter import Tk, Button, messagebox

FirstPlayer = "O"

def create_buttons(root, buttons):
    for i in range(3):
        for j in range(3):
            button = Button(root, text=" ", font=('Helvetica', 25, 'bold'), height=3,
                            width=6, bg="SystemButtonFace")
            button.grid(row=i, column=j)
            buttons.append(button)

def reset(buttons):
    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace", state='normal')

def get_button_texts(buttons):
    return [button['text'] for button in buttons]

def b_click(buttons, index):
    button = buttons[index]
    if button["text"] == " ":
        button["text"] = "X"
        play(buttons)

def tablero_lleno(tablero):
    return all(cell != ' ' for cell in tablero)

def ganador(tablero, jugador):
    # Comprobación de filas
    for i in range(3):
        if all(cell == jugador for cell in tablero[i * 3 : i * 3 + 3]):
            return True

    # Comprobación de columnas
    for i in range(3):
        if all(cell == jugador for cell in tablero[i :: 3]):
            return True

    # Comprobación de diagonales
    if tablero[0] == tablero[4] == tablero[8] == jugador:
        return True
    if tablero[2] == tablero[4] == tablero[6] == jugador:
        return True

    return False

def obtener_movimientos_disponibles(tablero):
    return [i for i in range(9) if tablero[i] == ' ']

def minimax(tablero, jugador, alpha, beta):
    if ganador(tablero, 'X'):
        return -1
    elif ganador(tablero, 'O'):
        return 1
    elif tablero_lleno(tablero):
        return 0

    if jugador == 'O':
        mejor_valor = float('-inf')
        for movimiento in obtener_movimientos_disponibles(tablero):
            nuevo_tablero = tablero[:]
            nuevo_tablero[movimiento] = jugador
            valor = minimax(nuevo_tablero, 'X', alpha, beta)
            mejor_valor = max(mejor_valor, valor)
            alpha = max(alpha, valor)
            if beta <= alpha:
                break
        return mejor_valor
    else:
        mejor_valor = float('inf')
        for movimiento in obtener_movimientos_disponibles(tablero):
            nuevo_tablero = tablero[:]
            nuevo_tablero[movimiento] = jugador
            valor = minimax(nuevo_tablero, 'O', alpha, beta)
            mejor_valor = min(mejor_valor, valor)
            beta = min(beta, valor)
            if beta <= alpha:
                break
        return mejor_valor

def movimiento_bot(tablero):
    mejor_valor = float('-inf')
    mejor_movimiento = None
    alpha = float('-inf')
    beta = float('inf')

    for movimiento in obtener_movimientos_disponibles(tablero):
        nuevo_tablero = tablero[:]
        nuevo_tablero[movimiento] = 'O'
        valor = minimax(nuevo_tablero, 'X', alpha, beta)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento

    return mejor_movimiento

def reset_message(buttons):
    response = messagebox.askyesno("Reset Game", "Do you want to reset the game?")
    if response:
        reset(buttons)

def play(buttons):
    tablero = get_button_texts(buttons)

    if not tablero_lleno(tablero) and not ganador(tablero, 'X') and not ganador(tablero, 'O'):
        movimiento = movimiento_bot(tablero)
        buttons[movimiento]["text"] = "O"
        tablero = get_button_texts(buttons)
        if ganador(get_button_texts(buttons), 'X'):
            messagebox.showinfo("Tic Tac Toe", f"¡¡¡ X Wins !!!")
            reset_message(buttons)
            start(buttons)
        elif ganador(get_button_texts(buttons), 'O'):
            messagebox.showinfo("Tic Tac Toe", f"¡¡¡ O Wins !!!")
            reset_message(buttons)
            start(buttons)
        elif tablero_lleno(tablero) and not ganador(tablero, 'X') and not ganador(tablero, 'O'):
            messagebox.showinfo("Tic Tac Toe", "It's a tie \nNo One Wins")
            reset_message(buttons)
            start(buttons)
    else:
        messagebox.showinfo("Tic Tac Toe", "It's a tie \nNo One Wins")
        reset_message(buttons)
        start(buttons)

def start(buttons):
    global FirstPlayer
    if FirstPlayer == "X":
        FirstPlayer = "O"
    else:
        movimiento = random.choice(obtener_movimientos_disponibles(get_button_texts(buttons)))
        buttons[movimiento]["text"] = "O"
        FirstPlayer = "X"

def main():
    root = Tk()
    root.title('Triki')
    root.iconbitmap('C:/Users/poloa/OneDrive/Documentos/IA/IA/tricki/tic-tac-toe.ico')
    root.resizable(False, False)

    buttons = []
    create_buttons(root, buttons)
    for i, button in enumerate(buttons):
        button.configure(command=lambda x=i: b_click(buttons, x))

    root.mainloop()

if __name__ == '__main__':
    main()
