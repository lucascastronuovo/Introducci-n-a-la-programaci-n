"""
Generar una funcion que reciba la cantidad de valores a ingresar.  
Calcular y retornar el mínimo de los valores ingresados
"""

def min_valores(cantidad):

    minimo = 99999999

    for i in range(1, cantidad + 1):
        print(f"Valor {i:}:")
        valor = int(input("Ingresa el valor: "))
        
        if minimo > valor:
            minimo = valor
    
    return minimo


cantidad = int(input("Cantidad de valores a ingresar: "))

minimo_cod_principal = min_valores(cantidad)


print("El mínimo es:", minimo_cod_principal)


#Abajo está el ejercicio de a profesora (Ahí se muestra como se debe hacer con el primer valor del max y el min)

"""
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

""" 


