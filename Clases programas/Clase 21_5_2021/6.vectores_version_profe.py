'''
Leer números enteros mientras sean mayor cero. Con esos números generar un único vector
 en la medida que se cargan donde las 5 primeras posiciones tengan los pares ingresados
 y las 5 siguientes los impares. Si se cargan más números de la paridad necesaria, se
 descartan. Mostrar el vector. Mostrar mayor numero ingresado.

[P,P,P,P,P,I,I,I,I,I]

'''

numeros = [0] * 10
print(numeros)

indice_pares = 0
indice_impares = 5

numero = int(input('Ingrese un numero: '))
mayor = numero
while numero > 0:

    if numero % 2 == 0 and indice_pares < 5:
        numeros[indice_pares] = numero
        indice_pares += 1
    elif numero % 2 != 0 and indice_impares < 10:
        numeros[indice_impares] = numero
        indice_impares += 1

    if mayor < numero:
        mayor = numero

    print(numeros, indice_pares, indice_impares)

    numero = int(input('Ingrese un numero: '))

print(numeros)
print(mayor)