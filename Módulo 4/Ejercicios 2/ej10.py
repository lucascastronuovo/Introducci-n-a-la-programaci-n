#10) Leer un número y calcular la suma de los números naturales hasta ese número. Modificar el algoritmo para que se pueda procesar muchos números. Dar por terminada la entrada cuando el número sea 0.

#Problema: Me tira Traceback cuando escribo números float (Números con coma)

try:
    suma = 0
    while True:
        num = int(input("Ingrese un número: "))
        if num == 0:
            break
        elif num % 1 == 0 and num > 0:
            suma = suma + num
        else:
            continue
    
    print("Suma calculada:", suma)

except:
    print("Error")