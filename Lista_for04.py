quant_idade = int(input("Quantas idades vai falar: "))
idade = 0

for cont in range(quant_idade):
    
    idades = int(input("Digite sua idade: "))
    idade += idades

media = idade // quant_idade
    
print(f"A média da suas idades é: {media}")