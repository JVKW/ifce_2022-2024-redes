"""Faça um programa para ler um número inteiro (posição) e depois uma string. Verifique se é possível remover o
caractere na posição indicada pelo número. Se isso poder ser realizado, imprima a string sem a letra daquela posição.
Caso contrário, imprima que não pode realizar essa operação."""

txt = str(input("Digite um nome: "))
num = int(input("Digite um número inteiro: "))

if len(txt) >= num > 0:
    print(f"É possível trocar a letra ({txt[num-1]}) desta posição.")
elif num > len(txt) or num <= 0:
    print(f"Não é possível trocar a letra desta posição.")
