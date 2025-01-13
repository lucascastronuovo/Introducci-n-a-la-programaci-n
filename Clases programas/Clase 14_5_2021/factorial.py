"""Pedir un número entero y calcular su factorial. Ejemplo factorial de 5 = 5*4*3*2*1"""


numero = int(input("numero  "))


for i in range(numero-1,1,-1):

    numero *= i 

print(numero)   

####


numero = int(input("numero  ")) 

anterior = numero 

while anterior != 1:

    anterior = anterior - 1

    numero *= anterior 

print(numero)

num = int(input("Ingrese un numero: "))
if num < 0:
    print("No existe")

elif  num == 0:
    print('El factorial es uno')

else :
    for i in range(1,num,):
        num *= i
print(num)


