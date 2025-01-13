"""
Un corredor da vueltas a una plaza 10 veces, en cada vuelta
cuenta la cantidad de pajaritos que vió.
- Cual fue la cantidad maxima de pajaritos que se vió 
  en una vuelta?
"""

def actualizar_maximo(vector):

    for i in range(10):

        if i == 0:
            maximo = vector[i]
        elif maximo < vector[i]:
            maximo = vector[i]

    return maximo

def main():

    pajaros_vuelta = []

    for vuelta in range(1, 11):
        print(f"Vuelta {vuelta}: ")
        
        cant_pajaros = int(input("Cuantos pájaros ví: "))

        pajaros_vuelta.append(cant_pajaros)

        print()

        
    maximo_pajaros = actualizar_maximo(pajaros_vuelta)
    

    print(f"La cantidad máxima de pajaritos que se vió fue {maximo_pajaros}")


    


main()