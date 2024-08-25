"""Escreva um programa que pergunte o raio de uma circunferência, e sem seguida mostre o diâmetro, comprimento e área da circunferência."""

from math import pi

raio = float(input("Raio da Circuferência: "))
print(f"\nDiâmetro: {raio*2}\nComprimento: {2*pi*raio:.2f}\nÁrea: {pi*(raio**2):.2f}")
