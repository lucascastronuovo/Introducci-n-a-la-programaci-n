def sumatoria_multiplos_3(cantidad):
    sumatoria = 0
    for n in range (cantidad):
        valor = int(input ("Ingrese un valor"))
        if valor % 3 == 0:
            sumatoria += valor
    if sumatoria >= 20:
        return sumatoria
    else:
        return -1
suma = sumatoria_multiplos_3(5)
print ("La suma es", suma)