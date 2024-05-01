"""Faça um programa para ler uma string e conte quantos caracteres tem sem contar os espaços."""

txt = str(input("Digite um um texto: ")).replace(" ", "")

print(f"Existem {len(txt)} letras neste nome.")
