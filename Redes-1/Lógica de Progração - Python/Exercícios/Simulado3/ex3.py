"""Faça um programa que pede a nota final de um aluno na disciplina de lógica de computadores. Em seguida, o programa
deve mostrar o seguinte resultado:"""

# A. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# B. A mensagem "Reprovado", se a média for menor do que quatro;
# C. A mensagem “Prova final”, se a média for maior que quatro e menor que sete;
# D. A mensagem "Aprovado com Distinção", se a média for igual a dez.

NF = float(input("Indique sua Nota Final: "))

if NF >= 7:
    print("Aprovado!")
elif NF < 4:
    print("Reprovado!")
elif 4 < NF < 7:
    print("Prova Final!")
elif NF == 10:
    print("Aprovado com Distinção.")
