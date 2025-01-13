'''
Se hace una encuesta en la calle para determinar el poder 
adquisitivo de las personas, para ello se pregunta
- cuando dinero dispone
- el nombre de las personas
- cantidad de integrantes en el grupo familiar
- pedir edades del grupo
Cuando el encuestador se cansa, ingresa en nombre: FIN.
Determinar y mostrar:
- Cual es el mayor importe
- De quien el mayor importe
- El promedio del dinero disponible       ( suma de elementos / cantidad de elementos)
- Que persona tiene el grupo familiar con el promedio de edad mas alto
'''



    



def actualizar_maximo(vector):

    for i in range(10):

        if i == 0:
            maximo = vector[i]
        elif maximo < vector[i]:
            maximo = vector[i]

    return maximo



def promedio(suma, cant, vector):

    if cant > 0:
        prom = suma / cant
    else:
        prom = "Error"


    vector.append(prom)
     


def promedio_din(vector):

    suma = 0

    cantidad = 0

    for i in range(len(vector)):
        suma += vector[i]

        cantidad += 1
    
    if cantidad > 0:
        promedio = suma / cantidad
    else:
        promedio = "Error"

    return promedio




def main():

    nombre = []

    dinero = []

    cant_familiares = []

    promedio_edad_familiar = []

    preg_nombre = input("Nombre: ")
    nombre.append(preg_nombre)

    preg_dinero = int(input("Dinero: "))
    while not preg_dinero > 0:
        preg_dinero = int(input("Dinero: "))
    dinero.append(preg_dinero)

    preg_cant_familiares = int(input("Cuantos familiares son: "))
    while not preg_cant_familiares >= 1:
        preg_cant_familiares = int(input("Cuantos familiares son: "))
    cant_familiares.append(preg_cant_familiares)

    for i in range(1, preg_cant_familiares + 1):
        suma_edades = 0
        print(f"Familiar {i}: ")
        edad = int(input("Edad: "))

        suma_edades += edad


    promedio(suma_edades, preg_cant_familiares, promedio_edad_familiar)    

     
    

    seguir_encuesta = input("Seguir con la encuesta: (SI - NO): ")
    while not (seguir_encuesta == "SI" or seguir_encuesta == "NO"):
        seguir_encuesta = input("Seguir con la encuesta: (SI - NO): ")

    while seguir_encuesta != "NO":

        preg_nombre = input("Nombre: ")
        nombre.append(preg_nombre)

        preg_dinero = int(input("Dinero: "))
        while not preg_dinero > 0:
            preg_dinero = int(input("Dinero: "))
        dinero.append(preg_dinero)

        preg_cant_familiares = int(input("Cuantos familiares son: "))
        while not preg_cant_familiares >= 1:
            preg_cant_familiares = int(input("Cuantos familiares son: "))
        cant_familiares.append(preg_cant_familiares)

        for i in range(1, preg_cant_familiares + 1):
            suma_edades = 0
            print(f"Familiar {i}")
            edad = int(input("Edad: "))

            suma_edades += edad


        promedio(suma_edades, preg_cant_familiares, promedio_edad_familiar)
        
        seguir_encuesta = input("Seguir con la encuesta: (SI - NO): ")
        while not (seguir_encuesta == "SI" or seguir_encuesta == "NO"):
            seguir_encuesta = input("Seguir con la encuesta: (SI - NO): ")


    for i in range(len(dinero)):

        if i == 0:
            mayor_importe = dinero[i]
            persona_mayor_importe = nombre[i]
        elif mayor_importe < dinero[i]:
            mayor_importe = dinero[i]
            persona_mayor_importe = nombre[i]

    promedio_dinero = promedio_din(dinero)

    for i in range(len(promedio_edad_familiar)):

        if i == 0:
            maximo = promedio_edad_familiar[i]
            persona_prom_mayor_edad_f = nombre[i]
        elif maximo < promedio_edad_familiar[i]:
            maximo = promedio_edad_familiar[i]
            persona_prom_mayor_edad_f = nombre[i]

    print()
    print()
    print("Resultados: ")
    print(f"El mayor importe es ${mayor_importe}, y es de {persona_mayor_importe}.")
    print(f"El promedio de dinero disponible es de ${promedio_dinero:.2f}")
    print(f"La familia que tiene el mayor promedio de edad es la de {persona_prom_mayor_edad_f} y es de {maximo} años")

        
main()

  

        
        

        


