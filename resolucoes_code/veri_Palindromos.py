#Descrição: Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

palavra = input("Digite uma palavra: ")  # Passo 1: recebe a palavra
palavra_inver = palavra[::-1]

if palavra.lower() == palavra_inver.lower():  # Passo 2: compara ignorando maiúsculas/minúsculas
    print("É um palíndromo!")

else:
    print("Não é um palíndromo.")   

    