"""Faça um programa para simular o teste da COVID-19 com o resultado do exame IgG e IgM. O programa pergunta o resultado
de cada exame (1-positivo e 2-negativo) e mostra se você teve COVID-19 ou não."""

IgG = int(input("Qual o resultado do teste IgG?\n[1]Positivo\n[2]Negativo\n> "))
ImG = int(input("Qual o resultado do teste ImG?\n[1]Positivo\n[2]Negativo\n> "))

if (IgG == 2) and (ImG == 2):
    print("Resultado: Não pegou")
elif (IgG == 1) or (ImG == 1):
    print("Resultado: Pegou")

#OBS: Como qualquer caso se resultado de IgG e ImG for verdadeiro, o resultado será "Pegou", não necessita dar todos os
#valores possíveis.