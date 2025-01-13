'''
Una ciudad se divide en tres zonas: 1, 2 y 3. En la zona 1, el metro cuadrado se cotiza a $1000. 
En la zona 2, se cotiza a $900, y en la zona 3 a $700. Una vez calculada la cotización, si esta 
supera el monto de $80000, se le aplica un 2% de impuesto para obtener el precio final del inmueble.
 Obtener el precio final de un inmueble si se ingresan la zona y la superficie del mismo.

  ¿Cuál sería el valor de la cartera de la inmobiliaria, si esta carga todas sus propiedades
   finalizando la carga con la zona igual a 0?
'''
total_cartera = 0

zona = int(input('Ingrese zona (1,2,3 o 0 para finalizar): '))
while not (zona >=0 and zona <=3):
    zona = int(input('Ingrese zona (1,2,3 o 0 para finalizar): '))

while zona != 0:
    superficie = float(input('Ingrese superficie: '))
    while not (superficie > 0):
        superficie = float(input('Ingrese superficie: '))

    if zona == 1:
        precio_propiedad = superficie * 1000
    elif zona == 2:
        precio_propiedad = superficie * 900
    elif zona == 3:
        precio_propiedad = superficie * 700

    if precio_propiedad > 80000:
        precio_propiedad *= 1.02    #  precio_propiedad = precio_propiedad * 1.02

    print(f'El valor de la propiedad es {precio_propiedad:.2f}')

    total_cartera += precio_propiedad

    zona = int(input('Ingrese zona (1,2,3 o 0 para finalizar): '))
    while not (zona >=0 and zona <=3):
        zona = int(input('Ingrese zona (1,2,3 o 0 para finalizar): '))

print(f'El valor total de la cartera es {total_cartera:.2f}')

