# Cargar un arreglo con 12 números enteros. Mostrarlo y calcular:
#     El elemento máximo y mínimo.
#     Calcular el promedio de los elementos ubicados en posiciones pares.
#     Calcular la sumatoria de los elementos pares en posiciones impares.
#     Calcular la cantidad de numeros primos.



def cargar_vector(v, longitud):
    
    for i in range(longitud):
        numero = int(input("Número: "))
        
        v.append(numero)
        
        


def calcular_max (vec_max):
    
    for i in range(len(vec_max)):
        if i == 0:
            maximo = vec_max[i]
            
        elif vec_max[i] > maximo:
            maximo = vec_max[i]
            
            
    
    return maximo
    
    
    
def calcular_min (vec_min):
    
    for i in range(len(vec_min)):
        if i == 0:
            minimo = vec_min[i]
            
        elif vec_min[i] < minimo:
            minimo = vec_min[i]
            
    
    return minimo
    
    
def promedio_pos_pares (vec_prom):
    
    suma_prom = 0
    
    contador_prom = 0
    
    for i in range(len(vec_prom)):
        
        if i % 2 == 0:
            suma_prom = vec_prom[i]
            
            contador_prom += 1
            
    
    if contador_prom > 0:
        
        promedio = suma_prom / contador_prom
        
    else:
        promedio = "Error"
        
        
    return promedio
    
    
    

    
def suma_pares_pos_impares(vec_sumat):
    
    suma_sumat = 0
    

    
    for i in range(len(vec_sumat)):
        
        if (vec_sumat[i] % 2 == 0 and i % 2 != 0):
            
            suma_sumat += vec_sumat[i]
            

            
            
            
            
    return suma_sumat
    
    


def cantidad_primos (vec_primos):
    
   cont_primos = 0
    
   for i in range(len(vec_primos)):
        div = 0
        for j in range(2, vec_primos[i]+1):
            if vec_primos[i] % j == 0:
                div += 1
        if div == 1:
            cont_primos += 1

   return cont_primos
    
    

def main ():
    vector = []
    cargar_vector(vector, 12)
    
    print(vector)
    
    maximo = calcular_max (vector)
    
    minimo = calcular_min (vector)
    
    promedio_posiciones_pares = promedio_pos_pares (vector)
    
    sumatoria_el_pares_pos_impares = suma_pares_pos_impares (vector)
    
    cant_primos = cantidad_primos(vector)
    
    
    print()
    print()
    
    print("El máximo es", maximo)
    print("El mínimo es", minimo)
    print("El promedio de las posiciones pares es", promedio_posiciones_pares)
    print("La sumatoria de elementos pares en posiciones impares es", sumatoria_el_pares_pos_impares)
    print("La cantidad de primos es", cant_primos)
    
main()