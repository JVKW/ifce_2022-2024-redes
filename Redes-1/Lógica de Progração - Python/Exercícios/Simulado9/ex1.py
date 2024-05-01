"""Escreva um programa Python para obter uma string feita de 4 cópias dos dois últimos caracteres de uma string recebida
pelo usuário (o comprimento deve ser pelo menos 2)."""

# Exemplo 1: 'Python' -> onononon
# Exemplo 2: ‘Lares’ -> eseseses

name = str(input("Escreva um nome: "))

print(f"Últimos 2 caracteres: {name[-2:]*4}")