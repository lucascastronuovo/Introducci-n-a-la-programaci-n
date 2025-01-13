"""
Calcular el importe que debe pagar una persona compra una heladera 
de pesos X y por pagar en efectivo le hacen el 10% de descuento ¿Cuánto 
abona? 

"""


try:

    importe_base = float((input("Importe de la heladera a comprar: $")))

    pregunta = input("¿Vas a pagar en efectivo? (Responda por SI o por NO):  ")

    while not (pregunta == "SI" or pregunta == "NO"):
        pregunta = input("¿Vas a pagar en efectivo? (Responda por SI o por NO):  ")
    
    if pregunta == "SI":
        importe_a_abonar = importe_base * 0.90
    else:
        importe_a_abonar = importe_base

    print(f"Se debe abonar ${importe_a_abonar:.2f}")

except:
    print("Error")

