"""João Papo-de-Pescador, homem de bem, comprou um laptop da Apple para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do Trici (50 quilos) deve
pagar um multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
P (peso de peixes) e verifique se há excesso. Se houver, gravar na variável E (Excesso) e na variável M o valor da multa
que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO."""

P = float(input("Digite o Peso dos Peixes: "))

if P > 50:
    Ex = P - 50
    Mu = Ex * 4.00
    print(f"Você está carregando Excesso de Peso!\nEx: {Ex}kg\nValor da Multa: R${Mu:.2f}")
else:
    print(f"Sem Excesso de peso.\nPeso: {P}kg")
