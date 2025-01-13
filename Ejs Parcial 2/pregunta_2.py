

def cargar_datos (v):
    longitud = int(input("Longitud del vector: "))

    while not longitud > 0:
        longitud = int(input("Longitud del vector: "))


    for i in range(longitud):

        num = int(input("Numero: "))

        v.append(num)


def promedio(vector):
    suma = 0

    contador = 0

    for i in range(len(vector)):
        suma += vector[i]

        contador += 1




    if contador > 0:
        promedio = suma / contador
    else:
        promedio = "Error"

    
    return promedio


def cargar_nums_menor_promedio(v_o, v_m_prom, prom):
    for i in range(len(v_o)):
        if v_o[i] < prom:
            v_m_prom.append(v_o[i])




def main ():
    vector_original = []

    vector_menor_promedio = []

    cargar_datos(vector_original)

    print("Vector original:", vector_original)

    promedio_v_o = promedio(vector_original)

    print("El promedio del vector original es:", promedio_v_o)

    cargar_nums_menor_promedio(vector_original, vector_menor_promedio, promedio_v_o)

    print("Vector menor promedio:", vector_menor_promedio)

    
main()