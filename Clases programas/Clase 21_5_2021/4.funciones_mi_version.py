'''
Escriba una función conteo(x) que determine la cantidad de términos que deben
sumarse de la serie: 1*2*3 + 2*3*4 + 3*4*5 + 4*5*6+…….
hasta que la suma exceda a un valor x dado. 

50
1*2*3 + 2*3*4 + 3*4*5
6     +  24   +  60
        92
'''


def cant_terminos(valor):
    n = 0
    x = 1
    z = 1
    termino = 0

    while valor > n:
        n = z*x*(x+1)*(x+2)
        n += n
        termino += 1

        x += 1

    return termino



terminos_prin = cant_terminos(int(input("Ingrese un valor: ")))

print(f"Los términos son {terminos_prin}")


