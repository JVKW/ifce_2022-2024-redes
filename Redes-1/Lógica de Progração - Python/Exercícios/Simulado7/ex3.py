"""Escreva um programa que pergunte um número ao usuário e imprima a soma de todos os números positivos até aquele número. Por exemplo, se o usuário digitar 10, a saída deve mostrar 55."""

x = 0
res = 0
num = int(input("Digite um número inteiro: "))

while x <= num:
    res = res + x
    x = x + 1
    print(res)

