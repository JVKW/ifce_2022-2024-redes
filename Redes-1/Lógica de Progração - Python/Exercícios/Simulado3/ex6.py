# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

if (num1 > num2) and (num2 > num3) and (num3 < num1):
    print(f"Forma Descrecente: {num1} - {num2} - {num3}")
elif (num1 > num2) and (num3 > num2) and (num3 < num1):
    print(f"Forma Descrecente: {num1} - {num3} - {num2}")
elif (num2 > num3) and (num3 > num1) and (num3 < num2):
    print(f"Forma Descrecente: {num2} - {num3} - {num1}")
elif (num2 > num3) and (num1 > num3) and (num3 < num2):
    print(f"Forma Descrecente: {num2} - {num1} - {num3}")
elif (num3 > num2) and (num2 > num1) and (num1 < num2):
    print(f"Forma Descrecente: {num3} - {num2} - {num1}")
elif (num3 > num2) and (num1 > num2) and (num2 < num3):
    print(f"Forma Descrecente: {num3} - {num1} - {num2}")
elif (num1 == num2) and (num2 == num3) and (num1 == num3):
    print(f"Todos os números são iguais!")
