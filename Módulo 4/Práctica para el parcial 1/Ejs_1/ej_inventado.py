"""
Crear un programa en donde te indique ingresar dos números enteros, luego te tiene que ofrecer para cada número entero
si se desea mostrar tal cual lo ingresaste o si se desea invertirlo. Luego de indicar estas cosas
se mostrará la suma

"""

num1 = int(input("Ingresar primer número: "))


invertido_preg1 = input("¿Quieres invertir el número? (Responde por SI o por NO): ")

while not (invertido_preg1 == "SI" or invertido_preg1 == "NO"):
    invertido_preg1 = input("¿Quieres invertir el número? (Responde por SI o por NO): ")




num2 = int(input("Ingresar segundo número: "))

invertido_preg2 = input("¿Quieres invertir el número? (Responde por SI o por NO): ")

while not (invertido_preg2 == "SI" or invertido_preg2 == "NO"):
    invertido_preg2 = input("¿Quieres invertir el número? (Responde por SI o por NO): ")



if invertido_preg1 == "SI":
    resto1 = num1  % 10
    num1 = num1 // 10

    invertido1 = 0

    while num1 != 0:
        invertido1 = invertido1 * 10 + resto1

        resto1 = num1  % 10
        num1 = num1 // 10

    invertido1 = invertido1 * 10 + resto1

    num1 = invertido1
    

if invertido_preg2 == "SI":
    resto2 = num2  % 10
    num2 = num2 // 10

    invertido2 = 0

    while num2 != 0:
        invertido2 = invertido2 * 10 + resto2

        resto2 = num2  % 10
        num2 = num2 // 10

    invertido2 = invertido2 * 10 + resto2

    num2 = invertido2



suma = num1 + num2

print("Suma:", suma)













