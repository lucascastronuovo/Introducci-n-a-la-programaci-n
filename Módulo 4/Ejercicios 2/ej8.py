#8) Ingresar las edades de 50 empleados de una empresa. Determinar cuál es el rango de edades y mostrarlo.


try:

    empleado = 2
    
    print("---------------------------")
    print("Empleado 1 :")
    edad = int(input("Edad del empleado: "))
    edadmin = edad
    edadmax = edad

    while empleado <= 50:
        print("---------------------------")
        print("Empleado", empleado, ":")
        edad = int(input("Edad del empleado: "))
        if edad <= 0:
            print("Error")
            break
        elif edadmin > edad:
            edadmin = edad
        elif edadmax < edad:
            edadmax = edad
        
            
        empleado = empleado + 1

    print("---")
    print("---")
    print("---")
    print("---")
    print("---")
    print("El rango de edades es de", edadmin, "a", edadmax, "años")

except:
    print("Error")     
