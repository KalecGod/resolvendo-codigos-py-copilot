

inicio = 0
nota = 0.0
for i in range(inicio, 3):


   nota+= float(input("Digite a nota do aluno: "))


print(f"A média do aluno é: {nota/3:.2f}")

if nota/3 >= 7:
    print("O aluno está aprovado.")
elif  nota/3 < 7:    
    print("O aluno está recuperação.")
else :
    print("O aluno está reprovado.")    

