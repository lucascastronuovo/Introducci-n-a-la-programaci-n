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

def leer_nombre():
    nombre = input('Ingrese el nombre o FIN para finalizar: ')
    while nombre == '':
        nombre = input('Ingrese el nombre o FIN para finalizar: ')
    return nombre
    
def leer_edad():
    edad = int(input('Ingrese la edad: '))
    while edad < 0:
        edad = int(input('Ingrese la edad: '))
    return edad

def leer_peso():
    peso = float(input('Ingrese la peso: '))
    while peso < 0:
        peso = float(input('Ingrese la peso: '))
    return peso

def cargar_datos(n, e, p):
    contador = 0
    nombre = leer_nombre()
    while nombre != 'FIN' and contador < 100:
        n[contador] = nombre
        e[contador] = leer_edad()
        p[contador] = leer_peso()

        contador += 1
        nombre = leer_nombre()
        
    return contador

def listar(n, e, p, cantidad):
    for i in range(cantidad):
        print(f'Nombre: {n[i]} \t Edad: {e[i]} \t Peso: {p[i]:.2f}')

def ordenar_por_nombre(n, e, p, cantidad):
    for i in range(cantidad - 1):
        for j in range(i+1, cantidad):
            if n[i] > n[j]:
                aux = n[i]
                n[i] = n[j]
                n[j] = aux

                aux = e[i]
                e[i] = e[j]
                e[j] = aux

                aux = p[i]
                p[i] = p[j]
                p[j] = aux

                # p[i], p[j] = p[j], p[i]


def calcular_promedio(vector, cantidad):
    suma = 0
    for i in range(cantidad):
        suma += vector[i]

    return suma / cantidad



nombres = [''] * 100
edades = [0] * 100
pesos = [0] * 100

cantidad_pesonas = cargar_datos(nombres, edades, pesos)

listar(nombres, edades, pesos, cantidad_pesonas)

print()

ordenar_por_nombre(nombres, edades, pesos, cantidad_pesonas)

listar(nombres, edades, pesos, cantidad_pesonas)

promedio = calcular_promedio(edades, cantidad_pesonas)
print(f'El promedio de edades es {promedio}')
