# Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor.

num1 = float(input("Digite um número: ")) # Float para fora ilimitação do usuário.
num2 = float(input("Digite outro número: "))

if num1 > num2:
    print(f"O valor de {num1} é maior do que {num2}.")
elif num1 < num2:
    print(f"O valor de {num1} é menor do que {num2}.")