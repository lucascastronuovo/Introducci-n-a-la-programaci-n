
#Invertir

def invertir(vector):

    for i in range(len(vector)//2):

        j = len(vector) - 1 - i

        #swap
        aux = vector[j]
        vector[j] = vector[i]
        vector[i] = aux



def invertir_rango(vector, desde, hasta):
    a = desde
    b = desde + (hasta - desde + 1) // 2

    for i in range(a, b):

        j = len(vector) - 1 - i

        #swap
        aux = vector[j]
        vector[j] = vector[i]
        vector[i] = aux



def main():
    v = []

    tamaño_v = int(input("Tamaño del vector: "))

    for i in range(tamaño_v):
        valor = int(input("Número: "))

        v.append(valor)

    print(v)

    pregunta = input("Invertir todo (T) o rango (R): ")
    while not (pregunta == "T" or pregunta == "R"):
        pregunta = input("Invertir todo (T) o rango (R): ")

    if pregunta == "T":
        invertir(v)
    else:
        desde = int(input("Desde: "))
        hasta = int(input("Hasta: "))
        invertir_rango(v, desde, hasta)

    print(v)


main()



