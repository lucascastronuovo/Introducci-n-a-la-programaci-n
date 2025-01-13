import random

random.seed(0)

# Extra
def generar_vector(longitud):
    v = [0] * longitud

    for i in range(longitud):
        v[i] = random.randrange(50)   # Numeros entre 0 y 49

    return v

def ordenar(vector):
    for i in range(len(vector) - 1):
        for j in range(i+1, len(vector)):
            if vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

'''      
[24, 48, 26, 2, 16, 32, 31, 25, 19, 30]
[2, 48, 26, 24, 16, 32, 31, 25, 19, 30]
[2, 26, 48, 24, 16, 32, 31, 25, 19, 30]
[2, 24, 48, 26, 16, 32, 31, 25, 19, 30]
[2, 16, 48, 26, 24, 32, 31, 25, 19, 30]

'''

un_vector = generar_vector(20)
print(un_vector)

ordenar(un_vector)
print(un_vector)
