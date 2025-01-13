"""
Construir una función que permite devolver la potencia de un número ingresando el
número y su potencia.

"""

def funcion_numero_potencia():
    numero = int(input("Número: "))
    potencia = float(input("Potencia: "))

    resultado = numero ** potencia

    return resultado




print("Resultado: %d" %(funcion_numero_potencia())) 