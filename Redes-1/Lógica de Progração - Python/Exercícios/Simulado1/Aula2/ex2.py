# Faça um algoritmo que receba duas notas e seus respectivos pesos, calcule e mostre a média ponderada.

nota1 = float(input("Digite a 1º nota: "))
peso1 = float(input("Digite o peso(1): "))
nota2 = float(input("Digite a 2º nota: "))
peso2 = float(input("Digite o peso(2): "))

MP = ((nota1*peso1+nota2*peso2)/(peso1 + peso2))
print(f"Média: {MP:.2f}")