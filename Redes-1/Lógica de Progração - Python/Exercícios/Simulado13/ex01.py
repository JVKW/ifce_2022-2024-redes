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

[ Tabela no README.md do diretório pai ]

QUESTÃO: Você deve escrever um programa que recebe quatro números, h1, m1, h2, m2
e cria uma lista com tamanho 04, ou seja, alarme = [h1, m1, h2, m2]. Faça o algoritmo em
Python para mostrar um número inteiro, indicando o número de minutos que Ana Emilly
tem para dormir.""",

def calcular_minutos_sono(h1, m1, h2, m2):
    minutos_atual = h1 * 60 + m1
    minutos_alarme = h2 * 60 + m2

    if minutos_alarme >= minutos_atual:
        minutos_sono = minutos_alarme - minutos_atual
    else:
        minutos_sono = (1440 - minutos_atual) + minutos_alarme

    return minutos_sono

h1, m1, h2, m2 = 22, 30, 6, 0 
alarme = [h1, m1, h2, m2]
minutos_sono = calcular_minutos_sono(*alarme)

print("Ana Emilly tem", minutos_sono, "minutos para dormir.")