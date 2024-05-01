# Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = int(input("Digite outro número inteiro: "))

if (num1 > num2) and (num1 > num3):
    print(f"O primeiro número é maior! ({num1})")
elif (num2 > num1) and (num2 > num3):
    print(f"O segundo número é maior! ({num2})")
elif (num3 > num1) and (num3 > num2):
    print(f"O terceiro número é maior! ({num3})")
else:
    print("Os números são iguais!")

if (num1 < num2) and (num1 < num3):
    print(f"O primeiro número é menor! ({num1})")
elif (num2 < num1) and (num2 < num3):
    print(f"O segundo número é menor! ({num2})")
elif (num3 < num1) and (num3 < num2):
    print(f"O terceiro número é menor! ({num3})")
else:
    print("Os números são iguais!")