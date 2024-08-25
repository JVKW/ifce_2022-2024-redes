"""Faça um programa que leia o nome do usuário e mostre o nome de traz para frente, utilizando somente letras maiúsculas."""

# Exemplo: Saulo
# Saída: OLUAS

name = str(input("Escreva um nome: "))
print(f"Seu nome ao contrário: {name[::-1].upper()}")
