# 60- faça um programa que leia um numero qualquer e mostre o seu fatorial.
# EX: 5! = 5x4x3x2x1 = 120

from math import factorial
n = int(input('Digite um numero: '))
fat = factorial(n)
print('O Fatorial do numero {} é {:.2f}'.format(n, fat))