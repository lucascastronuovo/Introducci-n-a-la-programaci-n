#Calcular el sueldo de una persona, conociendo la cantidad de horas que trabaja en el mes y el valor de la hora

#Preguntas: ¿Hay alguna forma de poner los símbolos, por ejemplo, de $ y el que representa la hora? ¿Y también hay alguna forma de separar los miles con puntos o comas?

horxm = int(input("Ingrese la cantidad de horas que trabaja en el mes: "))
valhor = int(input("Valor de la hora: "))

sueldo = horxm * valhor

print("Tu sueldo es: $", sueldo)