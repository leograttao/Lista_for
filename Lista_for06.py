somaEntre = 0
somaFora = 0

for n in range(1, 11):
    numero = int(input("Digite um numero: "))

    if 10 <= numero <= 20:
        somaEntre += 1
    else:
        somaFora += 1

print(f"Você digitou {somaEntre} entre 10 e 20")
print(f"Você digitou {somaFora} fora do intervalo de 10 e 20")