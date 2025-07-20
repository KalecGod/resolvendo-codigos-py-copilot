# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Se a Operação for (+,-,*,/), o resultado será: ")

operacao = input("Digite a operação desejada: ")

if operacao == "+":
    print("Resultado da soma:{:.2f}".format(num1 + num2))
elif operacao == "-":
    print("Resultado da subtração:{:.2f}".format(abs(num1 - num2)))
elif operacao == "*":
    print("Resultado da multiplicação:{:.2f}".format(num1 * num2))
elif operacao == "/":
    if num2 != 0:
        print("Resultado da divisão: {:.2f}".format(num1 / num2))
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")   