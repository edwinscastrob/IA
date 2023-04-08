

'''
Manos posibles Preflop 
o diferente palo
s mismo palo
'''
hands = ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s', 'AKo', 'AQo', 'AJo', 'ATo', 'A9o', 'A8o', 'A7o', 'A6o', 'A5o', 'A4o', 'A3o', 'A2o', 'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s', 'KQo', 'KJo', 'KTo', 'K9o', 'K8o', 'K7o', 'K6o', 'K5o', 'K4o', 'K3o', 'K2o', 'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s', 'QJo', 'QTo', 'Q9o', 'Q8o', 'Q7o', 'Q6o', 'Q5o', 'Q4o', 'Q3o', 'Q2o', 'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s', 'JTo', 'J9o', 'J8o', 'J7o', 'J6o', 'J5o', 'J4o', 'J3o', 'J2o', 'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s', 'T9o', 'T8o', 'T7o', 'T6o', 'T5o', 'T4o', 'T3o', 'T2o', '98s', '97s', '96s', '95s', '94s', '93s', '92s', '98o', '97o', '96o', '95o', '94o', '93o', '92o', '87s', '86s', '85s', '84s', '83s', '82s', '87o', '86o', '85o', '84o', '83o', '82o']

'''
Posiciones ordenadas en accion despues de apuesta minimas
'''

posiciones = ['UTG', 'UTG+1', 'MP1', 'MP2', 'HJ', 'CO', 'BTN', 'SB', 'BB']

'''
estados del juego antes de apostar en el preflop
'''
estado=['Open Raise', 'Raise over limpers', '3BET/CALL', 'CALL VS OPEN-PUSH', 'SQUEEZE/CALL', 'COLD4BET/FARHA']


#metodos

#revisar que mano ingresada existe
def check_hand(hand):
    return hand.upper() in hands

def determinar_posicion(posicion):
    posicion=posicion.upper()
    if posicion.upper() in posiciones[:3]:
        return "Temprana"
    elif posicion in posiciones[3:5]:
        return "Media"
    elif posicion in posiciones[5:]:
        return "Tardia"
    else:
        return "Posición inválida"







