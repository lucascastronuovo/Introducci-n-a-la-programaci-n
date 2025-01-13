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

def preguntar_estacion ():
    
    est = input("Estación (R o C): ")
    
    while not (est == "R" or est == "C"):
        est = input("Estación (R o C): ")
        
    return est
    
    
def leer_peso():
    peso = float(input("Peso: "))
    
    while not peso >= 0:
        peso = float(input("Peso: "))
        
    return peso
    
    
    
def leer_edad(ed_v):
    
    edad = int(input("Edad: "))
    
    while not edad >= 0:
       edad = int(input("Edad: "))
       
       
    ed_v.append(edad)
    
def leer_sexo (sex_v):
    
    sexo = input("Sexo (H o M): ")
    
    while not (sexo == "H" or sexo == "M"):
        sexo = input("Sexo (H o M): ")
        
    sex_v.append(sexo)    
    
    
    
def cargar_datos_r (pes_r,ed_r,sex_r):

    print()
    print()
    print("Retiro: ")
    
    c_enc = 0
    
    peso = leer_peso()
    
    

    
    while peso != 0:
        
        pes_r.append(peso)
        
        leer_edad(ed_r)
        
        leer_sexo(sex_r)
        
        
        c_enc += 1
        
        peso = leer_peso()
        
    
    
    return c_enc    


def cargar_datos_c(pes_c, ed_c, sex_c):

    print()
    print()
    print("Constitución: ")

    c_enc = 0
    
    peso = leer_peso()
    
    

    
    while peso != 0:
        
        pes_c.append(peso)
        
        leer_edad(ed_c)
        
        leer_sexo(sex_c)
        
        
        c_enc += 1
        
        peso = leer_peso()
        
    
    
    return c_enc 




def mostrar_datos_cargados(p_r, e_r, s_r, p_c, e_c, s_c):
    print()
    print()
    print("Retiro:")
    print()
    print("Peso:", p_r)
    print("Edad:", e_r)
    print("Sexo:", s_r)
    
    print()
    print()
    print("Constitución: ")
    print()
    print("Peso:", p_c)
    print("Edad:", e_c)
    print("Sexo:", s_c)
    print()
    


def promedio (suma, contador):
    
    if contador > 0:
        prom = suma / contador
        
    else:
        prom = suma / 1
        
    return prom
 
def comparacion_peso_promedio(pes_r, pes_c):
    
    suma_r = 0
    
    contador_r = 0
        
    for i in range(len(pes_r)):
        suma_r += pes_r[i]
     
        contador_r += 1
        
    
    promedio_r = promedio(suma_r,contador_r)
    
    suma_c = 0
    
    contador_c = 0
    
    for j in range(len(pes_c)):
        
        suma_c += pes_c[j]
        
        contador_c += 1

    
    promedio_c = promedio(suma_c,contador_c)
    
    
    if promedio_c > promedio_r:
        
        may_prom_peso = "Constitución tiene mayor promedio de peso", promedio_c
        
    elif promedio_r > promedio_c:
        
        may_prom_peso = "Retiro tiene mayor promedio de peso", promedio_r
    else:
        may_prom_peso = "Ambos tienen el mismo promedio de peso"
        
    return may_prom_peso
    


def ordenar_por_edad_enc_mayor(p,e,s):

    for i in range(len(e) -1):
        for j in range(i + 1, len(e)):

            if e[i] < e[j]:

                aux = e[i]

                e[i] = e[j]

                e[j] = aux

                aux = p[i]

                p[i] = p[j]

                p[j] = aux

                aux = s[i]

                s[i] = s[j]

                s[j] = aux


def cargar_vector_pesos_sup_prom_gen(vector, p_r, p_c):
    
    suma = 0 
    
    contador = 0
    
    for i in range(len(p_r)):
        
        suma += p_r[i]
        
        contador += 1
        
    
    for j in range(len(p_c)):
        
        suma += p_c[j]
        
        contador += 1
        
        
    promedio_general = promedio(suma, contador)
    
    
    for n in range(len(p_r)):
        
        if promedio_general < p_r[n]:
            
            vector.append(p_r[n])
            
    for m in range(len(p_c)):
        
        if promedio_general < p_c[m]:
            
            vector.append(p_c[m])
            

    
def main ():
    
    peso_r = []
    
    edad_r = []
    
    sexo_r = []
    
    
    peso_c = []
    
    edad_c = []
    
    sexo_c = []
    
    
    peso_mayor_prom = []
    
    estacion = preguntar_estacion() 
    
    if estacion == "R":
        
        cant_encuestas_r = cargar_datos_r(peso_r,edad_r,sexo_r)
        
        cant_encuestas_c = cargar_datos_c (peso_c,edad_c,sexo_c)
        
    else:
        
        cant_encuestas_c = cargar_datos_c (peso_c,edad_c,sexo_c)
        
        cant_encuestas_r = cargar_datos_r(peso_r,edad_r,sexo_r)
        
        
    
    
    
    
    
    mostrar_datos_cargados(peso_r,edad_r,sexo_r, peso_c,edad_c,sexo_c)
    
    peso_mayor_promedio = comparacion_peso_promedio (peso_r, peso_c)
    
    print(peso_mayor_promedio)
    
    if cant_encuestas_r > cant_encuestas_c:
        
        ordenar_por_edad_enc_mayor (peso_r,edad_r,sexo_r)
        
        print()
        print("Retiro: ")
        print()
        print("Peso:", peso_r)
        print("Edad:", edad_r)
        print("Sexo:", sexo_r)
    
    elif cant_encuestas_c > cant_encuestas_r:
        
        ordenar_por_edad_enc_mayor (peso_c,edad_c,sexo_c)
        print()
        print("Constitución: ")
        print()
        print("Peso:", peso_c)
        print("Edad:", edad_c)
        print("Sexo:", sexo_c)
        
        
    
    cargar_vector_pesos_sup_prom_gen(peso_mayor_prom, peso_r, peso_c)
    
    print("Pesos de ambos lotes que superan el promedio general:", peso_mayor_prom)
        

    
        
        
    
    


main()