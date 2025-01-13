#Ingresar un número por teclado y determinar si es positivo, negativo o igual a 0


num = int(input("Ingrese un número: "))

"""
if num > 0:
    print("El número es positivo")
else:
    print("El número es negativo")
"""

#Si quiero agregar una condición si el número es igual a 0

"""
if num > 0:
    print("El número es positivo")
else:
    print("El número es negativo")

if num == 0:
    print("El número es 0")

Funciona pero no es lo más correcto
"""

if num > 0:
    print("El número es positivo")
elif num == 0:
    print("El número es 0")
else:
    print("El número es negativo")