#Ingresar un número de tres cifras y mostrar el segundo dígito. 

#Cuando escribo por ej a7s me toma lo que escribí como un int y me imprime el 7.

try:
    numero = input("Ingresa un número de tres cifras: ")

    ndig = len(numero)

    if ndig == 3:

        digito = numero[1]

        digito1 = int(digito) 

        print(digito1)     
    else:
        print("Por favor, ingrese un número de tres cifras")

except:
    print("Error")