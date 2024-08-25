"""Escreva um programa que calcule a raiz quadrada de um número. Não pode usar o **. Utilize o método de Newton para obter um resultado aproximado. O algoritmo funciona da seguinte forma:"""

# a) Sendo n o número a obter a raiz quadrada, considere a base b=2.
# b) Calcule p usando a fórmula p = (b + (n/b)) / 2.
# c) Agora, calcule o quadrado de p.

n = int(input("Digite um Número: "))
b = 2

while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
    print(p)

print(f"A raiz quadrada de {n} é aproximado de {p:.8f}")
