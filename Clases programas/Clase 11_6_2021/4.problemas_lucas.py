'''
1)	El Ministerio de Salud le solicitó realizar un programa para llevar adelante un
censo de salud se tomaron los siguientes datos: peso, edad y sexo. Se realizan dos encuestas,
y los datos fueron tomados en dos estaciones ferroviarias: Retiro y Constitución. El sistema
recibe una ‘R’ si en Retiro o una ‘C’ si fue en Constitución. 
Se sabe que como mucho se tomaron 100 datos en cada encuesta.
a.	Cargar los datos de todas los encuestados. El ingreso concluye cuando el encuestador
 ingresa un número menor a 0 en el peso. Todos los datos deben ser validados.
b.	Mostrar los datos cargados.
c.	Determinar promediando cuál de las dos estaciones tiene las personas con mayor peso
 (mayor promedio).
d.	Ordenar los datos (segun edad) correspondiente al que se ingresaron más encuestas. Mostrarlo.
e.	Generar un nuevo vector con los pesos de ambos lotes que superen el promedio general. 
Mostrarlo.
'''


# lista peso R
# lista edad R
# lista sexo R

# lista peso C
# lista edad C
# lista sexo C

# Retiro R

# Constitución C

def validacion_estacion (est):
    while not (est == "C" or est == "R"):
        est = input("Ingrese C o R: ")
    
    return est

def validacion_nums (val):
    while not val >= 0:
        val = int(input("Ingrese valores positivos o 0: "))

    return val

def validacion_sexo (sex):
    while not (sex == "H" or sex == "M"):
        sex = input("Hombre o Mujer: ")

    return sex



def listar_peso(peso, peso_lista):
       
        
    peso_lista.append(peso)

    return peso_lista


def listar_edad(edad_lista):
    edad = int(input("Edad: "))
    edad = validacion_nums(edad)

    edad_lista.append(edad)

    return edad_lista


def listar_sexo (sexo_lista):
    sexo = input("Sexo Hombre (H) - Mujer (M): ")
    sexo = validacion_sexo(sexo)

    sexo_lista.append(sexo)

    return sexo_lista


def promedio_peso_estacion (peso_lista):

    cantidad = 0
    suma = 0
    for i in range(len(peso_lista)):
        suma += peso_lista[i]

        cantidad += 1


    if cantidad == 0:
        promedio = print("Error")
    else:
        promedio = suma / cantidad

    return promedio

def swap(dato_a_ordenar, i, j):
    aux = dato_a_ordenar[j]
    dato_a_ordenar[j] = dato_a_ordenar[i]
    dato_a_ordenar[i] = aux

    
def ordenar (edad_r, edad_c, dato_a_ordenar_a,dato_a_ordenar_b, cant_enc_a, cant_enc_b):
    dato_ordenado = []
    if cant_enc_a >= cant_enc_b:
        for i in range(len(edad_r) - 1):
            for j in range(len(edad_r) + 1):
                if dato_a_ordenar_a[i] > dato_a_ordenar_a[j]:
                    dato_a_ordenar_b = swap(dato_a_ordenar_a, i, j)
                    dato_ordenado = dato_a_ordenar_a

                
    elif cant_enc_a < cant_enc_b:
        for i in range(len(edad_c) - 1):
            for j in range(len(edad_c)):
                if dato_a_ordenar_b[i] > dato_a_ordenar_b[j]:
                    dato_a_ordenar_b = swap(dato_a_ordenar_b, i, j)
                    dato_ordenado = dato_a_ordenar_b

    return dato_ordenado


def ordenar_string (string_v_r,string_v_c,edad_r,edad_c, cant_enc_r, cant_enc_c):
    string_ordenado = []
    if cant_enc_r >= cant_enc_c:
        for i in range(len(edad_r) - 1):
            for j in range(len(edad_r) + 1):
                if edad_r [i] > edad_r[j]:
                    string_v_r = swap(string_v_r, i, j)
                    string_ordenado = string_v_r
    elif cant_enc_r >= cant_enc_c:
        for i in range(len(edad_c) - 1):
            for j in range(len(edad_c)):
                if edad_c[i] > edad_c[j]:
                    string_v_c = swap(string_v_c, i, j)
                    string_ordenado = string_v_c

    return string_ordenado



def main ():
    estacion = input("Estación Constitución (C) - Retiro (R): ")
    estacion = validacion_estacion (estacion)
    if estacion == "R":
        print("RETIRO: ")
    else:
        print("CONSTITUCIÓN:")

    peso = int(input("Peso: "))

    lista_peso_r = []
    lista_edad_r = []
    lista_sexo_r = []

    lista_peso_c = []
    lista_edad_c = []
    lista_sexo_c = []


     

    if estacion == "R":
        i = 0
        

        while (peso > 0 and i <= 100) :
            lista_peso_r = listar_peso(peso, lista_peso_r)
            lista_edad_r = listar_edad(lista_edad_r)
            lista_sexo_r = listar_sexo(lista_sexo_r)
            i = i + 1
            peso = int(input("Peso: "))

        promedio_peso_r = promedio_peso_estacion(lista_peso_r)

        print()
        print("Encuesta de RETIRO finalizada por ingreso de num neg en el peso o por superar el max de encuestados posibles (100): ")
        print()
        print()
        
        print("CONSTITUCIÓN:")

        j = 0
                

        
        peso = int(input("Peso: "))
        while (peso > 0 and j <= 100):
            lista_peso_c = listar_peso(peso, lista_peso_c)
            lista_edad_c = listar_edad(lista_edad_c)
            lista_sexo_c = listar_sexo(lista_sexo_c)
            j = j + 1
            peso = int(input("Peso: "))
        
        promedio_peso_c = promedio_peso_estacion(lista_peso_c)

        print()
        print("Encuesta de CONSTITUCIÓN finalizada por ingreso de num neg en el peso o por superar el max de encuestados posibles (100): ")
        print()
        print()
        
        

    else:
        j = 0
                

        
        
        while (peso > 0 and j <= 100):
            lista_peso_c = listar_peso(peso, lista_peso_c)
            lista_edad_c = listar_edad(lista_edad_c)
            lista_sexo_c = listar_sexo(lista_sexo_c)
            j = j + 1
            peso = int(input("Peso: "))

        promedio_peso_c = promedio_peso_estacion(lista_peso_c)

        print()
        print("Encuesta de CONSTITUCIÓN finalizada por ingreso de num neg en el peso o por superar el max de encuestados posibles (100): ")
        print()
        print()
        
        print("RETIRO: ")

        i = 0
        
        peso = int(input("Peso: "))
        while (peso > 0 and i <= 100):
            lista_peso_r = listar_peso(peso, lista_peso_r)
            lista_edad_r = listar_edad(lista_edad_r)
            lista_sexo_r = listar_sexo(lista_sexo_r)
            i = i + 1
            peso = int(input("Peso: "))

        promedio_peso_r = promedio_peso_estacion(lista_peso_r)

        print()
        print("Encuesta de RETIRO finalizada por ingreso de num neg en el peso o por superar el max de encuestados posibles (100): ")
        print()
        print()
       
    if (promedio_peso_c != None and promedio_peso_r != None):
    
        if promedio_peso_c > promedio_peso_r:
            mayor_peso = "La estación CONSTITUCIÓN tiene mayor peso"
        elif promedio_peso_c < promedio_peso_r:
            mayor_peso = "La estación RETIRO tiene mayor peso"
        else:
            mayor_peso = "Ambas estaciones tienen el mismo promedio de peso" 
    else:

        mayor_peso = "Error"
        

    if i >= j:
        may_cant_encuestados = "RETIRO"
    elif i < j:
        may_cant_encuestados = "CONSTITUCIÓN"
    else:
        may_cant_encuestados = "NADIE"

    ordenar_p_edad_edades = ordenar(lista_edad_r,lista_edad_c,lista_edad_r,lista_edad_c,i,j)
    ordenar_p_edad_peso = ordenar(lista_edad_r,lista_edad_c,lista_peso_r,lista_peso_c,i,j)
    ordenar_p_edad_sexo = ordenar_string(lista_sexo_r,lista_sexo_c,lista_edad_r,lista_edad_c,i,j)


            
    print("b)")
    print("")
    print("RETIRO: ")
    print(f"Peso: {lista_peso_r}")
    print(f"Edad: {lista_edad_r}")
    print(f"Sexo: {lista_sexo_r}")
    print()
    print()
    print()
    print(f"CONSTITUCIÓN: ")
    print(f"Peso: {lista_peso_c}")
    print(f"Edad: {lista_edad_c}")
    print(f"Sexo: {lista_sexo_c}")
    print()
    print("c):")
    print()
    print(mayor_peso, f"----RETIRO: {promedio_peso_r} - CONSTITUCIÓN: {promedio_peso_c}")
    print()
    print("d) ")
    print(f"La mayor cantidad de encuestados la tiene {may_cant_encuestados} y sus datos ordenados por edad son:")
    print(f"Edad: {ordenar_p_edad_edades}")
    print(f"Peso: {ordenar_p_edad_peso}")
    print(f"Sexo: {ordenar_p_edad_sexo}")
    print("f)")



main()
        
