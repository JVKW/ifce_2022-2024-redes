"""Ana Emilly é uma enfermeira em um grande hospital de Tauá–CE, e tem os horários de
trabalho muito variáveis. Para piorar, ela tem sono pesado, e uma grande dificuldade para
acordar com relógios despertadores.
Recentemente ela ganhou de presente de Tatielly um relógio digital, com alarme com
vários tons, e tem esperança que isso resolva o seu problema. No entanto, ela anda muito
cansada e quer aproveitar cada momento de descanso. Por isso, carrega seu relógio
digital despertador para todos os lugares, e sempre que tem um tempo de descanso
procura dormir, programando o alarme despertador para a hora em que tem que acordar.
No entanto, com tanta ansiedade para dormir, acaba tendo dificuldades para adormecer e
aproveitar o descanso.

Um problema que a tem atormentado na hora de dormir é saber quantos minutos ela teria
de sono se adormecesse imediatamente e acordasse somente quando o despertador
tocasse. Mas ela realmente não é muito boa com números, e pediu sua ajuda para
escrever um programa que, dada a hora corrente e a hora do alarme, determine o número
de minutos que ela poderia dormir.

A tabela abaixo ilustra alguns exemplos que podem estar no alarme da Ana Emilly.

QUESTÃO: Você deve escrever um programa que recebe quatro números, h1, m1, h2, m2
e cria uma lista com tamanho 04, ou seja, alarme = [h1, m1, h2, m2]. Faça o algoritmo em
Python para mostrar um número inteiro, indicando o número de minutos que Ana Emilly
tem para dormir.""",

# REFAZER

alarme = []

"""
h1 = int(input("Digite a hora que Emilly adormeceu: "))
if (h1 > 24) or (h1 < 0):
    print("Digite um horário existente!")
    quit()
    
m1 = int(input("Digite o minuto que Emilly adormeceu: "))
if (m1 > 60) or (m1 < 0):
    print("Digite um valor em minutos existente!")
    quit()
    
h2 = int(input("Digite a hora que Emilly Acordou: "))
if (h2 > 24) or (h2 < 0):
    print("Digite um horário existente!")
    quit()

m2 = int(input("Digite o minuto que Emilly Acordou: "))
if (m2 > 60) or (m2 < 0):
    print("Digite um valor em minutos existente!")
    quit()


print(f"Emilly dormiu: {abs(h2 - h1)} horas(h) e {abs(m2 - m1)} minutos(m).")
if (h2 == h1) and (m2 == m1):
    print(f"Emilly dormiu: {abs(h2 - h1)} horas(h) e {abs(m2 - m1)} minutos(m).")
    print("Status: Ainda dormindo.")
elif (h2 == 0) and (h1 > 0):
    print(f"Emilly dormiu: {abs(24 - h1)} horas(h) e {abs(m2 - m1)} minutos(m).")
"""
for i in range(4):
    num = int(input(f"Digite um horário{i + 1}: "))
    alarme.append(num)
print(alarme)

