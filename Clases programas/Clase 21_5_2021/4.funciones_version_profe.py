'''
Escriba una función contar_terminos(x) que determine la cantidad de términos que deben
sumarse de la serie: 1*2*3 + 2*3*4 + 3*4*5 + 4*5*6+…….
hasta que la suma exceda a un valor x dado. 

50
1*2*3 + 2*3*4 + 3*4*5
6     +  24   +  60
        92
'''
def conteo(x):
    cant_terminos = 1

    a = 1
    b = 2
    c = 3

    terminos = a * b * c
    suma_terminos = terminos

    while x > suma_terminos:

        a = b
        b = c
        c += 1

        terminos = a * b * c
        suma_terminos += terminos
        cant_terminos += 1
    
    return cant_terminos

x = int(input("numero  "))
cant_terminos = conteo(x)

print(cant_terminos)


# def contar_terminos(x):
#     cant_terminos = 0
#     suma_terminos = 0
#     n = 1
#     while x > suma_terminos:
#         termino = n * (n+1) * (n+2)
#         suma_terminos += termino
#         cant_terminos += 1
#         n += 1

#     return cant_terminos


# cantidad_terminos = contar_terminos(50)
# print(cantidad_terminos)