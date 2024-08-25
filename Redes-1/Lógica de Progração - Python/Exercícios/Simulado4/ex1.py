"""Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informa se o resultado foi um empate, a vitória do primeiro time ou do segundo time."""

time1 = int(input("Qual o placar do 1º Time? "))
time2 = int(input("Qual o placar do 2º Time? "))

if time1 > time2:
    print(f"O 1º Time venceu! {time1} - {time2}")
elif time1 == time2:
    print(f"Empate! Os dois times empataram! {time1} - {time2}")
elif time1 < time2:
    print(f"O 2º Time venceu! {time2} - {time1}")