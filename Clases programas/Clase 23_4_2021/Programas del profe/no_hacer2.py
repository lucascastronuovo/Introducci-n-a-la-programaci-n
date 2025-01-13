# Variables del FLAG o Bandera

# NO UTILIZAR!!!

bandera = 0
while bandera == 0:

    numero = int(input("numero:"))
    if numero % 2 == 0:
        bandera = 1


# Forma correcta

numero = int(input("numero:"))
while numero % 2 != 0:
    numero = int(input("numero:"))

