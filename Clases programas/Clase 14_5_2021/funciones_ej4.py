"""
Generar una funcion que pida el ingreso de N números y retorne la sumatoria de los numeros multiplos 
de 3 si da más de 20 o -1 en otro caso

"""

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
