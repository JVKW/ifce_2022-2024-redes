"""Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:"""

# Triângulo Equilátero: possui os 3 lados iguais.
# Triângulo Isóscele: possui 2 lados iguais.
# Triângulo Escaleno: possui 3 lados diferentes.

a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print("Não é um triângulo.")
elif (a == b) and (a == c):
    print("Triângulo Equilátero")
elif (a == b) or (b == c) or (c == a):
    print("Triângulo Isóscele")
elif (a != b) and (a != c):
    print("Triângulo Escaleno")