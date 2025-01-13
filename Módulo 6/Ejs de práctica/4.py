"""
Diseñar un programa que permita ingresar las dimensiones de un ambiente
rectangular y calcular utilizando funciones:
a) La superficie del piso.
b) La superficie de las paredes.
c) El perímetro del ambiente.
d) El costo de alfombrar el ambiente si el metro cuadrado de una alfombra cuesta $104.
e) El costo pintar el ambiente sabiendo que un litro rinde 6 metros cuadrados y el litro
cuesta $83.


"""

def verificacion_de_valores(valor):
    
    while not valor > 0:
        print("¡Se ingresó como valor %d en uno de los input!:" %(valor))
        valor = float(input("Por favor, ingrese un valor mayor a 0: "))
    
    return valor
        

    

def superficie_piso_techo (b, h):
    superf_piso_techo = b * h

    return superf_piso_techo

def superficie_pared1(b, h):
    superficie_pared1 = b * h

    return superficie_pared1

def superficie_pared2 (b, h):
    superficie_pared2 = b * h

    return superficie_pared2


def costo_alfombra(superficie_piso):
    if superficie_piso >= 1:
       costo = (superficie_piso * 104) / 1
    else:
        print("No hay ni la superficie mínima para alfombrar")

    return costo


def costo_pintar_ambiente (superf_piso_techo, superf_pared1, superf_pared2):
    superf_total = superf_piso_techo * 2 + superf_pared1 * 2 + superf_pared2 * 2

    if superf_total >= 6:
       costo = (superf_total * 83) / 6
    else:
        print("No hay la superficie minima como para comprar, por lo menos, 1 litro de pintura y que se utilice por completo")
    
    return costo
    
    







def calculo_total (b_piso_techo_pared1, h_piso_techo_b_pared2, h_pared):
    b_piso_techo_pared1 = verificacion_de_valores(b_piso_techo_pared1)
    h_piso_techo_b_pared2 = verificacion_de_valores(h_piso_techo_b_pared2)
    h_pared = verificacion_de_valores(h_pared)
    

    perímetro = (b_piso_techo_pared1 * 4) + (h_piso_techo_b_pared2 * 4 ) + (h_pared * 4)

    print(f"a) La superficie del piso es {superficie_piso_techo(b_piso_techo_pared1, h_piso_techo_b_pared2)} m^2")
    print(f"b) La superficie de las paredes son {superficie_pared1(b_piso_techo_pared1, h_pared)} m^2 y {superficie_pared2(h_piso_techo_b_pared2, h_pared)} m^2")
    print(f"c) El prímetro del ambiente es de {perímetro} m")
    print(f"d) El costo de la alfombra es de {costo_alfombra(superficie_piso_techo(b_piso_techo_pared1, h_piso_techo_b_pared2))} $")
    print(f"e) El costo de pintar el ambiente es de {costo_pintar_ambiente(superficie_piso_techo(b_piso_techo_pared1, h_piso_techo_b_pared2), superficie_pared1(b_piso_techo_pared1, h_pared), superficie_pared2(h_piso_techo_b_pared2, h_pared)):.2f} $")





print("Escribir los valores en metros: ")
calculo_total(float(input("Base_piso/techo - Base_pared_1: ")), float(input("Altura_piso/techo - Base_pared_2: ")), float(input("Altura_pared: ")))

