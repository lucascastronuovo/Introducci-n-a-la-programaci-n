"""
7) Leer dos números, mostrar el siguiente Menú pudiendo seleccionar alguna opción y 
repetir esta operación hasta que seleccione 5.
 Menú principal
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
 Seleccione una opción:
"""

try:
    a = int(input("Ingrese número 'a': "))
    b = int(input("Ingrese número 'b': "))
    print("------------------------------------------")
    while True:
        print("Menu principal: ")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Divir")
        print("5. Salir")
        print("---")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            suma = (a + b)
            print("Suma:", suma)
        elif opcion == 2:
            resta = (a - b)
            print("Resta:", resta)
        elif opcion == 3:
            multiplicacion = (a * b)
            print("Multiplicación:", multiplicacion)
        elif opcion == 4:
            division = (a / b)
            print("División:", division)
        elif opcion == 5:
            print("Salir")
            break
        else:
            print("Error")
        
        print("------------------------------------------")
except:
    print("Error")