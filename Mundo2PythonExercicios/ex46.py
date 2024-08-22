# 46- Faça um programa que mostre na tela uma contagem regressiva de fogos de artificio de 10 a 0 com 1 segundo de pausa entre cada.

from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('BUMMMMMMMMM')
