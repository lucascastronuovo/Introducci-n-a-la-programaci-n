""" Escribir una función que calcule el factorial de un numero dado"""

def calcular_factorial(): # Declaracion de la funcion

    numero = int(input("numero  ")) 

    anterior = numero 

    while anterior != 1:

        anterior = anterior - 1

        numero *= anterior 
    
    return numero

factorial = calcular_factorial() # LLamado a la funcion 
print(factorial)
