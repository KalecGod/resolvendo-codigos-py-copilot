# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
divisao = num1 / num2
multiplicacao = num1 * num2
subtracao = num1 - num2

print("A soma é: {:.2f}".format(soma))
print("A divisão é: {:.2f}".format(divisao))
print("A multiplicação é: {:.2f}".format(multiplicacao))
print("A subtração é: {:.2f}".format(subtracao))