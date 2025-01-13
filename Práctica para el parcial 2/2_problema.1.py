'''
Se desea realizar un programa que lleve el control de la vacunacion del covid, para un centro de salud.
Se sabe que a lo sumo se presentan 100 personas (tamaño del vector), el ingreso finaliza cuando
el nombre ingresado es FIN
A cada persona que se lo vacuna se registran nombre, edad y peso. (3 vectores)
El programa debe:
- Tomar los datos por teclado, validandolos que sean correctos.
- Listar los datos ordenados por nombre
- Calcular el promedio de edades de los vacunados
'''

def ordenar_por_nombre(nom,ed,pes):
    
    for i in range(len(nom) -1):
        for j in range(i+1, len(nom)):
            
            if nom[j] < nom[i]:
                #Swap por nombre
                aux = nom[i]
                nom[i] = nom[j]
                nom[j] = aux
                
                #Swap por edad
                aux = ed[i]
                ed[i] = ed[j]
                ed[j] = aux
                
                #Swap por peso
                aux = pes[i]
                pes[i] = pes[j]
                pes[j] = aux
                
            



def leer_edad():
    edad = int(input("Edad: "))
    while not edad >= 0:
        edad = int(input("Edad: "))
        
    return edad
    
def leer_peso():
    peso = float(input("Peso: "))
    while not peso > 0:
        peso = float(input("Peso: "))
        
    return peso

def leer_nombre():
    nombre = input("Nombre o FIN: ")
    while nombre == "":
        nombre = input("Nombre o FIN: ")
    
    return nombre
    

def cargar_datos(n,e,p):
    contador = 0
    
    nombre = leer_nombre()
    
    
    while (nombre != "FIN" and contador <= 100):
        n.append(nombre)
        
        edad = leer_edad()
        e.append(edad)
        
        peso = leer_peso()
        p.append(peso)
        
        contador += 1
        
        nombre = leer_nombre()
        


def listar_datos(nom,ed,pes):
    print("Nombre:", nom)
    print("Edad:", ed)
    print("Peso:", pes)



def promedio_edades(edad):
    
    suma = 0
    
    for i in range(len(edad)):
        
        suma += edad[i]
    
    if len(edad) > 0:
        promedio = suma / len(edad)
    else:
        promedio = "Error"

    return promedio
    

def main():
    
    nombre = []
    edad = []
    peso = []
    
    cargar_datos(nombre, edad, peso)
    
    listar_datos(nombre, edad, peso)
    
    ordenar_por_nombre(nombre, edad, peso)
    
    print()
    print()

    listar_datos(nombre, edad, peso)
    
    promedio = promedio_edades(edad)
    
    print(f"El promedio de edades de los vacunados es {promedio}")
    


main()