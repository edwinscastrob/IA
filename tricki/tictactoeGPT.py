import random

def imprimir_tablero(tablero):
    print('-------------')
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            print(tablero[i*3 + j], '|', end=' ')
        print('\n-------------')

def tablero_lleno(tablero):
    return all(cell != ' ' for cell in tablero)

def ganador(tablero, jugador):
    # Comprobación de filas
    for i in range(3):
        if all(cell == jugador for cell in tablero[i*3:i*3+3]):
            return True

    # Comprobación de columnas
    for i in range(3):
        if all(cell == jugador for cell in tablero[i::3]):
            return True

    # Comprobación de diagonales
    if tablero[0] == tablero[4] == tablero[8] == jugador:
        return True
    if tablero[2] == tablero[4] == tablero[6] == jugador:
        return True

    return False

def movimiento_valido(tablero, movimiento):
    return tablero[movimiento] == ' '

def obtener_movimientos_disponibles(tablero):
    return [i for i in range(9) if tablero[i] == ' ']

def minimax(tablero, jugador):
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
            valor = minimax(nuevo_tablero, 'X')
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float('inf')
        for movimiento in obtener_movimientos_disponibles(tablero):
            nuevo_tablero = tablero[:]
            nuevo_tablero[movimiento] = jugador
            valor = minimax(nuevo_tablero, 'O')
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def movimiento_bot(tablero):
    mejor_valor = float('-inf')
    mejor_movimiento = None

    for movimiento in obtener_movimientos_disponibles(tablero):
        nuevo_tablero = tablero[:]
        nuevo_tablero[movimiento] = 'O'
        valor = minimax(nuevo_tablero, 'X')
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento

    return mejor_movimiento

def jugar():
    tablero = [' ' for _ in range(9)]
    jugador_actual = 'X'

    while not tablero_lleno(tablero) and not ganador(tablero, 'X') and not ganador(tablero, 'O'):
        if jugador_actual == 'X':
            movimiento = int(input("Ingresa tu movimiento (0-8): "))
            if movimiento_valido(tablero, movimiento):
                tablero[movimiento] = jugador_actual
                jugador_actual = 'O'
            else:
                print("Movimiento inválido. Intenta nuevamente.")
        else:
            movimiento = movimiento_bot(tablero)
            tablero[movimiento] = jugador_actual
            jugador_actual = 'X'

        imprimir_tablero(tablero)

    if ganador(tablero, 'X'):
        print("¡Ganaste!")
    elif ganador(tablero, 'O'):
        print("¡Perdiste!")
    else:
        print("¡Empate!")

jugar()
