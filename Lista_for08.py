cont = 1

while cont <= 1:
    valor = int(input("Digite um valor positivo ate 50: "))

    if valor <= 0:
        print("Imprimiu valor errado, por favor digite um valor positivo até 50")
        continue
    else:
        break

divisores = []

while cont <= 100000:
    if valor % cont == 0:
        divisores.append(cont)
        cont += 1
    else:
        cont += 1
        continue

print(divisores)