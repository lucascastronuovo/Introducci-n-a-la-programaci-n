#Ingresar las edades de dos personas. Si una de ellas es mayor de edad y la otra menor de edad, calcular y mostrar su promedio. En caso contrario mostrar las dos edades. 

try:
    per1 = int(input("Ingrese la edad de la primera persona: "))
    per2 = int(input("Ahora ingrese la edad de la otra persona: "))

    if per1 >= 18 and 0 <= per2 < 18:
        promedio = (per1 + per2) / 2
        print("El promedio de las edades es:", promedio)
    elif 0 <= per1 < 18 and per2 >= 18:
        promedio = (per1 + per2) / 2
        print("El promedio de las edades es:", promedio)
    elif per1 < 0 or per2 < 0:
        print("Por favor escriba edades, no números negativos")
    elif per1 < 0 and per2 < 0:
        print("Por favor escriba edades, no números negativos")
    else:
        print("Las edades de las dos personas son:", per1, "año/s y", per2, "año/s")


except:
    print("Error")
    
    
