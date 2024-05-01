"""Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir
 10, 9, 8, ..., 1, 0 e Fogo! na tela."""

import time

clock = 10  # segundos

print("Iniciando lançamento...")
time.sleep(1)
for i in range(clock, -1, -1):
    time.sleep(1)
    print(i)
time.sleep(1)
print("FOGO!")