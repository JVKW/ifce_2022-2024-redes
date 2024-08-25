# Lista de Questões - Simulado 1 - Listas e Strings - 05/outubro/2022

## Simulado 12

1. **Exercício 1:**  
   Ana Emilly é uma enfermeira em um grande hospital de Tauá–CE, e tem os horários de trabalho muito variáveis. Para piorar, ela tem sono pesado, e uma grande dificuldade para acordar com relógios despertadores. Recentemente ela ganhou de presente de Tatielly um relógio digital, com alarme com vários tons, e tem esperança que isso resolva o seu problema. No entanto, ela anda muito cansada e quer aproveitar cada momento de descanso. Por isso, carrega seu relógio digital despertador para todos os lugares, e sempre que tem um tempo de descanso procura dormir, programando o alarme despertador para a hora em que tem que acordar. No entanto, com tanta ansiedade para dormir, acaba tendo dificuldades para adormecer e aproveitar o descanso.

   Um problema que a tem atormentado na hora de dormir é saber quantos minutos ela teria de sono se adormecesse imediatamente e acordasse somente quando o despertador tocasse. Mas ela realmente não é muito boa com números, e pediu sua ajuda para escrever um programa que, dada a hora corrente e a hora do alarme, determine o número de minutos que ela poderia dormir.

   | Alarme          | Resposta |
   |-----------------|----------|
   | [1, 5, 3, 5]    | 120      |
   | [23, 59, 0, 34] | 25       |
   | [21, 33, 21, 10]| 1417     |
   | [0, 0, 0, 0]    | 0        |

   **QUESTÃO:** Você deve escrever um programa que recebe quatro números, `h1`, `m1`, `h2`, `m2` e cria uma lista com tamanho 04, ou seja, `alarme = [h1, m1, h2, m2]`. Faça o algoritmo em Python para mostrar um número inteiro, indicando o número de minutos que Ana Emilly tem para dormir.

2. **Exercício 2:**  
   “Pega ladrão! Pega ladrão!”. Roubaram a bolsa da Júlia que caminhava no Parque da Cidade, na altura do Brisa da Lagoa e o ladrão fugiu em direção ao lago. Seu plano parece óbvio: ele pretende pegar um drone e escapar!

   O fugitivo, que a essa altura já está pendurado no seu drone de fuga, pretende atravessar o lago, que fica a 12 milhas náuticas de distância, onde estará são e salvo das autoridades locais. Por sorte, seu amigo Dimitri tem um Pedalinho Aquático em formato de Cisne consegue percorrer essa distância a uma velocidade constante de `VF` nós (a medida de velocidade no mar).

   Dimitri pretende interceptá-lo, e sua embarcação tem uma velocidade constante de `VP` nós. Supondo que ambos, o drone que carrega gente do ladrão e o pedalinho do Dimitri partam da costa exatamente no mesmo instante, com uma distância de `D` milhas náuticas entre eles, será possível o Dimitri alcançar o ladrão antes do ladrão chegar do outro lado e fugir?

   Assuma que o trajeto é perfeitamente retilíneo e a lagoa é bastante calma, de forma a permitir uma trajetória tão retilínea quanto possível.

   | Cenário         | O Ladrão conseguiu ficar com a bolsa? |
   |-----------------|---------------------------------------|
   | [5, 1, 12]      | Não                                   |
   | [12, 10, 7]     | Sim                                   |
   | [12, 9, 10]     | Sim                                   |
   | [9, 12, 15]     | Não                                   |

   **QUESTÃO:** Você deve escrever um programa que tenha uma lista, com três elementos, indicando a distância `D`, a velocidade `VF` e a velocidade `VP`. Faça o algoritmo em Python para mostrar se dado um cenário hipotético, o Ladrão conseguiria ficar com a bolsa.

3. **Exercício 3:**  
   Um número é chamado de número da sorte do Gabriel T quando a soma de cada um dos seus dígitos eleva à quantidade de dígitos do número equivale ao próprio número, por exemplo, 153 e 93084 são números da sorte, já que:

   153 = 1^3 + 5^3 + 3^3  
   93084 = 9^5 + 3^5 + 0^5 + 8^5 + 4^5

   **QUESTÃO:** Suponha que você recebe uma lista (com tamanho qualquer) em que cada elemento possui um dígito. Faça um programa em Python que indique se um número é da sorte ou não.

   | Número          | É da sorte? |
   |-----------------|-------------|
   | [1, 5, 3]       | Sim         |
   | [1, 5, 4]       | Não         |
   | [5, 2, 0, 8]    | Sim         |
   | [1, 6, 3, 5]    | Não         |
   | [9, 2, 7, 2, 7] | Sim         |
