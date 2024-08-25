"""Crie um programa que exibe se um dia é dia útil, fim de semana ou dia inválido dado o número referente ao dia. Considere que domingo é o dia 1 e sábado é o dia 7."""

dia = int(input("Informe um dia: "))

if (dia % 7 or dia % 6) == 0 or dia == 1 or dia == 7:
    print("Final de Semana!")
else:
    print("É um dia útil!")
