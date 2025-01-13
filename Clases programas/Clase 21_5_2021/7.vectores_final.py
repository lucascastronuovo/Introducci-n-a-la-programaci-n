'''
- Realizar una funcion que devuelva un vector de n elementos de valores ingresados, n es el parametro de la funcion
- Utilizando la funcion antes realizada, cargar 2 vectores donde la cantidad de elementos se cargan por teclado.
- Intercalar ambos vectores: [1,2,3] y [4,5,6,7] intercalado [1,4,2,5,3,6,7]
(Aclaracion, pueden ser de distinto tamaño)
'''



def devolver_vector(n):
    v = []

    for i in range(n):
        val = int(input("Ingrese un número: "))

        v.append(val)

    return v
        

def intercalacion(v1, v2):
    

    tamaño_vector = len(v1) + len(v2)

    v_i = [0] * tamaño_vector

    a = 0

    b = 0

    for i in range(tamaño_vector):
        
        if i == 0:
            v_i[i] = v1[a]
            a += 1    
        elif i % 2 != 0:
            v_i[i] = v2[b]
            b += 1
        elif i % 2 == 0:
            v_i[i] = v1[a]
            a += 1

    return v_i






def main():
    

    print("Vector 1:")
    vector_1 = devolver_vector(int(input("Tamaño del vector: ")))
    print()

    print("Vector 2:")
    vector_2 = devolver_vector(int(input("Tamaño del vector: ")))
    print()

    vector_intercalado = intercalacion(vector_1, vector_2)

    print(vector_1)
    print(vector_2)
    print(vector_intercalado)

    


main()