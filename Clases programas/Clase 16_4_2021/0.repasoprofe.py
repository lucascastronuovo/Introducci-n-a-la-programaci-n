
numero = float(input("Ingrese un numero real:"))  # Numero real
print(numero)


num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))

if num1 > 0:
    print("Es positivo")

# num1 es mayor si num1 > num2 y num1 > num3
if num1 >= num2 and num1 >= num3:       
    print("El mayor es ", num1)
elif num2 >= num1 and num2 >= num3:
    print("El mayor es ", num2)
elif num3 >= num1 and num3 >= num2:
    print("El mayor es ", num3)
else:
    print("Ninguno es mayor")
    
print("Sigue el programa")

