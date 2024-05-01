"""Criar um programa para identificar se um mês digitado pelo usuário é de alta ou baixa temporada (considerar os
seguintes meses como alta temporada: dezembro a fevereiro, junho e julho)."""

mes = input(("Digite um mês: "))

al_temp = (2, 7, 6, 12)

if mes in al_temp:
    print(f"Alta temporada!")
else:
    print("Baixa temporada!")
