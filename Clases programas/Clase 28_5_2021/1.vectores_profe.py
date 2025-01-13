# Pasaje por referencia

def dividir(vector, numero):
    for i in range(len(vector)):      # 0...len-1
        vector[i] = vector[i] // numero


v1 = [10, 20, 30, 40, 50]
print(v1)

dividir(v1, 2)

print(v1)
