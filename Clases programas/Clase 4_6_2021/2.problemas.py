'''
Se necesita un programa el cual registre los consumos de gas de un 
edificio y poder liquidar las expensas. Para ello, se ingresan los 
consumos de los N departamentos (N ingresado por teclado). 
Ademas de los consumos se ingresan los nombres de los propietarios y los metros cuadrados del depto.

El administrador necesita saber:

a) Promedio de consumo.
b) El departamento (indice) que tuvo mayor consumo.
c) Cuantos departamentos estan por debajo del promedio.
d) Cual propietario registra el menor consumo.
e) Cual es el promedio por metro cuadrado del consumo. (suma mtros cuadrados / suma consumos)

f) Listar los datos ordenados por nombre.
g) De los departamentos que el consumo supere el promedio, listarlos ordenados por consumo.
a
'''

def cargar_datos(consumos, nombres, metros2):
    for i in range(len(consumos)):
        consumos[i] = float(input(f'Ingrese el consumo del departamento {i}: '))
        nombres[i] = input(f'Ingrese el nombre del prop. del dpto. {i}: ')
        metros2[i] = float(input(f'Ingrese los metros cuadr. del departamento {i}: '))

def calcular_promedio(vector):
    suma = 0
    for elem in vector:
        suma += elem

    return suma / len(vector)

def buscar_mayor_consumo(consumos):
    pos_maximo = 0
    for i in range(len(consumos)):
        if consumos[pos_maximo] < consumos[i]:
            pos_maximo = i
    
    return pos_maximo

def buscar_pos_menor(arreglo):
    pos_minimo = 0
    for i in range(len(arreglo)):
        if arreglo[pos_minimo] > arreglo[i]:
            pos_minimo = i
    
    return pos_minimo

def contar_dptos_bajo_promedio(consumos):
    cantidad = 0
    promedio = calcular_promedio(consumos)
    for consumo in consumos:
        if consumo < promedio:
            cantidad += 1

    return cantidad

def buscar_prop_menor_consumo(consumos, nombres):
    pos_menor_consumo = buscar_pos_menor(consumos)
    return nombres[pos_menor_consumo]



cantidad_dptos = int(input('Ingrese la cantidad de departamentos: '))

consumos = [0] * cantidad_dptos
nombres = [''] * cantidad_dptos
metros2 = [0] * cantidad_dptos

cargar_datos(consumos, nombres, metros2)
promedio_consumo = calcular_promedio(consumos)
dpto_mayor_consumo = buscar_mayor_consumo(consumos)
cantidad_dpto_bajo = contar_dptos_bajo_promedio(consumos)
prop_menor = buscar_prop_menor_consumo(consumos, nombres)

suma_consumos = 0
suma_metros2 = 0
for i in range(len(consumos)):
    suma_consumos += consumos[i]
    suma_metros2 += metros2[i]

consumo_metro2 = suma_consumos / suma_metros2


