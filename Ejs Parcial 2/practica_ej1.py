"""
Se quiere procesar la venta de remeras lisas y estampadas de una tienda de ropa. Se quiere procesar la información mensualmente (31 días).

Se carga la cantidad vendida por día. (Utilizando arreglos)
Se ingresa L para indicar remera lisa y E para indicar remera estampada. (Un vector para cada tipo)
Se pide calcular el máximo vendido en el mes para un tipo de remera, mostrar el día del mes al que corresponde. (Resolver con funciones)
Calcular el promedio mensual en pesos, sabiendo que el costo de las remeras lisas es $350 y las estampadas $385. (Resolver con funciones).
Determinar en pesos de cual producto se vendió más.
"""



def main():
    remer_lisas = []
    remer_estampadas = []
    for dia in range(1, 31+1):

        print(f"Día {dia}: ")

        tipo = input("Tipo de remera a comprar: Lisa (L) - Estampada (E): ")

        while not (tipo == "L" or tipo == "E"):
            tipo = input("Tipo de remera a comprar: Lisa (L) - Estampada (E): ")

        if tipo == "L":
            cantidad = int(input("Cantidad: "))
            while not cantidad > 0:
                cantidad = int(input("Cantidad: "))

            remer_lisas.append(cantidad)
        elif tipo == "E":
            cantidad = int(input("Cantidad: "))
            while not cantidad > 0:
                cantidad = int(input("Cantidad: "))

            remer_estampadas.append(cantidad)


            



            


            

            

            


main()    



        


