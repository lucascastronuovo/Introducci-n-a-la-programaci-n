"""
Se requiere realizar la gestion de control de multas realizadas en un periodo de un mes en la ciudad.
Para ello se consideran 2 tipos de multas: exceso de velocidad y semaforo en rojo.
Exceso de velocidad: 1500, Semaforo en rojo: 1800
Se pide:
- Cargar un arreglo por cada tipo de multa, guardando la cantidad de multas realizadas diaramente. Se deben validar correctamente los datos de entrada ✔
- Generar una funcion que calcule el promedio de las multas para un tipo de multa ingresada por teclado, y luego mostrar el valor en pesos. ✔
- Ingresar por teclado una cantidad de multas, y decir en que dia se encuentra, si no esta, mostrar la leyenda en el vector de semaforo en rojo. ✔
- Generar una funcion que retorne el dia que mayor cantidad de multas hubo(sin ordenar el vector). ✔
- Generar una funcion que reciba como parametro una posición (dia) y retorne el total en cantidad de multas del dia, considerando ambos tipos de multa. ✔
- Crar una funcion que genere a partir de un vector de exceso de velocidad, otro vector conteniendo solo los dias en los cuales la cantidad de multas se supere al promedio en 10%.
"""
def ingreso (vec):
    cont = 0
    while cont < 32:
        print ("el dia", cont+1)
        multa = int(input("Cuantas multas hubo?: "))
        while multa < 0:
            print("no pueden haber multas negativas")
            multa = int(input("Cuantas multas hubo?: "))
        vec.append(multa)
        cont += 1
    return vec

def promedio (vec, costo):
    suma = 0
    for i in range (len(vec)):
        suma += vec[i]
    prom = suma/len(vec)
    total = prom * costo
    return total

def cantidad_multas (vec):    
    cant = int(input("ingrese la cantidad que desea buscar: "))
    while cant < 0:
        print ("error, no pueden haber cantidades negativas")
        cant = int(input("ingrese la cantidad que desea buscar: "))
    hubo = 0
    
    for i in range (len(vec)):
        if vec[i] == cant:
            hubo += 1
            return i+1
    
    if hubo == 0:
        return "no se encontró un dia con ese monto"

def mas_multas (vec):
    maxi = vec[0]
    dia = 0

    for i in range (len(vec)):
        if vec[i] > maxi:
            maxi = vec[i]
            dia = i

    return dia+1

def exceso_dias (vec):
    suma = 0
    nuevo = []

    for i in range (len(vec)):
        suma += vec[i]
    prom = (suma/len(vec))+(((suma/len(vec))/100)*10)

    for j in range (len(vec)):
        if vec[j] > prom:
            nuevo.append(j+1)
    return nuevo

def main ():
    cant = int(input("cuantos tipos de multas desea ingresar?: "))

    while cant < 0:
        print("error, solo pueden haber cantidades positivas")
        cant = int(input("cuantas multas desea ingresar?: "))
    
    multi_vec = []

    for i in range (cant):
        tipo = str(input("Cual tipo de multa desea ingresar?: "))
        vec = [] 
        ingreso(vec)
        print ("punto 1:","tipo de multa:", tipo, vec)

        multi_vec.append(vec)

        print ("Tenga en cuenta que: el valor de exceso de velocidad es de 1500 y el de semáforo en rojo es de 1800")
        pesos = int(input("ingrese el valor del tipo de multa: "))
        while pesos < 0:
            print("error, no puede haber monto negativo")
            pesos = int(input("ingrese el valor del tipo de multa: "))

        promediado = promedio(vec, pesos)
        print ("promedio ganado en", tipo, ":", promediado)

        cantidad = cantidad_multas(vec)
        print ("dia en que hubo esa cantidad:", cantidad)

        multas = mas_multas(vec)
        print ("el dia con mas multas de tipo", tipo, "fue:", multas)

        mayores = exceso_dias(vec)
        print ("los dias que superan al promedio en", tipo, "son", mayores)
    
    nuevo_vec = [0]*(31)
    for j in range (cant):
        vector = multi_vec[j]  
        for x in range (len(nuevo_vec)):
            nuevo_vec[x] += vector[x]
    print ("nuevo vector", nuevo_vec)

    dia = int(input("de que dia quiere saber el valor total?: "))
    while (dia > 31) and (dia < 0):
        print ("error, debe ser un dia entre 0 y 31")
        dia = int(input("de que dia quiere saber el valor total?: "))

    for p in range (len(nuevo_vec)):
        i = p+1
        if i == dia:
            print("el valor del dia", i, "es", nuevo_vec[p])

main()