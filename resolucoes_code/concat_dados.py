# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!



print("Vamos receber dois dados diferentes do usuário e concatená-los em uma única string!")


nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ") 

nomeSobrenome = nome + " " + sobrenome 

print("O nome completo é:", nome+sobrenome)
print("O nome completo é:", nome + " " + sobrenome)
print("O nome completo é:", f"{nome} {sobrenome}")
print("O nome completo é:", "{} {}".format(nome, sobrenome))
print("O nome completo é:", " ".join([nome, sobrenome]))        



