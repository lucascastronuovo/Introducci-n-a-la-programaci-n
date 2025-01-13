

def ordenar(vector):

    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i] < vector[j]:

                #swap
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux



def main():
    v = [12, 45, 88, 96, 32]
    print(v)

    ordenar(v)

    print(v)



main()
