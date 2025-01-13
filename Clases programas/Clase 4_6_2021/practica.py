
def determinar_primo(numero):
    i = 2

    while numero > 1 and numero % i != 0:
        i += 1

    return numero == i

def calcularprimo(vec):
    cantidad = 0

    for num in vec:
        es_primo = determinar_primo(num)

        if es_primo:
            cantidad += 1

    return cantidad




def invertir(vec):

    for i in range(len(vec)// 2):
        j = len(vec) -1 - i

        #swap

        aux = vec[i]

        vec[i] = vec[j]

        vec[j] = aux


def invertir_rango(vec, desde, hasta):

    a = desde

    b = desde + (hasta - desde + 1) // 2

    for i in range(a, b):

        j = len(vec) - 1 - i

        #swap
        aux = vec[i]

        vec[i] = vec[j]

        vec[j] = aux


def ordenar(vec):

    for i in range(len(vec) - 1):
        for j in range(i + 1, len(vec)):

            if vec[i] > vec[j]:
               #swap
                aux = vec[i]

                vec[i] = vec[j]

                vec[j] = aux 



def main():

    v = [12, 23, 9, 10, 7, 18]

    print(v)

    cant_primos = calcularprimo(v)

    print(f"Primos: {cant_primos}")

    invertir(v)

    print(v)

    invertir_rango(v, 1, 4)

    print(v)

    ordenar(v)

    print(v)

main()