"""Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:"""

# Para homens: (72,7 * Altura) – 58
# Para mulheres: (62,1 * Altura) – 44,7

sex = int(input("Qual o seu sexo? \n[1] Feminino\n[2] Masculino\n> "))
height = float(input("Digite sua altura(ex: 1.90): "))

if sex == 2:
    print(f"IM: {height} é: {(72.7*height)-58:.2f}kg")
elif sex == 1:
    print(f"IM: {height} é: {(62.1*height)-44.7:.2f}kg")