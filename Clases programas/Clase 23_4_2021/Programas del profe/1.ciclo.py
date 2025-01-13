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

# dinero, nombre, cantidad, edades

# Inicializar variables que estan en la condicin del while
nombre = input('Ingrese nombre: ')

dinero_mayor = 0
nombre_dinero_mayor = ''

suma_dinero = 0
personas_encuestadas = 0

promedio_edad_mayor = 0
nombre_promedio_edad = ''

# while CONDICION_LOGICA:
while nombre != 'FIN':
    # [ Leer/Obtener otros datos necesarios ]
    dinero = float(input('Ingrese dinero disponible: '))
    integrantes = int(input('Cantidad de integrantes: '))

    suma_edades = 0
    for i in range(integrantes):
        edad = int(input(f'Ingrese edad del integrante de {nombre} numero {i+1}: '))
        suma_edades += edad

    if integrantes > 0:
        promedio_edades = suma_edades / integrantes
    else:
        promedio_edades = 0
    
    if dinero >= dinero_mayor:
        dinero_mayor = dinero
        nombre_dinero_mayor = nombre

    suma_dinero += dinero
    personas_encuestadas += 1

    if promedio_edades >= promedio_edad_mayor:
        promedio_edad_mayor = promedio_edades
        nombre_promedio_edad = nombre

    # Actualizar las variables que estan en la condicion del while
    nombre = input('Ingrese nombre: ')


if personas_encuestadas > 0:
    promedio_dinero = suma_dinero / personas_encuestadas

    # print('El mayor importe es', dinero_mayor)
    # print('El mayor importe es: ' + str(dinero_mayor))
    # print('El mayor importe es {}'.format(dinero_mayor))

    mensaje = f'El mayor importe es {dinero_mayor:.2f} y fue de {nombre_dinero_mayor}.'
    print(mensaje)

    print(f'El promedio de dinero disponible es {promedio_dinero:.2f}.')

    print(f'La persona con grupo edades mayores promedio es {nombre_promedio_edad}, cuyo promedio es {promedio_edad_mayor:.2f}')

else:
    print('No se encuestaron personas')