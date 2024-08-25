"""Faça um programa que leia uma frase (isso implica que o usuário digitará mais de uma palavra) e mostre a frase no sentido inverso."""

# Exemplo:
# A tirei o pau no gato
# gato no pau Atirei

nome = str(input("Digite um nome: "))

x = nome.split()[::-1]

print(f"Nome inverso: {' '.join(x)}")
