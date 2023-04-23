from cProfile import label
import random
import matplotlib.pyplot as plt
import numpy as np

print('Diagramas de Linea')
x1 = [3, 4, 5, 6]
y1 = [5, 6, 3, 4]
x2 = [2, 5, 8]
y2 = [3, 4, 3]

plt.plot(x1, y1, label='Linea 1', linewidth=4, color='blue')
plt.plot(x2, y2, label='Linea 2', linewidth=4, color='green')
plt.title('Diagrama de Lineas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.legend()
plt.grid()
plt.show()
print()

print('Diagrama de Barras')
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10, 55, 80, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]
plt.bar(x1, y1, label='Datos 1', width=0.5, color='lightblue')
plt.bar(x2, y2, label='Datos 2', width=0.5, color='purple')
plt.title('Grafico de barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.legend()
plt.show()
print()

print('Histograma')
a = []
for i in range(60):
    a.append(random.randint(0, 120))
b = list(range(0, 121, 10))
plt.hist(a, b, histtype='bar', rwidth=0.8, color='green')
plt.title('Histogramas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.show()
print()

print('Graficos de dispersion')
x1 = np.arange(0.25, 4.26, 1)
y1 = np.random.randint(0, 81, size=len(x1))
x2 = np.arange(0.75, 4.76, 1)
y2 = np.random.randint(0, 81, size=len(x2))
plt.scatter(x1, y1, label='Datos 1', color='red')
plt.scatter(x2, y2, label='Datos 2', color='blue')
plt.title('Grafico de dispersion')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.legend()
plt.show()
print()

print('Graficos Circular')
""" Dormir = np.random.randint(1, 12, size=5)
comer = np.random.randint(1, 12, size=5)
trabajar = np.random.randint(1, 12, size=5)
recreacion = np.random.randint(1, 12, size=5) """
divisiones =np.random.randint(1, 12, size=4)
actividades=['Dormir','Comer','Trabajar','Recreacion']
colores=['red','blue','yellow','green']
plt.pie(divisiones,labels=actividades,colors=colores
        ,startangle=90
        ,shadow=True
        ,explode=(0.1,0,0,0)
        ,autopct='%1.2f%%')
plt.title('Grafico circular')
plt.show()
print()
