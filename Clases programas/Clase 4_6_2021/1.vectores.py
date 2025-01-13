# Cargar un arreglo con 12 números enteros. Mostrarlo y calcular:
#     El elemento máximo y mínimo.
#     Calcular el promedio de los elementos ubicados en posiciones pares.
#     Calcular la sumatoria de los elementos pares en posiciones impares.
#     Calcular la cantidad de numeros primos.

def cargar_arreglo(longitud):
    arreglo = []
    for i in range(longitud):
        numero = int(input('Ingrese un numero: '))
        arreglo.append(numero)

    return arreglo

def buscar_maximo(arreglo):
    maximo = arreglo[0]
    for numero in arreglo:
        if maximo < numero:
            maximo = numero

    return maximo

def buscar_pos_maximo(arreglo):
    pos_maximo = 0
    for i in range(len(arreglo)):
        if arreglo[pos_maximo] < arreglo[i]:
            pos_maximo = i

    return pos_maximo

def buscar_minimo(arreglo):
    minimo = arreglo[0]
    for numero in arreglo:
        if minimo > numero:
            minimo = numero

    return minimo

def calcular_promedio_pos_pares(arreglo):
    suma = 0
    cantidad = 0
    for i in range(len(arreglo)):
        if i % 2 == 0:
            suma = suma + arreglo[i]
            cantidad = cantidad + 1 

    promedio = suma / cantidad
    return promedio

def calcular_suma_pares(arreglo):
    suma = 0
    for i in range(len(arreglo)):
        if i % 2 != 0 and arreglo[i] % 2 == 0:
            suma = suma + arreglo[i]

    return suma

def determinar_primo(numero):
    i = 2
    while numero > 1 and numero % i != 0:    # i no divide a numero
        i += 1

    # Sale del while: i es igual a numero
    # o que i divide a numero y es distinto a numero

    return numero == i    # Es primo cuando numero es igual a i

def calcular_primos(arreglo):
    cantidad = 0

    for numero in arreglo:
        es_primo = determinar_primo(numero)
        if es_primo:
            cantidad += 1

    return cantidad

def calcular_primos_v2(arreglo):
    cant_primos = 0
    
    for i in range(len(arreglo)):
        div = 0
        for j in range(2, arreglo[i]+1):
            if arreglo[i] % j == 0:
                div += 1
        if div == 1:
            cant_primos += 1

    return cant_primos


numeros = cargar_arreglo(12)
maximo = buscar_maximo(numeros)
minimo = buscar_minimo(numeros)
promedio_pos_pares = calcular_promedio_pos_pares(numeros)
sumatoria = calcular_suma_pares(numeros)
cantidad_primos = calcular_primos(numeros)

print('El elemento máximo y mínimo: ', maximo, minimo)
print('Calcular el promedio de los elementos ubicados en posiciones pares: ', promedio_pos_pares)
print('Calcular la sumatoria de los elementos pares en posiciones impares: ', sumatoria)
print('Calcular la cantidad de numeros primos: ', cantidad_primos)
