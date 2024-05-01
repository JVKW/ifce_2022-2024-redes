"""Escreva um programa para descobrir a maior e a menor palavra de uma string lida pelo usuário."""

txt = str(input("Digite um nome: "))
maior = txt.split()
menor = txt.split()

for x in txt.split():
    if len(x) > len(maior):
        maior = x

    if len(x) < len(menor):
        menor = x

print(f"A maior palavra: {maior}\nA menor palavra: {menor}")
