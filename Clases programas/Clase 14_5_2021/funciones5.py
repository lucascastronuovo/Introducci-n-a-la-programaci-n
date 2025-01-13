""" Generar una funcion que reciba la cantidad de valores a ingresar.  
    Calcular y retornar el mínimo de los valores ingresados"""

def minimos(cantidad_numeros_ingresados):

    #numero_minimo = 10000

    for i in range(cantidad_numeros_ingresados):

        numero = int(input("Ingrese numero: ")) #Que se ingresen numeros menores a 10000

        if i == 0:
            numero_minimo = numero

        if numero <= numero_minimo:
            numero_minimo = numero
      
    return numero_minimo


resultado_final = minimos(5)
print ("El numero minimo es %d" %resultado_final)

def minimos(cantidad_numeros_ingresados):

    numero_minimo = numero = int(input("Ingrese numero: "))

    for i in range(cantidad_numeros_ingresados-1):

        numero = int(input("Ingrese numero: ")) #Que se ingresen numeros menores a 10000

        if numero <= numero_minimo:
            numero_minimo = numero
      
    return numero_minimo


resultado_final = minimos(5)
print ("El numero minimo es %d" %resultado_final)


"""

for i in range(cantidad_numeros_ingresados):

        numero = int(input("Ingrese numero: ")) #Que se ingresen numeros menores a 10000

        if i == 0:
            numero_minimo = numero
            numero_maximo = numero

        if numero <= numero_minimo:
            numero_minimo = numero
        if numero > numero_maximo:
            numero_maximo = numero    
      
    return numero_minimo

"""