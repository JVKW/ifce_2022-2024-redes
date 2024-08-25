"""Faça um programa que, a partir de um texto digitado pelo usuário, conte o número de caracteres total e o número de palavras (palavra é definida por qualquer sequência de caracteres delimitada por espaços em branco) e exiba o resultado."""

nome = str(input("Digite um nome: "))

print(f"Existem {len(nome.replace(' ', ''))} palavras nessa String.")
