"""Escreva um programa que pergunte o dia, mês e ano do aniversário de uma pessoa e diga se a data é válida ou não.
Caso não seja, diga o motivo (Dia inexistente, mês inexistente, ano inexistente). Suponha que todos os meses tem 31 dias
e que estejamos no ano de 2021 e ninguém nasceu antes de 1921."""

ano = int(input("Ano do Aniverssário: "))
mes = int(input("Mês do Aniverssário: "))
dia = int(input("Dia do Aniverssário: "))

if ano < 1921:
    print("Digite um ano Existente!")
elif mes < 1 or mes > 12:
    print("Digite um Mês exato!")
elif dia < 1 or dia > 31:
    print("Digite um dia exato!")
else:
    print("Data Salva!")
    print(f"{dia}/{mes}/{ano}")