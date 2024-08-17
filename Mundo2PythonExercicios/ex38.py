# 38 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior.
# o segundo valor é maior.
# não existe valor maior, os dois são iguais.

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if n1 > n2 :
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Os valores são iguais.')