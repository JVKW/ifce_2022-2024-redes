"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido."""

while True:
    resp = int(input("Digite uma nota entre 0 e 10: "))
    if (resp >= 0) and (resp <= 10):
        print("Nota Salva!")
        break
    elif (resp > 10) or (resp < 0):
        print("Informe um valor válido!")
        continue