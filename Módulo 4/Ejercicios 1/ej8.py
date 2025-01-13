#Ingresar dos números, calcular y mostrar el cociente del primero por el segundo, siempre que el divisor no sea cero. En este último caso mostrar la leyenda “no se puede realizar el cociente”. 

try:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))

    if num2 != 0:
      cociente = num1 / num2
      print("Cociente:", cociente)
    else:
        print("No se puede realizar el cociente")
    

except:
    print("Error")