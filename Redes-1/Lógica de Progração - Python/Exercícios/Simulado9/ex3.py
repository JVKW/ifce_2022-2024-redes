"""Faça um programa que receba do usuário uma string. O programa deve imprimir a string sem suas vogais."""

name = str(input("Escreva um nome: "))

name = name.lower().replace("a", "")
name = name.lower().replace("e", "")
name = name.lower().replace("i", "")
name = name.lower().replace("o", "")
name = name.lower().replace("u", "")

print(f"Seu nome sem as Vogais: {name}")