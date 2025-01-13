"""
Un corredor da vueltas a una plaza 10 veces, en cada vuelta
cuenta la cantidad de pajaritos que vió.
- Cual fue la cantidad maxima de pajaritos que se vió 
  en una vuelta?
"""

# Inicializar variables que estan en la condicin del while
numero_vuelta = 0
cantidad_maxima = 0

# while CONDICION_LOGICA:
while numero_vuelta < 5:
    # [ Leer/Obtener otros datos necesarios ]
    cantidad = int(input("Ingrese pajaritos vistos: "))

    # El proceso repetitivo
    if cantidad >= cantidad_maxima:
        cantidad_maxima = cantidad

    print(cantidad, cantidad_maxima)

    # Actualizar las variables que estan en la condicion del while
    numero_vuelta = numero_vuelta + 1