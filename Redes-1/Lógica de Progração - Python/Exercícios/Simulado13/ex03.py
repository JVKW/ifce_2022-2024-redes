"""Um número é chamado de número da sorte do Gabriel T quando a soma de cada um dos seus dígitos eleva à quantidade de digitos do número equivale ao próprio número, por exemplo, 153 e 93084 são números da sorte, já que:"""

# 153 = 1^3 + 5^3 + 3^3
# 93084 = 9^5 + 3^5 + 0^5 + 8^5 + 4^5

"""QUESTÃO: Suponha que você recebe uma lista (com tamanho qualquer) em que cada elemento possui um dígito. Faça um programa em Python que indique se um número é da sorte ou não"""

# [ Tabela no README.md do diretório pai ]

def eh_numero_da_sorte(numero):
    numero_str = str(numero)
    quantidade_digitos = len(numero_str)
    soma_potencias = sum(int(digito) ** quantidade_digitos for digito in numero_str)
    return soma_potencias == numero

numeros = [153, 93084, 9474, 9475]

for num in numeros:
    if eh_numero_da_sorte(num):
        print(f"{num} é um número da sorte do Gabriel T.")
    else:
        print(f"{num} não é um número da sorte do Gabriel T.")
