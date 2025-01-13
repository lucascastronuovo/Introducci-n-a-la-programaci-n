#Calcular el importe que debe pagar una persona compra una heladera de pesos X y por pagar en efectivo le hacen el 10% de descuento ¿Cuánto abona? 

while True:
    try:
     costgenhel = int(input("Escribir el importe a pagar por la heladera: "))   
     desc = input("¿Va a pagar en efectivo para conseguir el descuento? (Responda por SI o por NO): ")   
     if desc == "SI":
         importe = costgenhel * 0.90
         print("Debe abonar: $", importe)
         break
     elif desc == "NO":
         importe = costgenhel
         print("Debe abonar: $", importe)
         break
     else:
         print("Por favor, responda por SI o por NO")
         continue
            

    except:
        print("No se pudo leer correctamente lo escrito")
        continue
