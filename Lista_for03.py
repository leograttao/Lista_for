for i in range(1000):
   
    numero = int(input("Digite um número entre 1 e 10 para descobrir a tabuada: "))
    
    if numero > 10 or numero < 1:
        print("\nValor inválido\n")
        continue
    else:
        break
        
for n in range(1,11):

    print(f"{numero} X {n} = {numero * n}")
            