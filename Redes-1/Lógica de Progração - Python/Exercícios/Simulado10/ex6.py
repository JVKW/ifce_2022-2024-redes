# Faça um programa para ler uma string digitada pelo usuário e imprima o número de dígitos (0 a 9) da string.

nome = str(input("Digite um nome: "))
q = 1

for x in nome:
    print(q)
    q = q + 1
    if q == 10:
        break
