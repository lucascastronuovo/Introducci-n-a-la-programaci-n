# Cargar un arreglo con 12 números enteros. Mostrarlo y calcular:
#     El elemento máximo y mínimo.
#     Calcular el promedio de los elementos ubicados en posiciones pares.
#     Calcular la sumatoria de los elementos pares en posiciones impares.
#     Calcular la cantidad de numeros primos.


def main():
    v = [0] * 12

    num_par = 0

    for i in range(len(v)):
        v[i] = int(input("Número: "))

        if i == 0:
            maximo = v[i]
            minimo = v[i]
        elif maximo < v[i]:
            maximo = v[i]
        elif minimo > v[i]:
            minimo = v[i]
        

        if i % 2 == 0:
            num_par =+ v[i]

    



    


main()