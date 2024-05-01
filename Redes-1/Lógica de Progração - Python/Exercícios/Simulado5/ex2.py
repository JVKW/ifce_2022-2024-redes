"""Elabore um programa que leia as variáveis C e N, respectivamente código e número de horas trabalhadas de um operário,
e calcule o salário sabendo-se que um operário ganha R$ 10,00 por hora. Quando o número de horas exceder a 50, calcule o
excesso de pagamento armazenando-o na variável. Caso contrário zerar tal variável. A hora excedente de trabalho vale
R$ 20,00. No final do processamento imprimir o salário total e o salário excedente."""

C = int(input("Digite o seu código: ")) # ???
Nh = int(input("Horas Trabalhadas: "))

Salario = (Nh*10)

if Nh > 50:
    Nex = Nh - 50
    Salario = Salario + (Nex * 20)
    print(f"\nVocê trabalhou: {Nh} Horas\nExcedência: {Nex} Horas\nSalário: R${Salario:.2f}")
else:
    print(f"Você trabalhou: {Nh} Horas\nSalário: R${Salario:.2f}")
    Nh = 0
    Salario = 0