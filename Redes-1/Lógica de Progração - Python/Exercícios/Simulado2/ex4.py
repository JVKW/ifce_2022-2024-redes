"""Para doar sangue é necessário ter entre 18 e 67 anos. Faça um programa que pergunte a idade de uma pessoa e diga
se ela pode doar sangue ou não."""

idade = int(input("Qual a sua idade? "))

if idade >= 18 and idade <= 67:
    print("Pode doar sangue.")
else:
    print("Não pode doar sangue!")