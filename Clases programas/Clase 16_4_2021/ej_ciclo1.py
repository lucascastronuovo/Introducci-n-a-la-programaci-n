"""
Un corredor da vueltas a una plaza 10 veces, en cada vuelta
cuenta la cantidad de pajaritos que vió.
- Cual fue la cantidad maxima de pajaritos que se vió 
  en una vuelta?
"""

vuelta = 1
pajarosvueltas = []

while vuelta <= 10:
    pajaros = int(input("¿Cuántos pájaros vi en la vuelta", vuelta, "?: "))
    pajarosvueltas.append(pajaros)
    vuelta = vuelta + 1


print("La cantidad máxima de pajaritos que se vió en una vuelta fue: ", max(pajarosvueltas))


#El profe calculó el máximo mediante if, (mirar la programación que hizo)