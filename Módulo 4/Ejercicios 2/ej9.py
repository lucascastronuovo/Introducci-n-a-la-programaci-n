#9) Ingresar las temperaturas registradas a distintas horas de un día en grados hasta que ésta sea 100. Mostrar la temperatura máxima y la temperatura mínima.

hora = 2

try:
    print("------")
    print("Hora: 1")
    temp = int(input("Ingrese temperatura registrada: ")) 
    tempmax = temp
    tempmin = temp
    while True:
        print("------")
        print("Hora:", hora)
        temp = int(input("Ingrese temperatura registrada: "))
        if temp == 100:
            break
        elif tempmax < temp:
            tempmax = temp
        elif tempmin > temp:
            tempmin = temp
        
        hora = hora + 1

    print("-----")
    print("Temperatura máxima:", tempmax, "°")
    print("Temperatura mínima:", tempmin, "°")

except:
    print("Error") 