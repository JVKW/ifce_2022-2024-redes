"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turn = str(input("Qual turno você estuda?\n[M]Matutino\n[V]Vespertino\n[N]Nortuno\n> "))

if turn in "Mm":
    print("Bom dia!")
elif turn in "Vv":
    print("Boa tarde!")
elif turn in "Nn":
    print("Boa noite!")
else:
    print("Digite um dos turnos citados!")