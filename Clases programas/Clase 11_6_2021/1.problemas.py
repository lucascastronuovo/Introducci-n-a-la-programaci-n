'''
a) Cargar un arreglo de 15 elementos con las medidas del ancho de 15 terrenos
rectangulares.
b) Cargar otro arreglo de 15 elementos con las medidas del fondo de los terrenos.
c) Hallar el arreglo superficie. Mostrarlo ordenado.
d) Hallar cuál es el ancho correspondiente al terreno de mayor fondo.

'''

def obtener_vector(longitud, leyenda):
    vector = [0] * longitud
    for i in range(longitud):
        nro = int(input(leyenda))
        vector[i] = nro
    return vector


def obtener_vector_v2(longitud, leyenda):
    vector = []
    for i in range(longitud):
        nro = int(input(leyenda))
        vector.append(nro)
    return vector


def calculo_superficie(vector1, vector2):
    vector_resultante = []
    for i  in range(len(vector1)):
        sup = vector1[i] * vector2[i]
        vector_resultante.append(sup)

    return vector_resultante

def swap(vector, i, j):
    aux = vector[i]
    vector[i] = vector[j]
    vector[j] = aux

def ordenar (vector, anchos, largos):
    for i in range(len(vector)-1):
        for j in range(i+1, len(vector)):
            if vector[i] > vector[j]:
                swap(vector, i, j)
                swap(anchos, i, j)
                swap(largos, i, j)

    return vector


def mostrar(ancho, largo, superficies):
    for i in range(len(ancho)):
        print(f'Dimension {ancho[i]} x {largo[i]} = {superficies[i]}')

vector_ancho = obtener_vector(5,'Ingrese el ancho: ')
vector_largo = obtener_vector(5, 'Ingrese el largo: ')
superficie = calculo_superficie(vector_largo, vector_ancho)
ordenamiento = ordenar(superficie, vector_ancho, vector_largo)
mostrar(vector_ancho, vector_largo, superficie)
