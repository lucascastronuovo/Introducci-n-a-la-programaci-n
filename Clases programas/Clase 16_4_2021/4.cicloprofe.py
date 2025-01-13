"""
Dado un numero entero, calcular el mismo numero invertido:
por ejemplo: 
  123   ---   321
  12345  ---  54321
"""

numero = int(input("Ingrese un numero: "))

resto = numero % 10
numero = numero // 10
invertido = 0

while numero != 0:
    invertido = invertido * 10 + resto

    resto = numero % 10
    numero = numero // 10

invertido = invertido * 10 + resto

print(invertido)
