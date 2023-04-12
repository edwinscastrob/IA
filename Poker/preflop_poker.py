
import csv
import numpy as np

'''
Manos posibles Preflop 
o diferente palo
s mismo palo
'''
# Crear matriz de rango de manos de poker
hands = np.array([
    ['AA', 'AKS', 'AQS', 'AJS', 'ATS', 'A9S', 'A8S',
        'A7S', 'A6S', 'A5S', 'A4S', 'A3S', 'A2S'],
    ['AKO', 'KK', 'KQS', 'KJS', 'KTS', 'K9S', 'K8S',
        'K7S', 'K6S', 'K5S', 'K4S', 'K3S', 'K2S'],
    ['AQO', 'KQO', 'QQ', 'QJS', 'QTS', 'Q9S', 'Q8S',
        'Q7S', 'Q6S', 'Q5S', 'Q4S', 'Q3S', 'Q2S'],
    ['AJO', 'KJO', 'QJO', 'JJ', 'JTS', 'J9S', 'J8S',
        'J7S', 'J6S', 'J5S', 'J4S', 'J3S', 'J2S'],
    ['ATO', 'KTO', 'QTO', 'JTO', 'TT', 'T9S', 'T8S',
        'T7S', 'T6S', 'T5S', 'T4S', 'T3S', 'T2S'],
    ['A9O', 'K9O', 'Q9O', 'J9O', 'T9O', '99', '98S',
        '97S', '96S', '95S', '94S', '93S', '92S'],
    ['A8O', 'K8O', 'Q8O', 'J8O', 'T8O', '98O', '88',
        '87S', '86S', '85S', '84S', '83S', '82S'],
    ['A7O', 'K7O', 'Q7O', 'J7O', 'T7O', '97O', '87O',
        '77', '76S', '75S', '74S', '73S', '72S'],
    ['A6O', 'K6O', 'Q6O', 'J6O', 'T6O', '96O', '86O',
        '76O', '66', '65S', '64S', '63S', '62S'],
    ['A5O', 'K5O', 'Q5O', 'J5O', 'T5O', '95O', '85O',
        '75O', '65O', '55', '54S', '53S', '52S'],
    ['A4O', 'K4O', 'Q4O', 'J4O', 'T4O', '94O', '84O',
        '74O', '64O', '54O', '44', '43S', '42S'],
    ['A3O', 'K3O', 'Q3O', 'J3O', 'T3O', '93O', '83O',
        '73O', '63O', '53O', '43O', '33', '32S'],
    ['A2O', 'K2O', 'Q2O', 'J2O', 'T2O', '92O', '82O',
        '72O', '62O', '52O', '42O', '32O', '22']
], dtype=str)

'''
Posiciones ordenadas en accion despues de apuesta minimas
'''

posiciones = ['UTG', 'UTG+1', 'MP1', 'MP2', 'HJ', 'CO', 'BTN', 'SB', 'BB']

'''
estados del juego antes de apostar en el preflop
'''
estado = ['Open Raise','Raise over limpers', '3BET/CALL',
          'CALL VS OPEN-PUSH', 'SQUEEZE/CALL', 'COLD4BET/FARHA']

# metodos


# revisar que mano ingresada existe
def check_hand(hand):
    for row in hands:
        if hand.upper() in row:
            return True
    return False


# determinar tipo de posicion
def determinar_posicion(posicion):
    posicion = posicion.upper()
    if posicion.upper() in posiciones[:3]:
        return "Temprana"
    elif posicion in posiciones[3:5]:
        return "Media"
    elif posicion in posiciones[5:]:
        return "Tardia"
    else:
        return "Posición inválida"


# convertir csv a matrix
def csv_to_matrix(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = []
        for row in reader:
            data.append(row)
    return np.array(data, dtype=str)


def AccionBaseMano(hand, matriz_Acciones):

    posicion = np.argwhere(hands == hand.upper())[0]
    return matriz_Acciones[posicion[0], posicion[1]]


def OpenRaisePosicion(posicion):
    posicion=posicion.upper()
    switcher = {
        'UTG': sb_OpenRaise_UTG,
        'UTG+1': sb_OpenRaise_UTG1,
        'MP1': sb_OpenRaise_MP1,
        'MP2': sb_OpenRaise_MP2,
        'HJ': sb_OpenRaise_HJ,
        'CO': sb_OpenRaise_CO,
        'BTN': sb_OpenRaise_BTN,
        'SB': sb_OpenRaise_SB,
        'BB': sb_OpenRaise_BB,
    }
    return switcher.get(posicion, None)

# main

# cargar csv
sb_OpenRaise_UTG = csv_to_matrix('openraise_UTG.csv')
sb_OpenRaise_UTG1 = csv_to_matrix('openraise_UTG+1.csv')
sb_OpenRaise_MP1 = csv_to_matrix('openraise_MP1.csv')
sb_OpenRaise_MP2 = csv_to_matrix('openraise_MP2.csv')
sb_OpenRaise_HJ = csv_to_matrix('openraise_HJ.csv')
sb_OpenRaise_CO = csv_to_matrix('openraise_CO.csv')
sb_OpenRaise_BTN = csv_to_matrix('openraise_BTN.csv')
sb_OpenRaise_SB = csv_to_matrix('openraise_SB.csv')
sb_OpenRaise_BB = csv_to_matrix('openraise_BB.csv')


