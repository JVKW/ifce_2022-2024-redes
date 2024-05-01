"""Faça um programa para ler uma strings e que ele modifique todos os caracteres por *."""

txt = str(input("Digite um um texto: "))
x = txt

for i in txt:
    if i == " ":
        continue
    else:
        x = x.replace(i, "*")

print(x)
