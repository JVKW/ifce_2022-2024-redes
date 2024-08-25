"""Crie um algoritmo que leia um número entre 0 e 60 e imprima o seu sucessor, sabendo que para este caso, o sucessor de 60 é 0."""

num = int(input("Digite um número entre 0 e 60: "))

if num >= 60:
    sucessor = num - 60
    print(f"Sucessor: {sucessor}")
elif num >= 0 <= 59:
    print(f"Sucessor: {num + 1}")

