# 3) Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.

cantpos = 0

try:
    while True:
        num = int(input("Ingrese un número: "))
        if num != 0:
            if num > 0:
                cantpos = cantpos + 1
                continue
            else:
                continue
        else:
            break
    
    print("Cantidad de números positivos:", cantpos)

except:
    print("Error")
