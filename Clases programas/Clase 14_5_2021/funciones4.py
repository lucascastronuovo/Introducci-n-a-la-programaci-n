""" Escribir una función que reciba por parámetro la cantidad de notas que se van a ingresar por
parámetro y luego pida ingresar las notas de alumnos y retorne el promedio"""

def notas_alumnos(cantidad_alumnos):

    suma_notas = 0

    cantidad_notas = 0

    for i in range(cantidad_alumnos):
        
        notas = int(input("nota  "))

        suma_notas += notas

        cantidad_notas += 1

    if cantidad_notas > 1:
    
        promedio = suma_notas / cantidad_notas
    else:
        promedio = "no hubo alumnos"

    return promedio

cantidad_alumnos = int(input("cantidad alumnos  "))
promedio_notas = notas_alumnos(cantidad_alumnos)

print(f"{promedio_notas}")


def calcular_promedio(cantidad):
    suma_notas = 0
    for i in range(cantidad):
        nota = int(input("Ingrese la nota:"))
        suma_notas += nota
    promedio = suma_notas / cantidad
    return promedio

resultado = calcular_promedio(10)
print ("el promedio es:", resultado)

def calcular_promedio(cant_notas):
    
    sumnotas = 0
    for i in range(cant_notas):
        nota = float(input('Ingrese la nota'))
        sumnotas += nota
    promedio = sumnotas/cant_notas
    return promedio

cant_notas = int(input('Ingrese la cantidad de notas: '))
prom_notas = calcular_promedio(cant_notas)
print(prom_notas)


def promedio_notas(cantidad):
    notas = 0
    nota = 0
    for n in range (cantidad):
        nota = int(input("Ingrese otra nota"))
        notas += nota     
    promedio = notas / cantidad
    return (promedio)
promedio = promedio_notas(10)
print ("El promedio es", promedio)

def promedio_notas(cantidad):

    suma = 0

    for i in range(1, cantidad + 1):

        x = int(input("nota:  "))

        if x > -1:

            suma += x

    promedio = suma / i

    return promedio

cantidad = int(input("cantidad de notas:   "))

resultado = promedio_notas(cantidad)
print(resultado)


def promedio_notas(cantidad):
    notas = 0
    nota = 0
    for n in range (cantidad):
        nota = int(input("Ingrese otra nota"))
        notas += nota     
    promedio = notas / cantidad
    return (promedio)
promedio = promedio_notas(10)
print ("El promedio es", promedio)

