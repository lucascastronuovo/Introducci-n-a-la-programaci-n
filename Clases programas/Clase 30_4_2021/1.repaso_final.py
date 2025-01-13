'''
Una ciudad se divide en tres zonas: 1, 2 y 3. En la zona 1, el metro cuadrado se cotiza a $1000. 
En la zona 2, se cotiza a $900, y en la zona 3 a $700. Una vez calculada la cotización, si esta 
supera el monto de $80000, se le aplica un 2% de impuesto para obtener el precio final del inmueble.
 Obtener el precio final de un inmueble si se ingresan la zona y la superficie del mismo.

  ¿Cuál sería el valor de la cartera de la inmobiliaria, si esta carga todas sus propiedades
   finalizando la carga con la zona igual a 0?
'''


def determinar_precio(sup, zona):

    if zona == 1:
        precio = 1000 * sup
    elif zona == 2:
        precio = 900 * sup
    elif zona == 3:
        precio = 700 * sup
    
    if precio > 80000:
        precio *= 1.02

    return precio




def main():
    total_cartera = 0

    zona = int(input("Zona (3 - 2 - 1 - 0 (finalizar)): "))
    while not (zona >= 0 and zona <= 3):
        zona = int(input("Zona (3 - 2 - 1 - 0 (finalizar)): "))


    while zona != 0:
        superficie = float(input("Superficie: "))
        precio_final_inmueble = determinar_precio(superficie, zona)

        print(f"El inmueble ingresado tiene un precio de ${precio_final_inmueble:.2f}")

        total_cartera += precio_final_inmueble

        zona = int(input("Zona (3 - 2 - 1 - 0 (finalizar)): "))
        while not (zona >= 0 and zona <= 3):
            zona = int(input("Zona (3 - 2 - 1 - 0 (finalizar)): "))


    print()
    print(f"El valor total de la cartera inmobiliaria es de {total_cartera}")




main()