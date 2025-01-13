""" Escribir una función que pida ingresar notas de alumnos hasta que se ingrese un -1 
y retorne el promedio"""

def ingresar_notas():

    promedio = 0
    notas = int(input("Ingresar notas: "))

    while notas != -1:
        
        promedio = promedio / notas

        notas = int(input("Ingresar notas: "))

    return promedio 

alumnos = ingresar_notas()


def promedio_notas():
    cantidad = 0
    numnotas = 0
    notas = int(input("Ingrese la nota del alumno: "))

    while notas != -1:
        cantidad += 1
        numnotas += notas
        notas = int(input("Ingrese la nota del alumno: "))
    promedio = numnotas / cantidad
    return promedio


def notas_alumnos():

    notas = int(input("nota  "))

    suma_notas = 0

    cantidad_notas = 0

    while notas  != -1:

        suma_notas += notas

        cantidad_notas += 1

        notas = int(input("nota  "))

    promedio = suma_notas / cantidad_notas
    return promedio

promedio_notas = notas_alumnos()
print(promedio_notas)

def promedio_notas():

    x = int(input("nota:  "))
    contador = 0
    suma = 0

    while x > -1:

        suma += x

        x = int(input("nota:  "))
        
        contador = contador + 1

    promedio = suma / contador
    
    return promedio

x = promedio_notas()
print(x)

def calcular_promedio():
    nota = int(input("Ingrese su calificación (-1 para salir): "))
    contador_notas = 0
    acumulador_notas = 0
    
    while nota > -1 and nota < 11:
        contador_notas += 1
        acumulador_notas += nota
        nota = int(input("Ingrese su calificación (-1 para salir): "))
    
    promedio = acumulador_notas / contador_notas

    return (promedio)

promedio = calcular_promedio()
print(promedio)

def notas_alumnos():
    nota= int(input("Ingrese la nota"))
    suma= 0
    cont= 0
    while nota != -1:
        suma= nota + suma
        cont =+ 1
        nota= "Ingresar nota"
        nota= int(input("Ingrese la nota"))
    promedio = suma/cont  
    return promedio

promedio= notas_alumnos()
print(promedio)


def promedio_notas():
    notas = 0
    nota = 0
    total = 0
    nota = int(input("Ingrese la nota del alumno, -1 para finalizar"))
    while nota != -1:
        notas += nota
        total += 1
        nota = int(input("Ingrese otra nota, -1 para finalizar"))
    promedio = notas / total
    return (promedio)
    
promedio = promedio_notas()
print ("El promedio es", promedio)
