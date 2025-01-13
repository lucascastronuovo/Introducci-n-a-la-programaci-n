'''
- Realizar una funcion que devuelva un vector de n elementos de valores ingresados, n es el parametro de la funcion
- Utilizando la funcion antes realizada, cargar 2 vectores donde la cantidad de elementos se cargan por teclado.
- Intercalar ambos vectores: [1,2,3] y [4,5,6,7] intercalado [1,4,2,5,3,6,7]
(Aclaracion, pueden ser de distinto tamaño)
'''

def leer_positivo():
    numero = int(input('Ingrese un numero positivo: '))
    while numero <= 0:
        numero = int(input('Ingrese un numero positivo: '))

    return numero

def cargar_vector(longitud):
    vector = [0] * longitud

    for i in range(longitud):
        vector[i] = int(input(f'Ingrese el elemento {i}: '))

    return vector

# [1,2,3] y [4,5,6,7] intercalado [1,4,2,5,3,6,7]
def intercalar_vectores(vector1, vector2):
    resultado = [0] * (len(vector1) + len(vector2))

    if len(vector1) < len(vector2):
        vector_corto = vector1
        vector_largo = vector2
    else:
        vector_corto = vector2
        vector_largo = vector1


    indice = 0
    for i in range(len(vector_corto)):
        resultado[indice] = vector1[i]
        indice +=1

        resultado[indice] = vector2[i]
        indice +=1

    for i in range(len(vector_corto), len(vector_largo)):
        resultado[indice] = vector_largo[i]
        indice +=1

    return resultado


n1 = leer_positivo()
n2 = leer_positivo()

v1 = cargar_vector(n1)
v2 = cargar_vector(n2)

intercalado = intercalar_vectores(v1, v2)

print(v1)
print(v2)
print(intercalado)
