'''
Escribir un algoritmo que encuentre los dos primeros números perfectos.
Un número perfecto es un entero positivo, que es igual a la suma de todos 
los enteros positivos (excluido el mismo) que son divisores del número. 
El primer número perfecto es 6, ya que lo divisores de 6 son 1, 2, 3 y 1 + 2 + 3 = 6
'''

numero = 2
cantidad_perfectos = 0
while cantidad_perfectos < 3:

    suma_divisores = 0
    divisor = 1
    while divisor < numero:
        if numero % divisor == 0:
            suma_divisores += divisor

        divisor += 1

    if suma_divisores == numero:
        cantidad_perfectos += 1
        print(numero)

    numero += 1     # numero = numero + 1


    # 220: la suma de los divisores de 220 es 284
    # 284: la suma de los divisores de 284 es 220