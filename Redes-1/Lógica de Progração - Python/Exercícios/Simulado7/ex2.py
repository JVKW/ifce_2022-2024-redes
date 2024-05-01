"""Faça um programa que imprima o seguinte padrão de saída:
DICA: use um for/while dentro de outro."""
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

x = 1

for i in range(0, 5):
    x = 1
    for p in range(0, i + 1):
        print(x, end=" ")
        x = x + 1
    print("\r")
