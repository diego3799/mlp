import numpy as np
from random import randint
# Primero tenemos que pedir el numero de neuronas
print("Numero de neuronas iniciales:")
num_neuronas = int(input())
# Segundo pedimos la cantidad de neuronas intermedias
print("Numero de neuronas intermedias:")
num_intermedias = int(input())
# Los numeros de pesos que necesitamos es el numero de neuranos inicial x neuronas intermedias + neuronas intermedias
num_weight = num_neuronas*num_intermedias+num_intermedias

weights = [[np.random.rand() for i in range(num_intermedias)]
           for i in range(num_neuronas)]

weights += [[np.random.rand() for i in range(num_intermedias)]]


# necesitamos generar un numero N puntos
# con el numero de coordenas igual al numero de entradas iniciales
# junto con un identificador
print("Cuantos puntos aleatorios quieres generar:")
num_puntos = int(input())


conjunto_datos = [[randint(0, 10) for i in range(num_neuronas)]
                  for i in range(num_puntos)]

# Agregamos la identificacion de los puntos
for i in range(num_puntos):
    conjunto_datos[i].append(randint(0, 1))


for i in range(num_puntos):
    # tenemos que multiplicar por el peso de la neurona
    acum = 0
    hidden = []
    # Lo que tenemos que hacer es conseguir el valor de peso de las capas intermedias
    # que es cada uno de los pesos por las entradas
    # despues las entradas
    # for j in range(num_intermedias)
