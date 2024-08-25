"""Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:"""

# ACESSO PERMITIDO caso a senha seja válida.
# ACESSO NEGADO caso a senha seja inválida.

# O programa só para quando o acesso é permitido.

password = 1234

while True:
    resp = int(input("Digite a senha: "))
    if resp == password:
        print("ACESSO PERMITIDO")
        break
    else:
        print("ACESSO NEGADO")
        continue