"""Faça um programa para ler uma string e dizer se ela é um número binário ou não."""

num = str(input("Digite um número binário: "))
x = 0

if '0' or '1' in num:
    for i in num:
        x =+ 1
        if (i != '0') and (i != '1'):
            print("Número não Binário!")
            break
        if x == len(num):
            print("Número Binário!")
