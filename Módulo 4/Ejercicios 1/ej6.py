#Ingresar un número. Si es positivo, calcular su raíz cuadrada, si es negativo mostrar su cuadrado y si es cero mostrar “Error. Ha ingresado un valor nulo”.
try:
    numero = int(input("Ingrese un número: "))

    if numero > 0:
        a = pow(numero,1/2)
        print("Raíz Cuadrada de", numero ,"es:", a)
    elif numero == 0:
        print("Error. Ha ingresado un valor nulo")
    else:
        a =  pow(numero,2)
        print("El Cuadrado de", numero, "es:", a)

except:
    print("Error")