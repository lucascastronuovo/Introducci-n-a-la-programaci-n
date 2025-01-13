"""
Construir una función que permita devolver el valor absoluto de un número
ingresado por teclado.

"""


def valor_absoluto(num):
    if num > 0:
        print(num)
    elif num < 0:
        num *= -1
        print(num)
    else:
        print("El número ingresado es 0")




valor_absoluto(int(input("Número: ")))