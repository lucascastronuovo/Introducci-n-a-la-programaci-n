# Ingresar números hasta un múltiplo de 3. Mostrar el último número ingresado.

try:
    while True:
        num = int(input("Ingrese un número: "))
        if (num % 3 == 0):
            print("El último número ingresado es:", num)
            break
        else:
            continue

except:
    print("Error")


