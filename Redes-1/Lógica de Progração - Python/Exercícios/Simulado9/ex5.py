"""Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas."""

# Exemplo: Saulo
# S
# SA
# SAU
# SAUL
# SAULO

name = str(input("Escreva um nome: "))
x = 0

for i in name:
    print(name[0: x + 1].upper())
    x = x + 1
