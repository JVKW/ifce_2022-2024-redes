"""Faça um algoritmo para calcular a média aritmética M entre duas notas de um aluno e mostrar sua situação, que pode ser aprovado (M ≥ 7), reprovado (M < 4) e AF (4 ≤ M < 7)."""

nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

M = ((nota1 + nota2)/2)

if M >= 7:
    print("Situação: Aprovado")
    print(M)
elif M < 4:
    print("Situação: Reprovado")
    print(M)
elif M > 4 and M < 7:
    print("Situação: AF")
    print(M)