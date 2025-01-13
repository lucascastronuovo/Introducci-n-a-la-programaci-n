#6) Ingresar 10 números mayores a 3 y menores a 8. Mostrar el valor ingresado en número y letras.

try:
    numero = 1
    while numero <= 10:
        num = int(input("Ingrese un número mayor a 3 y menor a 8: "))
        if num > 3 and num < 8:
            if num == 4:
                print("Cuatro", num)
            elif num == 5:
                print("Cinco", num)
            elif num == 6:
                print("Seis", num)
            elif num == 7:
                print("Siete", num)
            else:
                print("Error")

        else:
            print("Error")
            continue

        numero = numero + 1


except:
    print("Error")
            

        