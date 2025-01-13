'''
 Realizar funciones que cumplan las siguientes tareas, y además mostrar su uso mediante un ejemplo:
a.    Debe leer un numero de teclado y devolverlo siempre y cuando sea múltiplo del recibido por parámetro, 
  caso contrario debe volver a pedirlo.
b.    Recibe 3 argumentos y retorna el mayor de ellos.
c.    Debe leer 3 números y con el mayor de ellos leer otro número que sea múltiplo de ese número y devolverlo.
'''

# Funciones
def leer_multiplo(divisor):
    '''
    Esta funcion lee numeros desde teclado hasta

    que uno de ellos sea multiplo de parametro 'divisor'
    '''
    numero = int(input(f'Ingrese un numero multiplo de {divisor}: '))
    while numero % divisor != 0:
        numero = int(input(f'Ingrese un numero multiplo de {divisor}: '))
    
    return numero

def calcular_mayor(a, b, c):
    '''
    Determina el mayor de los parametros a,b,c que recibe

    la funcion.
    '''
    numero_mayor = a
    if numero_mayor < b:
        numero_mayor = b
    if numero_mayor < c:
        numero_mayor = c
    
    return numero_mayor

def calcular_mayor_version2(a, b, c):
    if a>b and a>c:
        return a          # Tratar de evitar return's en el medio del codigo
    
    if b>a and b>c:
        return b

    return c

#  Debe leer 3 números y con el mayor de ellos leer otro número que sea múltiplo de ese número y devolverlo.
def leer_numeros():
    x = int(input('Ingrese primer numero: '))
    y = int(input('Ingrese segundo numero: '))
    z = int(input('Ingrese tercer numero: '))

    mayor = calcular_mayor(x, y, z)       # Pasaje por valor
    multiplo = leer_multiplo(mayor)

    return multiplo


# Programa principal

numero = leer_numeros()
