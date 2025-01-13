# PARA IR PENSANDO / HACIENDO

# Desarrollar un programa que solicite el ingreso de un numero entero
# e indique a que decena pertenece dicho numero: primera, segunda, tercera
# cuarta, o mas.

numero = int(input("Ingrese un numero: "))

if numero < 0:
    numero = -1 * numero

if numero < 10:
    print("Primera decena")
elif numero < 20:
    print("Segunda decena")
elif numero < 30:
    print("Tercera decena")
elif numero < 40:
    print("Cuarta decena")
else:
    print("Mas decenas...")