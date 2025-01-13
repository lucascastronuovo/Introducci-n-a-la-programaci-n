

def calcular_promedio(cantidad):

    nota_acumuladas = 0
    
    for i in range(1, cantidad+1):
        nota = int(input("Ingrese nota: "))
        while not (nota <= 10 and nota > 0):
            nota = int(input("Ingrese nota: "))
        
        nota_acumuladas += nota

    if cantidad != 0:
        promedio = nota_acumuladas / cantidad
    else:
        promedio = "Error"

    return promedio


cantidad_notas = int(input("Cantidad de alumnos: "))

promedio_cod_principal = calcular_promedio(cantidad_notas)

print(promedio_cod_principal)