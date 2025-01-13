'''
Escriba una función contar_terminos(x) que determine la cantidad de términos que deben
sumarse de la serie: 1*2*3 + 2*3*4 + 3*4*5 + 4*5*6+…….
hasta que la suma exceda a un valor x dado. 

50
1*2*3 + 2*3*4 + 3*4*5
6     +  24   +  60
        92
'''


def contar_terminos (x):

    contar = 1

    a = 1
    b = 2
    c = 3

    suma_terminos = a * b * c

    while suma_terminos < x:

        terminos = suma_terminos

        contar += 1

        a = b
        b = c
        c += 1

        terminos = a * b * c

        suma_terminos += terminos

    return contar








def main():
    cant_terminos = contar_terminos(int(input("Ingrese un número: ")))

    print(f"La cantidad de terminos es {cant_terminos}")



main()