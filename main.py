import numpy as np
from random import randint
from sklearn.neural_network import MLPClassifier
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

conjunto_test = [[randint(0, 10) for i in range(num_neuronas)]
                 for i in range(num_puntos)]

objetivos = []
# Agregamos la identificacion de los puntos
for i in range(num_puntos):
    objetivos.append(randint(0, 1))


print("\nPuntos Entrenamiento\n")
print(conjunto_datos)
print("\nObjetivos\n")
print(objetivos)


clf = MLPClassifier(solver='lbfgs', alpha=0.01, activation="logistic", learning_rate="constant", 
                    hidden_layer_sizes=(num_intermedias, ), random_state=1)

clf.fit(conjunto_datos, objetivos)

print("Resultado de prediciones")
print(clf.predict(conjunto_datos))
print("Resultado datos de Prueba")
print(conjunto_test)
print(clf.predict(conjunto_test))
