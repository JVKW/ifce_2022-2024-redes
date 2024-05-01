# 21/Setembro/2022

"""Faça um programa que receba um verbo regular no infinitivo e o conjugue no presente do indicativo. O programa deve
aceitar todas as conjugações (1a, 2a e 3a)."""

verbo = input("Digite um verbo regular: ") # amar

print(f"Eu {verbo[:-2]}o")
print(f"Tu {verbo[:-2]}as")
print(f"Ele {verbo[:-2]}a\n")

print(f"Nós {verbo[:-1]}mos")
print(f"Vós {verbo[:-1]}stes")
print(f"Eles {verbo[:-1]}m")

print("\nOBS: Caso alguma palavra tenha sido conjugada errada, verifique se a mesma é um verbo regular no infinitivo.")

"""....
Eu amo
Tu amas
Ele ama
Nós amamos
Vós amamais
Eles amam"""
