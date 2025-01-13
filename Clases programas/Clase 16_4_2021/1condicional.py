
# No es necesario que en los otros elif aclares por ejemplo que 10 < numero ya que eso "se pregunta" en la línea anterior.
# Si el if que pide que número esté menor o igual a 10 y que sea mayor a 0 y si esto no se cumple, entonces va a ser
# un número que no pertenece a la decena y
# se debe "preguntar" por otra condición, ya no es necesario aclarar
# que el número debe ser más grande que 10 ya que si no se cumplió la condición anterior es porque es más grande 
# que 10 o será número negativo.
try:
    numero = int(input("Ingrese un número entero: "))
    if numero < 0:
        numero = numero * -1

    if 0 <= numero <= 10:
        print("Pertenece a la primera decena,", numero)
    elif numero <= 20:
        print("Pertenece a la segunda decena,", numero)
    elif numero <= 30:
        print("Pertenece a la tercera decena,", numero)
    elif numero <= 40:
        print("Pertenece a la cuarta decena,", numero)
    else:
        print("No pertenece a ninguna de las primeras 4 decenas,", numero)

except:
    print("Error")
