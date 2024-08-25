"""Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência."""

for i in range(5, 100):
    if (i % 7) == 0 and (i % 5) != 0:
        print(i)
