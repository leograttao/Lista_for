lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
repetido = 0
maior_repeticao = 0
for i in range(0, 11):
    repeticao = lista.count(i)
    if repeticao > maior_repeticao:
        maior_repeticao = repeticao
        repetido = i
print(repetido)