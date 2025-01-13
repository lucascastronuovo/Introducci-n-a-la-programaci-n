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

Nombre_de_mayor_importe = ""

Nombre_familia_mayorpromedad = ""

promedio_edadfam_mayor = 0

cant_personas_encuestadas = 0

suma_importes = 0

sum_edad = 0

mayor_importe = 0

nombre = input("Nombre: ")

while nombre != "FIN":
    poder_adquisitivo = float(input("¿Cuánto dinero dispones?: $"))
    
    while not poder_adquisitivo >= 0:
        poder_adquisitivo = float(input("¿Cuánto dinero dispones?: $"))

    cant_integr_fam = int(input("Cantidad de integrantes en la familia: "))

    while not cant_integr_fam > 0:
         cant_integr_fam = int(input("Cantidad de integrantes en la familia: "))

    for x in range(1,(cant_integr_fam+1)):
        edad = int(input("Edad del %d° integrante: " %(x)))

        while not edad > 0:
            edad = int(input("Edad del %d° integrante: " %(x)))

        sum_edad += edad

    promedio_edadfam = sum_edad / cant_integr_fam

    if promedio_edadfam > promedio_edadfam_mayor:
        promedio_edadfam_mayor = promedio_edadfam
        nombre_familia_mayorpromedad = nombre


    if poder_adquisitivo > mayor_importe:
        mayor_importe = poder_adquisitivo
        nombre_de_mayor_importe = nombre

    suma_importes += poder_adquisitivo

    cant_personas_encuestadas += 1

    nombre = input("Nombre: ")


if cant_personas_encuestadas > 0:
    promedio_dinero_disponible = suma_importes / cant_personas_encuestadas


    print(f"El mayor importe es ${mayor_importe:.2f} y le pertenece a la familia de", nombre_de_mayor_importe)
    print("-")
    print("-")
    print(f"El promedio de dinero disponible es ${promedio_dinero_disponible:.2f}")
    print("-")
    print("-")
    print("La persona que tiene el grupo familiar con el promedio de edad mas alto es %s" %(nombre_familia_mayorpromedad))
    print("-")
    print("-")
else:
    print("No se encontraron personas")


    


