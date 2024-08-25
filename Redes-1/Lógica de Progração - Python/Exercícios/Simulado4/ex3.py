"""Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao solicitar R$ 18, o programa deve informar apenas a seguinte informação (note que não foram exibidas informações sobre as demais cédulas):"""
# 1 nota(s) de R$ 10.
# 1 nota(s) de R$ 5.
# 3 nota(s) de R$ 1.

sol = int(input("Digite uma quantia inteira: R$"))
res = sol

if sol >= 100:
    n100 = int(sol / 100)
    print(f"Você necessita de {n100} notas de R$100,00")
    res = sol - (n100 * 100)
if res >= 50:
    n50 = int(res / 50)
    print(f"Você necessita de {n50} notas de R$50,00 ")
    res = res - (n50 * 50)
if res >= 10:
    n10 = int(res / 10)
    print(f"Você necessita de {n10} notas de R$10,00")
    res = res - (n10 * 10)
if res >= 5:
    n5 = int(res / 5)
    print(f"Você necessita de {n5} notas de R$5,00")
    res = res - (n5 * 5)
if res >= 1:
    n1 = int(res / 1)
    print(f"Você necessita de {n1} notas de R$1,00")
    res = res - (n1 * 1)
