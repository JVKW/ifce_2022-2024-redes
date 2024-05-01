# Faça um programa para ler uma string digitada pelo usuário e imprima o número de vogais da string.

name = str(input("Digite um nome: ").lower())

vogais = name.count('a') + name.count('e') + name.count('i') + name.count('o') + name.count('u')

print(f"Existem {vogais} nessa String.")


"""
OUTRA RESOLUÇÃO

quantidade = 0
texto = input("Digite um nome: ")

for v in "aeiou":
    quantidade += texto.count(v)

print(quantidade)
"""
