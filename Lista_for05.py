somaPar = 0
somaImpar = 0

for quant in range(1, 11):
   
    n = int(input("Digite 10 numeros para saber quantos são pares ou ímpares: "))
    
    if n % 2 == 0:
        somaPar += 1
    else:
        somaImpar += 1

print(f"Você falou {somaPar} números pares")
print(f"Você falou {somaImpar} números ímpares")