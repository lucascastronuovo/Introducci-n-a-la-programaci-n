#Hallar la longitud de la hipotenusa de un triángulo dada la medida de sus catetos

try:
    cat1 = int(input("Escribe la medida de uno de los catetos del triángulo en cm: "))
    cat2 = int(input("Ahora escribe la medida del otro cateto en cm: "))

    c = pow(cat1,2) + pow(cat2,2)
    hipotenusa = pow(c,1/2)

    print("La longitud de la hipotenusa es de:", hipotenusa, "cm")


except:
    print("Error")