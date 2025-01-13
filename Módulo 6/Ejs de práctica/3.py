"""
Diseñar una función que calcule el triple de un número y otra función que calcule el
siguiente de un número. Utilizar las funciones en un programa para que ingresado
un numero muestre el consecutivo del triple del número y el triple del consecutivo del
número.

"""

def triple (num):
    triple = num * 3

    return triple


def consec (num):
    consec = num + 1

    return consec


def consec_triple_num():
    numero = int(input("Número consec_triple: "))

    resultado = consec(triple(numero))

    return resultado


def triple_consec_num():
    numero = int(input("Número triple_consec: "))

    resultado = triple(consec(numero))

    return resultado



print(f"El consecutivo del triple del número es {consec_triple_num()} y el triple del consecutivo del número es {triple_consec_num()}")