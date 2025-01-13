""" Escribir una función que pida ingresar notas de alumnos hasta que se ingrese un -1 
y retorne el promedio
"""


def notas_de_alumnos():

    alumnos = 0

    notas_acumuladas = 0

    nota = int(input("Ingrese la nota del alumno (-1 para calcular el promedio de las notas registradas): "))
    while not (nota >= -1 and nota <= 10 and nota != 0):
        nota = int(input("Ingrese la nota del alumno (-1 para calcular el promedio de las notas registradas): "))

    

    while nota != -1:
        notas_acumuladas += nota

        alumnos += 1
     


        nota = int(input("Ingrese la nota del alumno (-1 para calcular el promedio de las notas registradas): "))
        while not (nota >= -1 and nota <= 10 and nota != 0):
            nota = int(input("Ingrese la nota del alumno (-1 para calcular el promedio de las notas registradas): "))


           
    if alumnos != 0:
        promedio = notas_acumuladas / alumnos
    else:
       promedio = "Error"

    return promedio

promedio_cod_principal = notas_de_alumnos()

print(promedio_cod_principal)
    


    



 
    
    
  






