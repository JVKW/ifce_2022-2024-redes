"""Escreva um algoritmo que leia 3 notas de um aluno e uma letra. Se a letra for A o algoritmo deve calcula a média aritmética media = (n1 + n2 + n3)/3 das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) media = (5n1 + 3n2 + 2n3)/5 + 3 + 2 e se for H, a sua média harmônica media = (n1 + n2 + n3)/(1/n1 + 1/n2 + 1/n3)."""

n1 = float(input("Digite a primeira Nota: "))
n2 = float(input("Digite a segunda Nota: "))
n3 = float(input("Digite a tericeira Nota: "))
letter = str(input("Que cálculos desejas fazer?\n[A] Cáculo Aritmétrico\n[P] Cálculo Ponderado\n[H] Cálculo "
                   "Harmônico\n> "))

if letter in "Aa":
    result = ((n1 + n2 + n3) / 3)
    print(f"Sua nota em Cálculo Aritmétrico:  {result:.2f}")
elif letter in "Pp":
    result = (5 * n1 + 3 * n2 + 2 * n3) / (5 + 3 + 2)
    print(f"Sua nota em Cálculo Ponderado: {result:.2f}, com pesos (5,3,2)")
elif letter in "Hh":
    result = (n1 + n2 + n3) / ((1 / n1) + (1 / n2) + (1 / n3))
    print(f"Sua nota em Cáculo Harmônico: {result:.2f}")
