# Pasaje por VALOR

def una_funcion(numero):
    numero = 123

def otra_funcion(texto):
    print('dentro:', texto)
    texto = 'desde la funcion'

x = 456
una_funcion(x)  # ---->  una_funcion(456)
print(x)

s = 'fuera'
otra_funcion(s) # ---->  otra_funcion('fuera')
print(s)
