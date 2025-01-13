# Definir una funcion que invierta el arreglo recibido por parametro dentro de un rango tambien
#  recibido por parametro

# [1,2,3,4,5] -> [5,4,3,2,1]



def validacion(numero): #Preguntar lo de la validación
    while not numero >= 0:
        numero = int(input("Ingrese un valor positivo: "))

    return numero    



def creando_vector(longitud):
    v = []
    for i in range(longitud):
        valor = int(input("Ingrese un valor: "))
        v.append(valor)

    return v


def invertir (vector,desde,hasta):

    rango = hasta - desde

    for i in range(desde - 1, hasta // 2):
        for n in range(rango):
            j = hasta -1 - n

        #swap

        aux = vector[j]
        vector [j] = vector [i]
        vector [i] = aux



def main():
    longitud = int(input("Ingrese la longitud del arreglo: "))
    longitud = validacion(longitud)

    rango_a_invertir_desde = int(input("Rango a invertir desde:"))
    rango_a_invertir_desde = validacion(rango_a_invertir_desde)
    rango_a_invertir_hasta = int(input("Rango a invertir hasta: "))
    rango_a_invertir_hasta = validacion(rango_a_invertir_hasta)




    vector = creando_vector(longitud)

    print(vector)


    invertir(vector, rango_a_invertir_desde, rango_a_invertir_hasta)

    print(vector)


main ()