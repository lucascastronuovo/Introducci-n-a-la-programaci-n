'''
Convertir longitudes de millas a Km. y de pulgadas a cm., si:
1 milla = 1.60935 Km.
1 pulgada = 2.534 cm

'''
try:
    milla = float(input("Escriba la longitud de milla que desea convertir a kilómetros: "))
    pulgada = float(input("Escriba la longitud de pulgada que desea convertir a centímetros: "))

    km = milla * 1.60935
    cm = pulgada * 2.534

    print(milla, "milla/s son", km, "km y", pulgada, "pulgada/s son", cm, "cm")

except:
    print("Error")
