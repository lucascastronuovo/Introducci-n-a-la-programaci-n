
"""
Se quiere procesar la venta de remeras lisas y estampadas de una tienda de ropa. 

Se quiere procesar la información mensualmente (31 días).

Se carga la cantidad vendida por día. (Utilizando arreglos)
Se ingresa L para indicar remera lisa y E para indicar remera estampada. (Un vector para cada tipo)
Se pide calcular el máximo vendido en el mes para un tipo de remera, mostrar el día del mes al que corresponde. 
(Resolver con funciones)
Calcular el promedio mensual en pesos, sabiendo que el costo de las remeras lisas es $350 y las estampadas $385. 
(Resolver con funciones).
Determinar en pesos de cual producto se vendió más.


"""

def seg_comprando ():
    respuesta = input("Seguir comprando (SI - NO): ")
    
    while not (respuesta == "SI" or respuesta == "NO"):
        respuesta = input("Seguir comprando (SI - NO): ")
        
    
    return respuesta
    

def preguntar_remera():
    
    rem = input("Estampada (E) o Lisa (L): ")
    
    while not (rem == "E" or rem == "L"):
        rem = input("Estampada (E) o Lisa (L): ")
    
    return rem




def maximo (vector):
    
    for i in range(len(vector)):
        
        if i == 0:
            maximo = vector[i]
        elif vector[i] > maximo:
            maximo = vector[i]
    
    return maximo
    
    
def dia_maximo(vector, maximo):
    
    
    for i in range(len(vector)):
        
        if vector[i] == maximo:
            
            dia_maximo = i
            
    
            
    return dia_maximo
            
            
    
def promedio(vector):
    
    suma = 0
    contador = 0
    
    for i in range(len(vector)):
        suma += vector[i]
        
        contador += 1
     
     
    
       
    if contador > 0:
        promedio = suma / contador
        
    else:
        promedio = "Error"
        
        
    
    return promedio
    
    
def mayor_venta(m_l,m_e):
    
    cant_l = m_l // 350
    
    cant_e = m_e // 385
    
    
    if cant_l > cant_e:
        mayor = "Remeras Lisas"
    elif cant_e > cant_l:
        mayor = "Remeras Estampadas"
        
    else:
        mayor = "Igual cantidad"
        
    return mayor
    

def main ():
    
    lisa = []
    
    estampada = []
    
    for d in range(0, 31):
        cantidad_estampada = 0
        cantidad_lisa = 0
        
        print(f"Dia {d}:")
        
        seguir_comprando = seg_comprando()
        
        while seguir_comprando != "NO":
            
            remera = preguntar_remera()
        
            if remera == "L":
                
                cantidad_lisa += 1
                
                precio_l = 350
                
                
                
            else:
                
                cantidad_estampada += 1
                
                precio_e = 385
                
            
            
            seguir_comprando = seg_comprando()   
        
        
        
        cant_vend_dia_l = cantidad_lisa * precio_l
        
        lisa.append (cant_vend_dia_l)
        
        
        
      
        cant_vend_dia_e = cantidad_estampada * precio_e
        
        estampada.append (cant_vend_dia_e)
        
        
        print("Lisa: ", lisa)
    
        print("Estampada: ", estampada)

    
    maximo_l = maximo(lisa)
    
    
    
    maximo_e = maximo(estampada)
    
    
    dia_maximo_l = dia_maximo(lisa, maximo_l)
    
    dia_maximo_e = dia_maximo(estampada, maximo_e)
    
    
    print(f"El máximo vendido en un mes para las remeras lisas es {maximo_l} día {dia_maximo_l}")
    
    print(f"El máximo vendido en un mes para las remeras estampadas es {maximo_e} día {dia_maximo_e}")
    
    
    promedio_l = promedio(lisa)
    
    promedio_e = promedio(estampada)
    
    
    print("Promedio mensual de remeras lisas:", promedio_l)
    
    print("Promedio mensual de remeras estampadas:", promedio_e )
    
    
    may_ventas = mayor_venta(maximo_l, maximo_e)
    
    
    print("Se vendieron más las:", may_ventas)
    
    
    
    
            
            
            



main()    