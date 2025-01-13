#Ingreso un vector, imprimo el vector original y luego con una funcion creada por mi invierto el vector e imprimo su valor invertido


def validacion(numero):
    while not numero > 0:
        numero = int(input("Ingrese un valor positivo: "))

    return numero    



def creando_vector(longitud):
    v = []
    for i in range(longitud):
        valor = int(input("Ingrese un valor: "))
        v.append(valor)

    return v


def invertir (vector):

    for i in range(len(vector) // 2):
        j = len(vector) -1 - i

        #swap

        aux = vector[j]
        vector [j] = vector [i]
        vector [i] = aux



def main():
    longitud = int(input("Ingrese la longitud del arreglo: "))
    longitud = validacion(longitud)

    vector = creando_vector(longitud)

    print(vector)


    invertir(vector)

    print(vector)

    




main()