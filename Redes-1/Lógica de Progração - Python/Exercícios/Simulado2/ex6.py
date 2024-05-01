"""Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234.
Devem ser impressas as seguintes mensagens:"""

# ACESSO PERMITIDO caso a senha seja válida.
# ACESSO NEGADO caso a senha seja inválida.

password = 1234

resp = int(input("Digite a senha: "))

if resp == password:
    print("ACESSO PERMITIDO")
elif resp != password:
    print("ACESSO NEGADO")
else:
    print("Erro!")