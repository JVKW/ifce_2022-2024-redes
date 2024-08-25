"""O Oráculo é um jogo que foi criado por um engenheiro de telecomunicações chamado
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

[ Tabela no README.md do diretório pai ]

QUESTÃO: Você deve escrever um programa que tenha duas listas, senha e palpite,
ambas com tamanho 04. Faça o algoritmo em Python para mostrar todas as posições
deduzidas após um conjunto de palpites e respostas, isto é, o E e o B."""

palpite = []
senha = ['1', '2', '3', '4']
excelente = 0
bom = 0

while True:
    r = str(input("Digite uma senha de 4 números: "))
    if (len(r) > 0) and (len(r) <= 4):
        for i in r:
            palpite.append(i)
        break
    else:
        print("Digite uma senha como solicitada!")


"""bom = len([i for i in palpite if i in senha])"""

for i in palpite:
    if i in senha:
        bom = bom + 1
   
for y in range(len(senha)):
    if palpite[y] == senha[y]:
        excelente = excelente + 1
        bom = bom - 1

print(f"Bom: {bom}")
print(f"Excelente: {excelente}")
        

