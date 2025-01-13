# Definir una funcion que invierta el arreglo recibido por parametro
# [1,2,3,4,5] -> [5,4,3,2,1]

import random

random.seed(0)

# Extra
def generar_vector(longitud):
    v = [0] * longitud

    for i in range(longitud):
        v[i] = random.randrange(50)   # Numeros entre 0 y 49

    return v


def invertir_vector(vector):
    for i in range(len(vector) // 2):
        j = len(vector) - 1 - i

        aux = vector[j]       # swap
        vector[j] = vector[i]
        vector[i] = aux


uno = generar_vector(10)
print(uno)

invertir_vector(uno)
print(uno)