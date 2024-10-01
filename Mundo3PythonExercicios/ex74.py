#Crie um programa que vai gerar 5 numeros aleatorias e colocar em uma tupla.
#epois disso, mostre a listagem de numeros gerados e também indique o menor valor e o maior na tupla.

import random

numeros = tuple(random.randint(1, 100) for _ in range(5))

print("Números gerados:", numeros)

menor_valor = min(numeros)
maior_valor = max(numeros)

print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)