'''
Se necesita un programa el cual registre los consumos de gas de un 
edificio y poder liquidar las expensas. Para ello, se ingresan los 
consumos de los N departamentos (N ingresado por teclado). 
Ademas de los consumos se ingresan los nombres de los propietarios y los metros cuadrados del depto.

El administrador necesita saber:

a) Promedio de consumo.
b) El departamento (indice) que tuvo mayor consumo.
c) Cuantos departamentos estan por debajo del promedio.
d) Cual propietario registra el menor consumo.
e) Cual es el promedio por metro cuadrado del consumo. (suma mtros cuadrados / suma consumos)

f) Listar los datos ordenados por nombre
g) De los departamentos que el consumo supere el promedio, listarlos ordenados por consumo.
'''

def validacion_de_valores (valor):
    while not valor > 0:
        valor = int(input("¡Valor no válido! Ingrese denuevo: "))
    
    return valor


def ord_dept_sup_prom_consumo (cons,nom,met_cuad,prom_cons):

    for i in range(len(cons)):
        if cons[i] < prom_cons:
            cons.remove(cons[i])

            nom.remove(nom[i])

            met_cuad.remove(met_cuad[i])

    for i in range(len(cons) - 1):
        for j in range(i + 1, len(cons)):
            if cons[i] < cons[j]:
                aux = cons[i]
                cons[i] = cons[j]
                cons[j] = aux 

                aux = met_cuad[i]
                met_cuad[i] = met_cuad[j]
                met_cuad[j] = aux

                aux = nom[i]
                nom[i] = nom[j]
                nom[j] = aux

    



    




def calcular_prom_cons (cons):
    suma = 0
    cant = 0
    
    
    for i in range(len(cons)):
        suma += cons[i]

        cant += 1

    if cant > 0:
        promedio = suma / cant
    else:
        print("Error")

    return promedio


def calcular_mayor_consumo (cons):

    for i in range(len(cons)):
        if i == 0:
            mayor = cons[i]
            indice_mayor = i
        elif cons[i] > mayor:
            mayor = cons[i]
            indice_mayor = i

    
    return indice_mayor

    
def calcular_deptos_deb_prom (cons_prom, cons):
    menor_prom = 0
    for i in range(len(cons)):
        if cons_prom > cons[i]:
            menor_prom += 1

    return menor_prom   


def calcular_prop_menor_cons (cons, prop):

    for i in range(len(cons)):
        if i == 0:
            men_cons = cons[i]
            prop_men_cons = cons[i]
        elif cons[i] < men_cons:
            men_cons = cons[i]
            prop_men_cons = prop[i]

    return prop_men_cons



def calcular_prom_metcuad_cons (met_cuad, cons):

    suma = 0

    suma_met_cuad = 0

    for i in range(len(cons)):
        suma += cons[i]

    for i in range(len(met_cuad)):
        suma_met_cuad += met_cuad[i]

    if suma > 0:
        promedio = suma_met_cuad / suma
    else:
        print("Error")

    return promedio



def cargar_n_departamentos ():
    departamentos = int(input("Departamentos: "))
    valor_validado = validacion_de_valores(departamentos)

    return valor_validado
    



def cargar_consumo (deptos):
    v = []

    

    for i in range(deptos):
        consumo = int(input(f"Consumo dep {i}: "))
        valor_validado = validacion_de_valores(consumo)

        if consumo < 0:
            v.append(valor_validado)
        else:
            v.append(consumo)
        


    return v


def cargar_nombre (nom):
    x = []

    

    for i in range(nom):
        nombres = input(f"Nombre prop dep {i}: ")
        x.append(nombres)


    return x


def cargar_metro_cuadrado (depto):
    y = []

    

    for i in range(depto):
        met_cuad = int(input(f"Metro Cuadrado depto {i}: "))
        valor_validado = validacion_de_valores(met_cuad)

        if met_cuad < 0:
            y.append(valor_validado)
        else:
            y.append(met_cuad)


    return y



def ordenar_datos_por_nombre(nombre, met_cuad, consumo):

    for i in range(len(nombre) - 1):
        for j in range(i + 1, len(nombre)):
            if nombre[i] > nombre[j]:
                aux = nombre[i]
                nombre[i] = nombre[j]
                nombre[j] = aux 

                aux = met_cuad[i]
                met_cuad[i] = met_cuad[j]
                met_cuad[j] = aux

                aux = consumo[i]
                consumo[i] = consumo[j]
                consumo[j] = aux






def main ():
    departamentos = cargar_n_departamentos()
    consumos = cargar_consumo(departamentos)
    nombres = cargar_nombre(departamentos)
    metro_cuadrado = cargar_metro_cuadrado(departamentos)

    promedio_consumo = calcular_prom_cons (consumos)
    depto_mayor_consumo = calcular_mayor_consumo (consumos)
    deptos_deb_prom = calcular_deptos_deb_prom (promedio_consumo, consumos)
    prop_menor_cons = calcular_prop_menor_cons (consumos, nombres)
    prom_metcuad_cons = calcular_prom_metcuad_cons (metro_cuadrado, consumos)

    print(f"a) Promedio de consumo: {promedio_consumo}")
    print(f"b) El departamento (indice) que tuvo mayor consumo: {depto_mayor_consumo}")
    print(f"c) Cuantos departamentos estan por debajo del promedio: {deptos_deb_prom}")
    print(f"d) Cual propietario registra el menor consumo: {prop_menor_cons}")
    print(f"e) Cual es el promedio por metro cuadrado del consumo. (suma mtros cuadrados / suma consumos): {prom_metcuad_cons}")


    ordenar_datos_por_nombre(nombres, metro_cuadrado, consumos)

    print("Nombres Ordenados:", nombres)
    print("Metro Cuadrado Ordenados:", metro_cuadrado)
    print("Consumos Ordenados:", consumos)

    ord_dept_sup_prom_consumo(consumos,nombres,metro_cuadrado,promedio_consumo)

    print("Nombre (sup_prom) Ordenado por consumo:", nombres )
    print("Nombre (sup_prom) Ordenado por consumo:", consumos)
    print("Nombre (sup_prom) Ordenado por consumo:", metro_cuadrado)


    


main()
    

    
    


    
