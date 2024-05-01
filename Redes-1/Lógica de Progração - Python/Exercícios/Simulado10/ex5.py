"""Faça um programa para ler uma string digitada pelo usuário e imprima se a string digitada termina com “RIO”
(ignorando maiúsculas/minúsculas). """

nome = str(input("Digite um nome: ").upper())

if nome.endswith("RIO"):
    print("A string termina com 'RIO'.")
