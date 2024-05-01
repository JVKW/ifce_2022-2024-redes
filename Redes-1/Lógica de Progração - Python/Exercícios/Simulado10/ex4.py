"""Faça um programa para ler uma string digitada pelo usuário e imprima se a string digitada começa com “UNI”
(ignorando maiúsculas/minúsculas)."""

nome = input("Digite um nome: ").upper()

if nome.startswith("UNI"):
    print("A string começa com UNI")

