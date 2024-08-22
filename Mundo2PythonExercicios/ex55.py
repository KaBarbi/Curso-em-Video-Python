# 55- Faça um programa que leia o peso de 5 pessoas e no final mostre o maior e o menor dos pesos lidos.
from wsgiref.types import InputStream

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))
