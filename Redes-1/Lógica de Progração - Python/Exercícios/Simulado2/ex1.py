"""Elabore um programa para somar dois números inteiros (informados pelo usuário) e mostrar o valor da soma na tela. Caso a soma dos números seja maior que 10 mostrar uma mensagem informativa na tela: “A soma dos números digitados é maior que 10”."""

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

res = num1 + num2
if res > 10:
    print(res)
    print("A soma dos números digitados é maior do que 10.")