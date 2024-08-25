"""João e Maria são amigos desde a creche. Desde então, eles compartilharam uma lúdica
rotina: cada vez que se encontram, jogam Cara ou Coroa com uma moeda, e quem
ganhar tem o privilégio de decidir o que vai pagar o açaí do dia. Maria sempre escolhe
Cara, e João sempre escolhe a cauda. Hoje eles estão na faculdade, mas continuam
sendo bons amigos. Sempre que se encontram, eles ainda jogam Cara ou Coroa, e o
perdedor faz um PIX para o vencedor no valor de R$ 50,00.

Ontem, a Maria confidenciou a João que tem mantido um registro dos resultados de cada
brincam desde que começaram, na creche. Foi uma surpresa para o João! Mas como
João faz Ciência da Computação, ele decidiu que era uma boa oportunidade para mostrar
a Maria suas habilidades em programação, escrevendo um programa para determinar o
número de vezes que cada um deles ganhou o jogo ao longo dos anos. Você é o João na
prova e vai precisar fazer o programa.

Tem uma colher de chá, existe uma função que o João não viu na faculdade, mas ele
sabe como funciona. Essa função se chama sum (soma em inglês) e ela soma todos os
valores de uma lista e retorna o total.
Exemplo:

n = sum([1, 2, 3, 4]) # n = 1 + 2 + 3 + 4 = 10
m = sum([-1, -2, 3, 4]) # m = -1 - 2 + 3 + 4 = 4

A tabela abaixo ilustra alguns exemplos que podem estar no caderno de Maria.

[ Tabela no README.md do diretório pai ]

QUESTÃO: Você deve escrever um programa que tenha uma lista, caderno, e você não
sabe qual o tamanho dela, mas sabe que ela tem os valores de todos os jogos. Faça o
algoritmo em Python para mostrar quantas vezes Maria e João ganharam."""

cadern = []
n = 1

while True:
    resp = int(input(f"Quem ganhou o {n}º jogo?\n[1]João\n[2]Maria\n(Digite '0' para finalizar.)\n"))
    if resp == 1:
        cadern.append(1)
        print("João ganhou essa rodada!")
        n = n + 1
    elif resp == 2:
        cadern.append(2)
        print("Maria ganhou essa rodada!!")
        n = n + 1
    elif resp == 0:
        print("A contagem foi finalizada!")
        print(f"João fez: {cadern.count(1)} pontos.")
        print(f"Maria fez: {cadern.count(2)} pontos.")
        if cadern.count(1) > cadern.count(2):
            print("João Venceu!")
        elif cadern.count(2) > cadern.count(1):
            print("Maria Venceu!")
        else:
            print("Empate!")
        quit()
    else:
        print("Digite um valor exato!")
