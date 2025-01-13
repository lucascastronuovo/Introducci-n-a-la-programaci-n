"""
Ingresar las medidas de dos ángulos expresados en grados minutos y 
segundos y hallar la suma. (recordar que los minutos y los segundos no deben 
excederse de 60) 

"""

angulos_ingresados = 1

sumasegundos = 0

sumaminutos = 0

sumagrados = 0

while angulos_ingresados <= 2:
    print("Ángulo %d:" %(angulos_ingresados))

    grados_angulo = int(input("Ingresar los grados del ángulo: "))

    minutos_angulo = int(input("Ingresar los minutos del ángulo: "))
    while not minutos_angulo <= 60:
        minutos_angulo = int(input("Ingresar los minutos del ángulo: "))

    segundos_angulo = int(input("Ingresar los segundos del ángulo: "))
    while not segundos_angulo <= 60:
        segundos_angulo = int(input("Ingresar los segundos del ángulo: "))

    
    if angulos_ingresados == 1:
        grados_angulo1 = grados_angulo
        minutos_angulo1 = minutos_angulo
        segundos_angulo1 = segundos_angulo
    else:
        grados_angulo2 = grados_angulo
        minutos_angulo2 = minutos_angulo
        segundos_angulo2 = segundos_angulo

    angulos_ingresados += 1



sumasegundos = (segundos_angulo1 + segundos_angulo2)

if sumasegundos > 60:
    sumasegundos -= 60
    sumaminutos += 1


sumaminutos += (minutos_angulo1 + minutos_angulo2)

if sumaminutos > 60:
    sumaminutos -= 60 
    sumagrados += 1



sumagrados += (grados_angulo1 + grados_angulo2)


print("La suma de los ángulos da como resultado: %d° %d\' %d\"" %(sumagrados, sumaminutos, sumasegundos))








    
    
