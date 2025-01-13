'''
Leer números enteros mientras sean mayor cero. Con esos números generar un único vector
 en la medida que se cargan donde las 5 primeras posiciones tengan los pares ingresados
 y las 5 siguientes los impares. Si se cargan más números de la paridad necesaria, se
 descartan. Mostrar el vector. Mostrar mayor numero ingresado.

[P,P,P,P,P,I,I,I,I,I]

'''


def cargar_vector(v):

    indice_par = 0

    indice_impar = 5

    num = int(input("Número mayor a cero: "))


    while num > 0:

        
        
        if (num % 2 == 0 and indice_par <= 4):
            v[indice_par] = num
            indice_par += 1
        elif (num % 2 != 0 and indice_impar < 10):
            v[indice_impar] = num
            indice_impar += 1
    
        print(v)

        num = int(input("Número mayor a cero: "))



    for i in range(len(v)):
        if i == 0:
            mayor = v[i]
        elif mayor < v[i]:
            mayor = v[i]

    print("Mayor:",mayor)
        

    
            






def main():

    vector = [0] * 10

    print(vector)

    cargar_vector(vector)

    print(vector)



main()