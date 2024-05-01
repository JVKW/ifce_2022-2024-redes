"""Desenvolva um programa que:"""
# A. Leia 4 (quatro) números;
# B. Calcule o quadrado de cada um;
# C. Se o valor resultante do quadrado do terceiro for >= 1000, só imprima-o;
# D. Caso contrário, imprima os valores lidos e seus respectivos quadrados.

num1 = float(input("Valor do Primeiro: "))
num2 = float(input("Valor do Segundo: "))
num3 = float(input("Valor do Terceiro: "))

# Quadrados
qn1 = num1 ** 2
qn2 = num2 ** 2
qn3 = num3 ** 2

if qn3 >= 1000:
    print(f"Quadrado do 3º: {qn3}")
else:
    print(f"Quadrado do 1º: {qn1}")
    print(f"Quadrado do 2º: {qn2}")
