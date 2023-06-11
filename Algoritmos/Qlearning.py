import gym
from random import randint
import numpy as np
# Crear el entorno MountainCar-v0
env = gym.make('MountainCar-v0')

def discretizar(valor):
    estado=np.array(valor[0][:2])
    low=env.observation_space.low
    high=env.observation_space.high
    aux=((estado-low)/(high-low))*20
    return tuple(aux.astype(np.int32))

q_table = np.random.uniform(low=-1, high=1, size=[20, 20, 3])

tasa_aprendizaje = 0.1
factor_descuento = 0.95
episodios=5000
listados_recompensas=[]
# Ciclo principal

for episodio in range (episodios):
    final = False
    recompensa_total=0
    
    estado =discretizar(env.reset())
    while not final:
        if randint(0,10)>2:
            accion=np.argmax(q_table[estado])
        else:
            accion = randint(0, 2)
        nuevo_estado, recompensa, final, truncated, info = env.step(accion)

        q_table[estado][accion] = q_table[estado][accion] + tasa_aprendizaje * \
            (recompensa + factor_descuento *
            np.max(q_table[discretizar([nuevo_estado])]) - q_table[estado][accion])
        estado=discretizar([nuevo_estado])
        recompensa_total+=recompensa
        # Renderizar el entorno
        if(episodio+1)%500==0:
            env.render()
        
    listados_recompensas.append(recompensa_total)
    if (episodio+1)%100==0:
        print(f"Episodio {episodio+1} - Recompensa: {np.mean(listados_recompensas)}")
    # Cerrar el entorno
env.close() 
