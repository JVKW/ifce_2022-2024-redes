"""“Pega ladrão! Pega ladrão!”. Roubaram a bolsa da Júlia que caminhava no Parque da
Cidade, na altura do Brisa da Lagoa e o ladrão fugiu em direção ao lago. Seu plano
parece óbvio: ele pretende pegar um drone e escapar!
O fugitivo, que a essa altura já está pendurado no seu drone de fuga, pretende atravessar
o lago, que fica a 12 milhas náuticas de distância, onde estará são e salvo das
autoridades locais. Por sorte, seu amigo Dimitri tem um Pedalinho Aquático em formato de
Cisne consegue percorrer essa distância a uma velocidade constante de VF nós (a
medida de velocidade no mar).

Dimitri pretende interceptá-lo, e sua embarcação tem uma velocidade constante de VP
nós. Supondo que ambos, o drone que carrega gente do ladrão e o pedalinho do Dimitri
partam da costa exatamente no mesmo instante, com uma distância de D milhas náuticas
entre eles, será possível o Dimitri alcançar o ladrão antes do ladrão chegar do outro lado
e fugir?

Assuma que o trajeto é perfeitamente retilíneo e a lagoa é bastante calma, de forma a
permitir uma trajetória tão retilínea quanto possível.
A tabela abaixo ilustra alguns exemplos que cenários que poderiam acontecer. D, VF e
VP, indicam, respectivamente, a distância inicial entre o fugitivo e o pedalinho, a
velocidade do drone do fugitivo e a velocidade do pedalinho.

[ Tabela no README.md do diretório pai ]

QUESTÃO: Você deve escrever um programa que tenha uma lista, com três elementos,
indicando a distância D, a velocidade VF e a velocidade VP. Faça o algoritmo em Python
para mostrar se dado um cenário hipotético, o Ladrão conseguiria ficar com a bolsa."""

def ladrão_escapará(D, VF, VP):
    distancia_lago = 12
    
    tempo_ladrao = distancia_lago / VF
    
    tempo_dimitri = D / (VP - VF) if VP > VF else float('inf')
    
    if tempo_dimitri <= tempo_ladrao:
        return "Dimitri conseguirá alcançar o ladrão."
    else:
        return "O ladrão conseguirá fugir com a bolsa."

cenario = [5, 10, 12]
resultado = ladrão_escapará(*cenario)
print(resultado)
