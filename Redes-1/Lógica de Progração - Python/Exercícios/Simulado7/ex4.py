"""Escreva um programa que pergunte um número ao usuário e imprima a tabuada daquele número. Por exemplo, se o usuário digitar 2, o programa imprime:"""

# 1 x 2 = 2
# 2 x 2 = 4
# 3 x 2 = 6
# 4 x 2 = 8
# 5 x 2 = 10
# ...
# 10 x 2 = 20

num = int(input("Digite um número inteiro: "))

for i in range(1, 11):
    print(f"{i} x {num} = {i * num}")