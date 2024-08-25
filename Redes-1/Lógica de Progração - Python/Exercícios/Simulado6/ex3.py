"""Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B ao final do calculo atribuir o valor para uma variável C, e exibir o resultado na tela."""

A = float(input("Digite um número: "))
B = float(input("Digite outro número: "))

if A == B:
    C = A + B
    print(f"Soma de A + B: {C}")
else:
    C = A * B
    print(f"Multiplicando A * B: {C}")
