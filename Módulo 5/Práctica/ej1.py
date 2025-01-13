"""
Ejercicio resuelto
En un relevamiento inmobiliario se obtienen los siguientes datos de los inmuebles a 
la venta en la ciudad de Buenos Aires:
 Tipo de inmueble ( Casa – Depto. - PH)
 Cantidad de ambientes (1-2-3-4)
 Precio
 Barrio
Diseñar un programa que permita ingresar los datos hasta que el tipo de inmueble 
sea NNN y el barrio sea ZZZ, y calcule y muestre:
a) El precio promedio por tipo de inmueble XXXXX
b) El precio promedio del barrio de Palermo según la cantidad de ambientes XXXXX
c) De todas las casas que porcentaje son de Villa Crespo XXXXX
d) El nombre del Barrio cuyo departamento de 4 ambientes es el más caro XXXXX
e) La cantidad de ambientes y el nombre del barrio del departamento más económico XXXXX
f) El valor total de las casas del barrio de Flores XXXXX
g) En el barrio de Almagro ¿qué porcentaje de PH hay?

"""

inmueble = 1

precio_total_casa = 0

precio_total_depto = 0

precio_total_ph = 0

num_inmueble_casa = 0

num_inmueble_depto = 0

num_inmueble_ph = 0

precio_total_palermo_ambiente1 = 0

precio_total_palermo_ambiente2 = 0

precio_total_palermo_ambiente3 = 0

precio_total_palermo_ambiente4 = 0

ambiente1_palermo = 0

ambiente2_palermo = 0

ambiente3_palermo = 0

ambiente4_palermo = 0

casas_de_villcrespo = 0

mas_caro_4ambientes = 0

nombre_barrio_4amb_mas_caro = ""

depto_mas_economico = 9999999


valor_total_casas_flores = 0

num_inmueble_ph_almagro = 0

for i in range(0,9):
        print("-")

print(f"Datos de inmuebles a la venta - Inmueble {inmueble:d}:")

tipo_inmueble = input("Tipo de inmueble (Casa – Depto. - PH) [NNN para salir]: ")

while not (tipo_inmueble == "Casa" or tipo_inmueble == "Depto." or tipo_inmueble == "PH" or tipo_inmueble == "NNN"):
    tipo_inmueble = input("Tipo de inmueble (Casa – Depto. - PH): ")

cant_ambientes = int(input("Cantidad de ambientes (1-2-3-4): "))

while not (1 <= cant_ambientes <= 4):
    cant_ambientes = int(input("Cantidad de ambientes (1-2-3-4): "))

precio = int(input("Precio: $"))

while not (precio > 0):
    precio = int(input("Precio: $"))

barrio = input("Barrio [ZZZ para salir]: ")


while tipo_inmueble != "NNN" and barrio != "ZZZ":
    if tipo_inmueble == "Casa":
        precio_total_casa += precio
        num_inmueble_casa += 1

    elif tipo_inmueble == "Depto.":
        precio_total_depto += precio
        num_inmueble_depto += 1

    elif tipo_inmueble == "PH":
        precio_total_ph += precio
        num_inmueble_ph += 1

    
    if barrio == "Palermo":
        if cant_ambientes == 1:
            precio_total_palermo_ambiente1 += precio
            ambiente1_palermo += 1

        elif cant_ambientes == 2:
            precio_total_palermo_ambiente2 += precio
            ambiente2_palermo += 1

        elif cant_ambientes == 3:
            precio_total_palermo_ambiente3 += precio
            ambiente3_palermo += 1
        
        elif cant_ambientes == 4:
            precio_total_palermo_ambiente4 += precio
            ambiente4_palermo += 1


    if tipo_inmueble == "Casa" and barrio == "Villa Crespo":
        casas_de_villcrespo += 1


    if cant_ambientes == 4 and tipo_inmueble == "Depto." and precio >= mas_caro_4ambientes:
        mas_caro_4ambientes = precio
        nombre_barrio_4amb_mas_caro = barrio

    if tipo_inmueble == "Depto." and depto_mas_economico >= precio:
        cant_ambientes_depto_economico = cant_ambientes
        barrio_depto_economico = barrio
        depto_mas_economico = precio

    if barrio == "Flores" and tipo_inmueble == "Casa":
        valor_total_casas_flores += precio

    if tipo_inmueble == "PH" and barrio == "Almagro":
        num_inmueble_ph_almagro += 1
    
    for i in range(0,5):
        print("-")

    print(f"Datos de inmuebles a la venta - Inmueble {inmueble:d}:")

    tipo_inmueble = input("Tipo de inmueble (Casa – Depto. - PH) [NNN para salir]: ")

    while not (tipo_inmueble == "Casa" or tipo_inmueble == "Depto." or tipo_inmueble == "PH" or tipo_inmueble == "NNN"):
        tipo_inmueble = input("Tipo de inmueble (Casa – Depto. - PH): ")

    cant_ambientes = int(input("Cantidad de ambientes (1-2-3-4): "))

    while not (1 <= cant_ambientes <= 4):
        cant_ambientes = int(input("Cantidad de ambientes (1-2-3-4): "))

    precio = int(input("Precio: $"))

    while not (precio > 0):
        precio = int(input("Precio: $"))

    barrio = input("Barrio [ZZZ para salir]: ") 


if num_inmueble_casa > 0:
    precio_promedio_casa = (precio_total_casa / num_inmueble_casa)
else:
    precio_promedio_casa = "No se puede calcular el promedio"

if num_inmueble_depto > 0:
    precio_promedio_depto = (precio_total_depto / num_inmueble_depto)
else:
    precio_promedio_depto = "No se puede calcular el promedio"

if num_inmueble_ph > 0:
    precio_promedio_ph = (precio_total_ph / num_inmueble_ph)
else:
    precio_promedio_ph = "No se puede calcular el promedio"


if ambiente1_palermo > 0:
    precio_promedio_palermo_ambiente1 = (precio_total_palermo_ambiente1 / ambiente1_palermo)
else:
   precio_promedio_palermo_ambiente1 = "No se puede calcular el promedio"

if ambiente2_palermo > 0:
    precio_promedio_palermo_ambiente2 = (precio_total_palermo_ambiente2 / ambiente2_palermo)
else:
    precio_promedio_palermo_ambiente2 = "No se puede calcular el promedio"

if ambiente3_palermo > 0:
    precio_promedio_palermo_ambiente3 = (precio_total_palermo_ambiente3 / ambiente3_palermo)
else:
   precio_promedio_palermo_ambiente3 = "No se puede calcular el promedio"

if ambiente4_palermo > 0:
    precio_promedio_palermo_ambiente4 = (precio_total_palermo_ambiente4 / ambiente4_palermo)
else:
    precio_promedio_palermo_ambiente4 = "No se puede calcular el promedio"
    


if casas_de_villcrespo > 0 and num_inmueble_casa > 0:
    porcentaje_casa_villacrespo = (casas_de_villcrespo * 100) / num_inmueble_casa
else:
    porcentaje_casa_villacrespo = "No se puede calcular el porcentaje"

if num_inmueble_ph_almagro > 0 and num_inmueble_ph > 0:
    porcentaje_ph_almagro = (num_inmueble_ph_almagro * 100) / num_inmueble_ph
else:
    porcentaje_ph_almagro = "No se puede calcular el porcentaje"



for i in range(0,9):
        print("-")


print("El precio promedio de casas es $", precio_promedio_casa, ", el de departamentos es $", precio_promedio_depto, "y el de ph es $", precio_promedio_ph)

for i in range(0,5):
        print("-")


print("El precio promedio del barrio de Palermo en inmuebles de 1 ambiente es $", precio_promedio_palermo_ambiente1, ", el de 2 ambientes es $", precio_promedio_palermo_ambiente2, ", el de 3 ambientes es $", precio_promedio_palermo_ambiente3, "y el de 4 ambientes es $", precio_promedio_palermo_ambiente4)

for i in range(0,5):
        print("-")

print("El porcentaje de casas de Villa Crespo es de", porcentaje_casa_villacrespo, "%")

for i in range(0,5):
        print("-")

print("El depto más caro de 4 ambientes es de $", mas_caro_4ambientes, "y se encuentra en el barrio", nombre_barrio_4amb_mas_caro)

for i in range(0,5):
        print("-")

print("La cantidad de ambientes del depto más económico es de", cant_ambientes_depto_economico, "ambientes y se encuentra en el barrio", barrio_depto_economico)

for i in range(0,5):
        print("-")

print("El valor total de las casas del barrio Flores es de $", valor_total_casas_flores)

for i in range(0,5):
        print("-")

print("El porcentaje de ph que hay en el barrio Almagro es de", porcentaje_ph_almagro, "%")

for i in range(0,5):
        print("-")




 
    





    



    

    


    


        
        



    

    







