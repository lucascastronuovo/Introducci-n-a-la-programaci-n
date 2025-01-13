#5) Leer el número de mes y mostrar cuantos días tiene ese mes (año actual)

try:
    enero = 30
    febrero = 28
    marzo = 31
    abril = 30
    mayo = 31
    junio = 30
    julio = 31
    agosto = 31
    septiembre = 30
    octubre = 31
    noviembre = 30
    diciembre = 31
    mes = int(input("Escribe el número de mes: "))

    if mes > 12 or mes < 0:
        print("Error")
    elif mes == 1:
        print("Enero:", enero)
    elif mes == 2:
        print("Febrero:", febrero)
    elif mes == 3:
        print("Marzo:", marzo)
    elif mes == 4:
        print("Abril:", abril)
    elif mes == 5:
        print("Mayo:", mayo)
    elif mes == 6:
        print("Junio:", junio)
    elif mes == 7:
        print("Julio:", julio)
    elif mes == 8:
        print("Agosto:", agosto)
    elif mes == 9:
        print("Septiembre:", septiembre)
    elif mes == 10:
        print("Octubre:", octubre)
    elif mes == 11:
        print("Noviembre:", noviembre)
    elif mes == 12:
        print("Diciembre:", diciembre)
    else:
        print("Error")
        

except:
    print("Error")