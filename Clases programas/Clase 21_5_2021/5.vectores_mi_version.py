numeros = [10, 40, 3, 66, 340, 70]

print(numeros[0])

segundo = numeros[1]
print(segundo)

print(numeros)

print('-' * 50)

for i in range(len(numeros)):
    print(numeros[i], end='\t')

print('-' * 50)

# Reemplazar los numeros pares del vector por su valor dividido 2
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros[i] = numeros[i] // 2

print(numeros)

print('-' * 50)

for nro in numeros:     # for each / para cada
    print(nro, end='\t')

# Determinar la  suma de todos los numeros pares en el vector
suma = 0
for nro in numeros:
    if nro % 2 == 0:
        suma += nro

print(f'la suma es {suma}')
