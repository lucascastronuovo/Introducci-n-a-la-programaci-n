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

#https://onlinegdb.com/WiaZw476g


def exceden_promedio(nuevo_vec, vec):
    
    suma = 0
    
    for i in range(len(vec)):
        
        suma += vec[i]
    
    prom = suma / len(vec)
    
    prom_10 = prom * 1.10
    
    for j in range(len(vec)):
        
        
        if vec[j] > prom_10:
            
            nuevo_vec.append(j)
            
    

        
        
        



def determinar_cantidadxdia(vec, dia):
    
    
    
    for i in range(len(vec)):
        if dia == i:
            cant_multas_dia_det = vec[i]
            
    
    return cant_multas_dia_det
    


def calcular_mayor_dia_multas(vec):
    
    for i in range(len(vec)):
        
        if i == 0:
            mayor_dia = i
            
        elif mayor_dia < vec[i]:
            mayor_dia = i
            
    
    return mayor_dia

def promedio_tipo_multa(multa_vel, multa_semf):

    cant_vel = len(multa_vel)

    cant_semf = len(multa_semf)
    
    pregunta = input("Obtener promedio de multa (V) o multa (R): ")
    while not (pregunta == "V" or pregunta == "R"):
        pregunta = input("Obtener promedio de multa (V) o multa (R): ")
    
    if (pregunta == "V" and cant_vel > 0):
        
        suma = 0
        
        for i in range(len(multa_vel)):
            
            suma += multa_vel[i]
            
        
        promedio = suma / len(multa_vel)
        
        
        promedio_pesos = promedio * 1500
        
    elif (pregunta == "R" and cant_semf > 0):
        
        suma = 0
        
        for i in range(len(multa_vel)):
            
            suma += multa_semf[i]
            
            
        
        promedio = suma / len(multa_semf)
        
        promedio_pesos = promedio * 1800
        
    else:
        promedio_pesos = "No se pudo calcular el promedio"
            
            
     
     
    return promedio_pesos   

def main():
    
    #1
    
    multa_exc_vel = []
    multa_sem_rojo = []
    
    for i in range(1, 31 + 1):
        
        print("Día", i ,":")
        
        cantidad_de_vel = int(input("Cantidad de multas de exc. de vel: "))
        while not cantidad_de_vel >= 0:
            cantidad_de_vel = int(input("Cantidad de multas de exc. de vel: "))

        multa_exc_vel.append(cantidad_de_vel)
            
        
        cantidad_de_sem_rojo = int(input("Cantididad de multas de semaforo en rojo: "))
        while not cantidad_de_sem_rojo >= 0:
            cantidad_de_sem_rojo = int(input("Cantididad de multas de semaforo en rojo: "))

        multa_sem_rojo.append(cantidad_de_sem_rojo)   
        
    
    #2
    
    promedio_multas = promedio_tipo_multa(multa_exc_vel, multa_sem_rojo)
    
    
    
    
    
    #3
    
    historial_v = []
    
    historial = int(input("Ingrese la cantidad de multas del día a averiguar (Multas de velocidad): "))
    while not historial >= 0:
        historial = int(input("Ingrese la cantidad de multas del día a averiguar (Multas de velocidad): "))
    
    for i in range(len(multa_exc_vel)):
        
        if historial == multa_exc_vel[i]:
            
            historial_v.append(i)
            
    
    
    
        
    
    
    #4
    
    may_dia_mult_v = calcular_mayor_dia_multas(multa_exc_vel)
    
    
    
    may_dia_mult_semf = calcular_mayor_dia_multas(multa_sem_rojo)
    
    
    
    
    #5
    
    preguntar_dia = int(input("Día: "))
    while not (preguntar_dia >= 1 and preguntar_dia <= 31):
       preguntar_dia = int(input("Día: "))
       
    
    cant_dia_det_mult_vel = determinar_cantidadxdia(multa_exc_vel, preguntar_dia)
    
    
    
    cant_dia_det_mult_semf = determinar_cantidadxdia(multa_sem_rojo, preguntar_dia)
    
    
    

    #6
    
    dias_exc_prom = []
    
    exceden_promedio(dias_exc_prom, multa_exc_vel)
    
    
    
    
    print("----")
    print("El promedio de multa seleccionada es $", promedio_multas)

    if len(historial_v) != 0:
        print(f"Habrá una cantidad de {historial} multas de exc_vel en los días {historial_v} del correspondiente mes")
    
    else:
        
        for i in range(len(multa_sem_rojo)):
        
            if historial == multa_sem_rojo[i]:
                
                historial_v.append(i)
                
                
        print(f"Habrá una cantidad de {historial} multas de semf_rojo en los días {historial_v} del correspondiente mes")
                
    print("El día con mayor cantidad de multas de velocidad es el", may_dia_mult_v, "del correspondiente mes")     
    print("El día con mayor cantidad de multas de semáforo en rojo es el", may_dia_mult_semf, "del correspondiente mes")       
    print(f"En el día {preguntar_dia} se registraron {cant_dia_det_mult_vel} multas de velocidad y {cant_dia_det_mult_semf} multas de semáforo en rojo")            
    print(f"Los dias en donde la cant de multas de velocidad exceden el promedio en 10% son: {dias_exc_prom}")
    
    
    
    
    
    
            
          
main()      
        
           