"""Generar una funcion que pida el ingreso de N números y retorne la sumatoria de los numeros multiplos 
de 3 si da más de 20 o -1 en otro caso"""

numeros_cantidad=int(input("Cantidad de numeros a ingresar"))
def sumatoria_multiplos(numeros_cantidad):
    multiplos=0
    suma=0
    for i in range(numeros_cantidad):
        numero= int(input("Cantidad de numeros a ingresar"))
        multiplos= numero / 3
        if multiplos == 0:
            suma = suma + multiplos
        elif suma >= 20:
            print("1")
        else:
            print("-1")
suma=sumatoria_multiplos(numeros_cantidad)


def sumatoria_3(n):

    suma = 0

    for i in range(n):

        n = int(input("valor:  "))

        if n%3 == 0:
            suma += n

    if suma > 20:
        return suma

    elif suma < 20:
        return -1

n = int(input("cantidad de numeros:  "))

resultado = sumatoria_3(n)
print(resultado)


def sumatoria_multiplos(numeros_cantidad):
    multiplos=0
    suma=0
    for i in range(numeros_cantidad):
        numero= int(input("Cantidad de numeros a ingresar"))
        multiplos= numero / 3
        if multiplos == 0:
            suma = suma + multiplos
        if suma >= 20:
            return suma
        else:
            return -1 

numeros_cantidad=int(input("Cantidad de numeros a ingresar"))        
suma=sumatoria_multiplos(numeros_cantidad)

def suma_multiplos_3(cantidad_numeros):

    suma_3 = 0

    for i in range(cantidad_numeros):

        numero = int(input("numero   "))

        div_3 = numero % 3

        if div_3 == 0:
            
            suma_3 += numero
           

    if suma_3 < 20:
        return -1
    else:
        return suma_3

cantidad_numeros = int(input("cantidad de numeros  "))

suma = suma_multiplos_3(cantidad_numeros)

print(suma)


    


cantidad_numeros = int(input("cantidad de numeros  "))

suma = suma_multiplos_3(cantidad_numeros)

print(suma)

def sumatoria_multiplos_3(cantidad):
    sumatoria = 0
    for n in range (cantidad):
        valor = int(input ("Ingrese un valor"))
        if valor % 3 == 0:
            sumatoria += valor
    if sumatoria >= 20:
        return sumatoria
    else:
        return -1
suma = sumatoria_multiplos_3 (5)
print ("La suma es", suma)
