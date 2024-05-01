"""Faça um algoritmo que receba um valor referente a uma compra em dólar no cartão de crédito, calcule e mostre o valor
de conversão para real sabendo que em compras internacionais incide-se sobre o total uma taxa de IOF com valor de 6,38%.
 Adote o valor do dólar R$ 4,35."""

dolar = float(input("Valor em Dólar: $"))
reais = dolar * 4.35 + (dolar*0.0638)

print(f"Valor de ${dolar}\nR${reais:.2f}")