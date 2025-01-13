'''
1)	Se ha realizado un relevamiento sobre el procesador de 
   texto más utilizado: número identificatorio (1-Word, 2-LibreWriter y 3-LaTeX), 
   cantidad de documentos creados, tiempo que usan el procesador por día. Se ingresan
    los datos hasta que el identificador sea igual o menor a 0. Calcular y mostrar:

a.	Dado un procesador determinado (ingresado por teclado, al comenzar), cuál es el 
    promedio de documentos creados para ese procesador.

b.  El procesador con mayor tiempo dedicado.
'''

procesador_deseado = int(input('Ingrese procesador deseado (1-Word, 2-LibreWriter y 3-LaTeX, 0-Finalizar): '))
while not (procesador_deseado == 1 or procesador_deseado == 2 or procesador_deseado == 3 or procesador_deseado <= 0):
    procesador_deseado = int(input('Ingrese procesador deseado (1-Word, 2-LibreWriter y 3-LaTeX, 0-Finalizar): '))

suma_documentos = 0
cantidad_procesador = 0

procesador = int(input('Ingrese procesador (1-Word, 2-LibreWriter y 3-LaTeX, 0-Finalizar): '))
while not (procesador <= 3):
    procesador = int(input('Ingrese procesador (1-Word, 2-LibreWriter y 3-LaTeX, <= 0 Finalizar): '))

tiempo_mayor = 0
procesador_tiempo_mayor = 0

while procesador > 0:
    cantidad_documentos = int(input('Cantidad de documentos: '))    # Se podrian validar q sean positivos
    tiempo_uso = float(input('Tiempo de uso: '))

    if procesador == procesador_deseado:
        suma_documentos += cantidad_documentos
        cantidad_procesador += 1

    if tiempo_uso > tiempo_mayor:
        tiempo_mayor = tiempo_uso
        procesador_tiempo_mayor = procesador


    procesador = int(input('Ingrese procesador (1-Word, 2-LibreWriter y 3-LaTeX, 0-Finalizar): '))
    while not (procesador <= 3):
        procesador = int(input('Ingrese procesador (1-Word, 2-LibreWriter y 3-LaTeX, 0-Finalizar): '))


if cantidad_procesador != 0:
    promedio = suma_documentos / cantidad_procesador
    print(promedio)
else:
    print('Sin datos para ese procesador.')

if procesador_tiempo_mayor == 1:
    print('El Word fue el mas usado.')
elif procesador_tiempo_mayor == 2:
    print('El LibreWriter fue el mas usado.')
elif procesador_tiempo_mayor == 3:
    print('El LaTeX fue el mas usado.')
else:
    print('Sin datos para procesar')

# print(f'El procesador {procesador_tiempo_mayor} fue el mas usado')