# Escreva um programa que dado um valor numérico digitado pelo usuário (armazenado em uma variável inteira), imprima cada um dos seus dígitos por extenso.

# Por exemplo:
# Entre o número: 4571
# Resultado: quatro, cinco, sete, um

num = str(input("Digite um número: "))

numex = num.replace("0", " Zero")
numex = numex.replace("1", " Um")
numex = numex.replace("2", " Dois")
numex = numex.replace("3", " Três")
numex = numex.replace("4", " Quatro")
numex = numex.replace("5", " Cinco")
numex = numex.replace("6", " Seis")
numex = numex.replace("7", " Sete")
numex = numex.replace("8", " Oito")
numex = numex.replace("9", " Nove")
numex = numex.replace(" ", ", ")

print(numex[1:])

