# Lista de Questões - Simulado 11 - Listas e Strings - 05/outubro/2022

## Simulado 11

1. **Exercício 1:**  
   O Oráculo é um jogo que foi criado por um engenheiro de telecomunicações chamado
   Mordechai Meirovitz, da Romênia, em 1971. O jogo foi premiado com o prestigioso “Jogo
   do Ano” em 1974 e foi um enorme sucesso comercial, tendo sido vendido em mais de 40
   países.

   O Oráculo é um jogo de lógica em que seu objetivo como jogador é descobrir uma senha
   secreta escolhida por um jogador adversário. A senha a ser encontrada é uma sequência
   de valores de um determinado alfabeto (conjunto de símbolos). Para descobrir qual é a
   senha, você envia “palpites” ao seu oponente. Um palpite é um senha possível. Ou seja,
   um palpite é uma lista do mesmo número de elementos que a senha, do mesmo alfabeto.
   Após cada palpite, você recebe uma resposta, que consiste em dois números inteiros, (E,
   B), indicando quão bom seu palpite foi. Se um caractere em um palpite existir na senha na
   mesma posição (da lista), então conta como “excelente” (E). Caso contrário, se existir um
   valor tanto no palpite quanto na senha, mas em uma posição diferente na corda, então
   conta como “bom” (B). Um único valor de um palpite não é contado duas vezes (ou seja,
   se é contado como excelente, não é contado como bom). A tabela abaixo ilustra alguns
   exemplos.

   Com base nas respostas recebidas após cada palpite, um jogador pode eventualmente
   deduzir qual é a senha. O objetivo do jogo é descobrir a senha com o mínimo de
   tentativas.

   | Senha         | Palpite       | Resposta | Observação                                                                                   |
   |---------------|---------------|----------|----------------------------------------------------------------------------------------------|
   | [1, 2, 3, 3]  | [3, 2, 4, 3]  | E=2, B=1 | 2 e o segundo 3 estão na mesma posição tanto na senha quanto no palpite, e o primeiro 3 também existe na senha, mas em outra posição. |
   | [1, 2, 3, 3]  | [3, 0, 0, 0]  | E=0, B=1 | O único valor coincidente na senha e no palpite é o 3, mas em posições diferentes.           |
   | [1, 2, 3, 3]  | [4, 4, 5, 5]  | E=0, B=0 | 4 e 5 não estão presentes na senha.                                                          |
   | [1, 2, 3, 4]  | [1, 2, 3, 4]  | E=4, B=0 | Correto.                                                                                     |

   QUESTÃO: Você deve escrever um programa que tenha duas listas, senha e palpite,
   ambas com tamanho 04. Faça o algoritmo em Python para mostrar todas as posições
   deduzidas após um conjunto de palpites e respostas, isto é, o E e o B.

2. **Exercício 2:**  
   João e Maria são amigos desde a creche. Desde então, eles compartilharam uma lúdica
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

   | Caderno          | Observação      |
   |-----------------|---------------|
   | [0, 0, 1, 0, 1]    | Maria ganhou 03 vezes e João 02 vezes              |
   | [0, 0, 0, 0, 0, 1] | Maria ganhou 05 vezes e João 01 vezes              |
   | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]| Maria ganhou 11 vezes e João 00 vezes              |

   QUESTÃO: Você deve escrever um programa que tenha uma lista, caderno, e você não
   sabe qual o tamanho dela, mas sabe que ela tem os valores de todos os jogos. Faça o
   algoritmo em Python para mostrar quantas vezes Maria e João ganharam.
