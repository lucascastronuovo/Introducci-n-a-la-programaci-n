"""
Dado un numero entero, calcular el mismo numero invertido:
por ejemplo: 
  123   ---   321
  12345  ---  54321
"""

def invertir(num):

    resto = num % 10

    num = num // 10

    invertido = 0

    while num != 0:
        invertido = invertido * 10 + resto

        resto = num % 10

        num = num // 10

    
    invertido = invertido * 10 + resto

    return invertido



def main():
    numero = int(input("Número a invertir: "))

    numero_invertido = invertir(numero)

    print(f"El número invertido de {numero} es {numero_invertido}")



main()