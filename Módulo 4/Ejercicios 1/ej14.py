#Ingresar un numero de dos cifras, si es mayor que 50 mostrarlo invertido. Sino mostrar la cifra que corresponde a las unidades. 

try:
    numero = int(input("Ingrese un número de dos cifras: "))

    numerostr = str(numero)

    if len(numerostr) == 2:
        if numero > 50:
            numero = numero % 100
            digito1 = numero / 10
            digito2 = numero % 10

            numinv = digito2 * 10 + digito1
            print("Número invertido:", int(numinv))
        else:
            digito2 = numero % 10
            print("Cifra de la unidad:", digito2)
    else:
        print("Escriba un número de dos cifras")

except:
    print("Error")