"""
2) Calcular el promedio semanal de gastos en un mes, ingresando como datos:
 Semana número
 Gasto semanal
El proceso termina cuando “semana número” es igual a 5.

"""

try:
    semana = 0
    gastost = 0
    while semana < 5:
        gastos = int(input("Gasto Semanal: "))
        gastost = gastost + gastos
        semana = semana + 1
    promedio = gastost / 5
    print("El promedio semanal de gastos en un mes es de: $", promedio)

except:
    print("Error")
        