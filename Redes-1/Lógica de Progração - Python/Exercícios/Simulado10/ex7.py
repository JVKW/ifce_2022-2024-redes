"""Faça um programa para ler uma string digitada pelo usuário e imprima se a string é um palíndromo ou não. Um palíndromo diz-se de ou frase ou palavra que se pode ler,indiferentemente, da esquerda para a direita ou vice-versa."""

nome = str(input("Digite um nome: "))

if nome[::-1] == nome:
    print("Esse texto é um palídromo.")
else:
    print("Esse nome não é um palídromo.")
