def validacion_pregunta(validar_string_pregunta):
    while not (validar_string_pregunta == "FIN" or validar_string_pregunta == "CONTINUAR") :
        validar_string_pregunta = input("Continuas (CONTINUAR) o finalizas (FIN): ")
        
        
    
    return validar_string_pregunta
    


def numeros ():
    numeros = []
    
    num = int(input("Numero: "))
    
    numeros.append(num)
    
    pregunta = input("Continuas (CONTINUAR) o finalizas (FIN): ")
    pregunta = validacion_pregunta(pregunta)
    
    while pregunta != "FIN":
        
        num = int(input("Numero: "))
        numeros.append(num)
        
        
        pregunta = input("Continuas (CONTINUAR) o finalizas (FIN): ")
        pregunta = validacion_pregunta(pregunta)
        
    
    return numeros


def maximo_v (num_v):
    
    for i in range(len(num_v)):
        
        if i == 0:
            maximo = num_v[i]
            
        elif num_v[i] > maximo:
            maximo = num_v[i]
            

    return maximo
    

def minimo_v (num_v):
    
    for i in range(len(num_v)):
        
        if i == 0:
            minimo = num_v[i]
            
        elif num_v[i] < minimo:
            minimo = num_v[i]
            
        
    
    return minimo


def main ():
    
    numeros_v = numeros()
    
    maximo = maximo_v(numeros_v)
    
    minimo = minimo_v (numeros_v)
    
    print(f"El máximo es {maximo} y el mínimo {minimo}")


main()
