import tensorflow as tf  #Libreria IA
import numpy as np       #Arreglos numericos
import matplotlib.pyplot as plt

celsius = np.array([-40,-10,0,8,15,22,38,100,50],dtype=float)
fahrenheit =np.array([-40,14,32,46,59,72,100,212,122],dtype=float)

oculta1= tf.keras.layers.Dense(units=3,input_shape=[1])
oculta2= tf.keras.layers.Dense(units=3)
salida=tf.keras.layers.Dense(units=1)
modelo=tf.keras.Sequential([oculta1,oculta2,salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("entrenando...")
historial=modelo.fit(celsius,fahrenheit,epochs=200,verbose=False)
print("FINISHED")

plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

resultado = modelo.predict([60.0])
print("El resultado es "+str(resultado) +"fahrenheit!")

print("Variables internas del modelo")
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())
