# Não revisado

"""Escreva um programa que, a partir de um nome informado pelo usuário, exiba suas
iniciais.

As iniciais são formadas pela primeira letra de cada nome, sendo que todas deverão
aparecer em maiúsculas na saída do programa. Note que os conectores e, do, da, dos,
das, de, di, du não são considerados nomes e, portanto, não devem ser considerados
para a obtenção das iniciais. As iniciais devem ser impressas em maiúsculas, ainda que o
nome seja entrado todos em maisculos.

Exemplos:
Maria das Graças Pimenta => MGP
João Carlos dos Santos => JCS
José da Silva => JS
Pedro Pereira Teixeira => PPT"""

nome = str(input("Digite o seu nome: ")).lower()
z = nome
conects = ["e", "dos", "da", "das", "de", "di", "du"]

for i in nome.split():
    if i in conects:
        z = z.replace((" " + i + " "), " ")

c = z
z = z.split()[0][0]
for i in c.split():
    z = z + i[0]

print(f"Suas iniciais: {z[1:].upper()}")
