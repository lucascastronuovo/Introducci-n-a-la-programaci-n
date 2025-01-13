"""
4) Al terminar un día en un colegio secundario se hace una estadística de faltas sabiendo 
de cada curso:
 Curso (1-5)
 Presentes
 Ausentes 
Calcular
 Por cada curso el porcentaje de presentes sobre el total
 Cantidad de ausentes en el colegio
 Curso con mayor cantidad de ausente
"""

try:
    cantausent = 0
    curso = 1
    curs_mayor_ausent = 0
    while curso <= 5:
        print("Curso", curso, ": ")
        total = int(input("Total del Curso: "))
        presentes = int(input("Presentes: "))
        if presentes > total:
            print("Error")
            continue
        else:
            ausentes = (total - presentes)
            if ausentes > total:
                print("Error")
                continue
            else:
                porcentajepres = (presentes * 100) / total 
                cantausent = cantausent + ausentes
                if curs_mayor_ausent < ausentes:
                    curs_mayor_ausent = ausentes
                if curso == 1:
                    porcentajeprescur1 = porcentajepres
                elif curso == 2:
                    porcentajeprescur2 = porcentajepres
                elif curso == 3:
                    porcentajeprescur3 = porcentajepres
                elif curso == 4:
                    porcentajeprescur4 = porcentajepres
                elif curso == 5:
                    porcentajeprescur5 = porcentajepres

            curso = curso + 1
    print("-")
    print("-")
    print("-")
    print("-")
    print("-")
    print("-")
    print("Porcentaje de presentes: ")
    print("Curso 1:", porcentajeprescur1, "%")
    print("Curso 2:", porcentajeprescur2, "%")
    print("Curso 3:", porcentajeprescur3, "%")
    print("Curso 4:", porcentajeprescur4, "%")
    print("Curso 5:", porcentajeprescur5, "%")
    print("-")
    print("-")
    print("-")
    print("Cantidad de ausentes en el colegio:", cantausent)
    print("-")
    print("-")
    print("-")
    print("Curso con mayor cantidad de ausentes:", curs_mayor_ausent)


        

        
except:
    print("Error")
