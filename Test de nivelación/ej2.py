nums = 0
num_mult3 = 0

try:
    while True:
        num = int(input("Ingrese un número: "))
        nums = nums + num
        if nums <= 500:
            numx = num % 3
            if numx == 0:
                num_mult3 = num_mult3 + num
            continue
        else:
            break

    print("Suma de los múltiplos de 3: ", num_mult3)

except:
    print("Error")